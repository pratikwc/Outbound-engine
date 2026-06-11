"""
Whitecarrot — Contact Personalization Script
=============================================
Reads Apollo Contacts Found sheet, generates personalization for each unfilled
contact using Claude, and writes results directly back to the sheet.

Fills columns:
  AB = Qualify Contact?
  AC = Persona Brief
  AD = email_body
  AE = research_signal
  AF = fallback_flag

Usage:
  python personalize.py                  # Process all unfilled contacts
  python personalize.py --limit 50       # Process first 50 unfilled contacts
  python personalize.py --dry-run        # Preview without writing to sheet

Requirements:
  pip install anthropic google-auth google-auth-httplib2 google-api-python-client python-dotenv

.env must contain:
  GOOGLE_SERVICE_ACCOUNT_EMAIL=...
  GOOGLE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n..."
  ANTHROPIC_API_KEY=sk-ant-...

Note: The Google service account must have EDITOR access to the spreadsheet.
      Share the sheet with founders-os-reader@founders-os-497313.iam.gserviceaccount.com
      and set role to Editor (not Viewer).
"""

import os
import sys
import json
import time
import argparse
from dotenv import load_dotenv

load_dotenv()

# ── Config ──────────────────────────────────────────────────────────────────
SPREADSHEET_ID = "1t6qIBAqE1kbnbJDDJQiGigvpgxWLwQuOWB-Su_4CUxQ"
SHEET_NAME     = "Apollo Contacts Found"
READ_RANGE     = f"'{SHEET_NAME}'!A:AF"

# Column indices (0-based, matching Apollo Contacts Found layout)
C = {
    "first_name":        0,   # A
    "last_name":         1,   # B
    "title":             2,   # C
    "company":           3,   # D
    "email":             4,   # E
    "seniority":         9,   # J
    "departments":       10,  # K
    "lists":             15,  # P
    "city":              19,  # T
    "country":           21,  # V
    "apollo_acct_id":    24,  # Y
    "has_ats":           26,  # AA  (already filled upstream)
    "qualify_contact":   27,  # AB  ← we fill this
    "persona_brief":     28,  # AC  ← we fill this
    "email_body":        29,  # AD  ← we fill this
    "research_signal":   30,  # AE  ← we fill this
    "fallback_flag":     31,  # AF  ← we fill this
}
WRITE_START_COL = "AB"   # First column we write to
WRITE_END_COL   = "AF"   # Last column we write to

CLAUDE_MODEL = "claude-haiku-4-5-20251001"

# ── ICP qualifier — titles we care about ────────────────────────────────────
ICP_TITLE_KEYWORDS = [
    "hr", "human resources", "people", "talent", "recruitment",
    "recruiter", "chro", "cpo", "head of hr", "vp people",
    "talent acquisition", "workforce", "personnel",
]

# ── Google Sheets setup ──────────────────────────────────────────────────────
def get_sheets_service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    private_key = os.getenv("GOOGLE_PRIVATE_KEY", "").replace("\\n", "\n")
    client_email = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL", "")

    if not private_key or not client_email:
        sys.exit("ERROR: GOOGLE_SERVICE_ACCOUNT_EMAIL or GOOGLE_PRIVATE_KEY missing from .env")

    creds = service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "project_id": "founders-os-497313",
            "private_key_id": "key",
            "private_key": private_key,
            "client_email": client_email,
            "client_id": "",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        },
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


# ── Read contacts ────────────────────────────────────────────────────────────
def read_contacts(service):
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=READ_RANGE)
        .execute()
    )
    rows = result.get("values", [])
    if len(rows) < 2:
        print("Sheet appears empty.")
        return []
    return rows[1:]  # skip header row


def pad(row, length=40):
    return row + [""] * max(0, length - len(row))


def get(row, key):
    return row[C[key]].strip() if len(row) > C[key] else ""


def needs_fill(row):
    return not get(row, "email_body")


# ── Claude prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are writing cold email copy for Whitecarrot — an AI recruitment software
for 100–1,000 person companies in UAE and KSA.

Whitecarrot: centralises the hiring pipeline, uses AI to speed up recruitment.
ROI: pays for itself in under 11 months on recruiter time savings. Time-to-hire
↓55% on average. Clients like Alabbar Enterprises (3 recruiters, 850 hires/yr).

Voice rules (non-negotiable):
- Under 15 seconds silent reading time. Typically 60–80 words for the body.
- No buzzwords: no "leverage", "synergy", "game-changer", "skyrocket", "cutting-edge"
- No long intros. Line 1 = the hook. Get to the point.
- Write like a human, not a template.
- Sign-off: Pratik, Whitecarrot

Email format:
  Subject: [subject line]
  [blank line]
  [email body, 3–4 short paragraphs or sentences]

Always return ONLY a valid JSON object — no prose before or after."""

def build_user_prompt(row):
    row = pad(row)
    name      = f"{get(row,'first_name')} {get(row,'last_name')}".strip()
    title     = get(row, "title")
    company   = get(row, "company")
    city      = get(row, "city")
    country   = get(row, "country")
    seniority = get(row, "seniority")
    dept      = get(row, "departments")
    has_ats   = get(row, "has_ats")
    segment   = get(row, "lists")

    # Determine qualify_contact from title keywords
    title_lower = title.lower()
    is_icp = any(kw in title_lower for kw in ICP_TITLE_KEYWORDS)
    qualify_hint = "yes" if is_icp else "no"

    return f"""Contact info:
  Name: {name}
  Title: {title}
  Company: {company}
  Location: {city}, {country}
  Seniority: {seniority}
  Department: {dept}
  Has ATS: {has_ats or "unknown"}
  Segment: {segment}
  ICP title match: {qualify_hint}

Generate a JSON object with exactly these fields:

{{
  "qualify_contact": "yes" or "no"  // Is this person worth emailing? HR/Talent/People title = yes. C-suite at ≤1000 = yes. Finance/legal/IT = no.
  "persona_brief": "One sentence. Who they are + why they're a fit. Max 20 words. No fluff.",
  "research_signal": "The hook. Max 15 words. Base it on ATS status, company size, or industry — never make up a fact.",
  "email_body": "Full email. Subject on first line as 'Subject: ...'. Then blank line. Then 3–4 tight lines. Under 80 words total. Sign off: Pratik, Whitecarrot.",
  "fallback_flag": "yes" if you used a generic opener because no signal was available, else "no"
}}"""


# ── Claude call ───────────────────────────────────────────────────────────────
def personalize(client, row):
    import anthropic
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=600,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_prompt(row)}],
    )
    text = message.content[0].text.strip()

    # Extract JSON block
    start = text.find("{")
    end   = text.rfind("}") + 1
    if start == -1 or end <= start:
        raise ValueError(f"No JSON found in response:\n{text}")
    return json.loads(text[start:end])


# ── Write back to sheet ───────────────────────────────────────────────────────
def write_row(service, data_row_index, result):
    sheet_row = data_row_index + 2  # +1 header, +1 for 1-based index
    values = [[
        result.get("qualify_contact", ""),
        result.get("persona_brief", ""),
        result.get("email_body", ""),
        result.get("research_signal", ""),
        result.get("fallback_flag", ""),
    ]]
    range_str = f"'{SHEET_NAME}'!{WRITE_START_COL}{sheet_row}:{WRITE_END_COL}{sheet_row}"
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_str,
        valueInputOption="RAW",
        body={"values": values},
    ).execute()


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit",   type=int, default=None, help="Max contacts to process")
    parser.add_argument("--dry-run", action="store_true",    help="Preview without writing")
    parser.add_argument("--list",    type=str, default=None, help="Only process contacts in this Apollo list name (substring match)")
    args = parser.parse_args()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ERROR: ANTHROPIC_API_KEY missing from .env")

    import anthropic
    client  = anthropic.Anthropic(api_key=api_key)
    service = get_sheets_service()

    print(f"Reading contacts from '{SHEET_NAME}'...")
    all_rows = read_contacts(service)
    print(f"Total rows: {len(all_rows)}")

    # Filter: unfilled only
    queue = [(i, r) for i, r in enumerate(all_rows) if needs_fill(r)]

    # Optional list filter
    if args.list:
        queue = [(i, r) for i, r in queue if args.list.lower() in get(r, "lists").lower()]
        print(f"Filtered to list '{args.list}': {len(queue)} contacts")

    # Apply limit
    if args.limit:
        queue = queue[:args.limit]

    print(f"Contacts to personalize: {len(queue)}")
    if not queue:
        print("Nothing to do — all contacts already have email_body filled.")
        return

    if args.dry_run:
        print("\n[DRY RUN — no changes will be written]\n")

    ok = 0
    fail = 0

    for idx, (row_index, row) in enumerate(queue):
        name    = f"{get(row,'first_name')} {get(row,'last_name')}".strip() or "?"
        company = get(row, "company") or "?"
        label   = f"[{idx+1}/{len(queue)}] {name} @ {company}"

        try:
            result = personalize(client, row)

            if args.dry_run:
                print(f"\n{label}")
                print(f"  qualify: {result.get('qualify_contact')}")
                print(f"  signal:  {result.get('research_signal')}")
                print(f"  brief:   {result.get('persona_brief')}")
                print(f"  fallback:{result.get('fallback_flag')}")
                print(f"  email:\n{result.get('email_body','').strip()}")
            else:
                write_row(service, row_index, result)
                print(f"{label}  ✓  (qualify={result.get('qualify_contact')}, fallback={result.get('fallback_flag')})")

            ok += 1

        except Exception as e:
            print(f"{label}  ✗  {e}")
            fail += 1

        # Polite rate limit: ~3 req/sec
        if not args.dry_run:
            time.sleep(0.4)

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Done — {ok} personalized, {fail} failed.")


if __name__ == "__main__":
    main()

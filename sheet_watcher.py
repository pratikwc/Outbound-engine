"""
Whitecarrot Sheet Watcher
=========================
Run this ONCE in the background. It watches for a pending_sheet_updates.json
file that Cowork (Claude) drops when it finishes personalizing contacts.
As soon as the file appears, it writes the data to the Google Sheet and
removes the file.

Usage:
  python sheet_watcher.py

Keep this running in a terminal. You can start it at login by adding it
to Windows Task Scheduler (Action = python.exe, Argument = full path to this file).
"""

import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# ── Config ──────────────────────────────────────────────────────────────────
HERE              = Path(__file__).parent
PENDING_FILE      = HERE / "pending_sheet_updates.json"
DONE_FILE         = HERE / "last_sheet_write.json"
SPREADSHEET_ID    = "1t6qIBAqE1kbnbJDDJQiGigvpgxWLwQuOWB-Su_4CUxQ"
SHEET_NAME        = "Apollo Contacts Found"
POLL_INTERVAL_SEC = 3   # check every 3 seconds

load_dotenv(HERE / ".env")


def get_sheets_service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    private_key   = os.getenv("GOOGLE_PRIVATE_KEY", "").replace("\\n", "\n")
    client_email  = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL", "")

    if not private_key or not client_email:
        sys.exit("ERROR: Missing Google credentials in .env")

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


def find_row_by_email(service, email: str) -> int | None:
    """Return 1-based sheet row for a contact email, or None if not found."""
    result = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"'{SHEET_NAME}'!E:E",   # Column E = Email
        )
        .execute()
    )
    emails = result.get("values", [])
    for idx, row in enumerate(emails):
        if row and row[0].strip().lower() == email.strip().lower():
            return idx + 1  # 1-based
    return None


def write_updates(service, updates: list[dict]) -> dict:
    """
    Batch-write personalization columns AB–AF for a list of contacts.
    Each update must have: email, qualify_contact, persona_brief,
                           email_body, research_signal, fallback_flag
    Returns a summary dict.
    """
    ok, skipped = [], []

    batch_data = []
    for u in updates:
        email = u.get("email", "").strip()
        if not email:
            skipped.append({"email": "MISSING", "reason": "no email field"})
            continue

        row = find_row_by_email(service, email)
        if row is None:
            skipped.append({"email": email, "reason": "not found in sheet"})
            continue

        range_str = f"'{SHEET_NAME}'!AB{row}:AF{row}"
        batch_data.append({
            "range": range_str,
            "values": [[
                u.get("qualify_contact", ""),
                u.get("persona_brief",    ""),
                u.get("email_body",       ""),
                u.get("research_signal",  ""),
                u.get("fallback_flag",    ""),
            ]],
        })
        ok.append(email)

    if batch_data:
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body={
                "valueInputOption": "RAW",
                "data": batch_data,
            },
        ).execute()

    return {"written": ok, "skipped": skipped}


def process_pending(service):
    with open(PENDING_FILE) as f:
        payload = json.load(f)

    updates = payload if isinstance(payload, list) else payload.get("updates", [])
    print(f"  Processing {len(updates)} contact(s)...")

    summary = write_updates(service, updates)

    # Archive result
    with open(DONE_FILE, "w") as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "written": len(summary["written"]),
            "skipped": len(summary["skipped"]),
            "details": summary,
        }, f, indent=2)

    PENDING_FILE.unlink()  # delete the trigger file
    print(f"  ✓ Written: {len(summary['written'])}  |  Skipped: {len(summary['skipped'])}")
    if summary["skipped"]:
        for s in summary["skipped"]:
            print(f"    ↳ SKIPPED {s['email']}: {s['reason']}")


def main():
    print("=== Whitecarrot Sheet Watcher ===")
    print(f"Watching for: {PENDING_FILE.name}")
    print(f"Sheet: Apollo Contacts Found")
    print("Press Ctrl+C to stop.\n")

    # Eagerly connect once at startup to catch credential errors early
    print("Connecting to Google Sheets...", end=" ", flush=True)
    try:
        service = get_sheets_service()
        print("OK")
    except Exception as e:
        print(f"FAILED\n{e}")
        sys.exit(1)

    print("Watching...\n")
    while True:
        try:
            if PENDING_FILE.exists():
                ts = time.strftime("%H:%M:%S")
                print(f"[{ts}] Found {PENDING_FILE.name}")
                process_pending(service)
            time.sleep(POLL_INTERVAL_SEC)
        except KeyboardInterrupt:
            print("\nWatcher stopped.")
            break
        except Exception as e:
            print(f"  ERROR: {e}")
            time.sleep(10)  # back off on error


if __name__ == "__main__":
    main()

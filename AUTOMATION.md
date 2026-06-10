# Instantly API Automation — Design Doc

## What This Does
Replaces the manual "check Instantly → guess what to do" loop with a daily Claude analysis layer that reads campaign data, flags what's working and what's not, and surfaces copy variants for Pratik to approve before anything changes.

**Rule**: Claude reads and drafts. Pratik approves. Nothing goes live without a human click.

---

## System Architecture

```
Instantly API
    ↓  (daily pull)
Claude Analysis Layer
    ↓  (generates report + recommendations)
Daily Digest (Slack/Email to Pratik)
    ↓  (Pratik reviews and approves)
Manually applied changes in Instantly
```

---

## Daily Automation — What Runs Each Morning

### 1. Pull Campaign Stats
Via Instantly API → `/campaigns` and `/analytics/campaign`

Pulls for each active campaign:
- Emails sent
- Open rate
- Reply rate (total, positive, negative)
- Bounce rate
- Unsubscribe count

### 2. Score Each Campaign
Claude applies the kill/scale/test rule:
- **Kill** → reply rate <2% after 50+ sends
- **Scale** → reply rate >5% after 50+ sends  
- **Test More** → reply rate 2–5%
- **Insufficient data** → <50 sends, no action

### 3. Generate Copy Variants (if needed)
If a campaign is flagged Kill or needs iteration, Claude generates:
- 1–2 new subject line options (A/B test)
- OR a revised Email 1 body (change ONE variable only)
- Rationale: what hypothesis this tests

### 4. Deliver Daily Digest
Format: short, scannable, decision-ready

```
📊 WC Outbound — Daily Brief [Date]

CAMPAIGNS NEEDING ATTENTION:
Campaign 01 (25% Formula / Persona A)
  Sent: 67 | Reply rate: 1.4% → KILL CANDIDATE
  Recommendation: Pause. Test new subject line.
  Draft: "{{first_name}} — hiring pain at {{company_name}}"

Campaign 02 (One-Liner / Persona B)
  Sent: 43 | Reply rate: 6.2% → SCALE
  Recommendation: Increase send volume. Duplicate to KSA segment.

POSITIVE REPLIES THIS WEEK: 4
- [Company A] — interested, asked for demo
- [Company B] — asked about pricing

ACTION NEEDED:
[ ] Approve/reject campaign 01 subject line change
[ ] Confirm scale-up for campaign 02
```

---

## Weekly Automation — What Runs on Mondays

### Campaign Performance Review
- Compare week-over-week reply rates
- Flag which email in the sequence is dropping (E1 vs E2 vs E3 open/reply comparison)
- Identify best-performing persona/campaign combo

### Copy Iteration Log
- Record what was changed and when
- Track which changes improved performance (close loop on A/B tests)

---

## How to Build This (Step-by-Step)

### Step 1 — Get Instantly API key
- Instantly dashboard → Settings → API
- Store as environment variable (never hardcode)

### Step 2 — Build the data pull script (Python, runs daily)

```python
import requests
import json

INSTANTLY_API_KEY = "your_key_here"
BASE_URL = "https://api.instantly.ai/api/v1"

def get_campaign_analytics():
    headers = {"Authorization": f"Bearer {INSTANTLY_API_KEY}"}
    response = requests.get(f"{BASE_URL}/analytics/campaign/summary", 
                           params={"limit": 10},
                           headers=headers)
    return response.json()

def get_campaigns():
    headers = {"Authorization": f"Bearer {INSTANTLY_API_KEY}"}
    response = requests.get(f"{BASE_URL}/campaign/list", headers=headers)
    return response.json()
```

### Step 3 — Claude analysis prompt (runs after data pull)

Feed the stats JSON to Claude with this prompt:

```
You are the outbound campaign analyst for Whitecarrot.
ICP: HR leaders at UAE/KSA companies, 100-500 employees.
Kill threshold: <2% reply after 50 sends.
Scale threshold: >5% reply.

Here is today's campaign performance data:
[INSERT JSON DATA]

1. Score each campaign: Kill / Scale / Test More / Insufficient Data
2. For any Kill or declining campaign, suggest ONE copy change only (subject line OR email body, not both). Explain the hypothesis.
3. Flag any positive replies that need follow-up.
4. Output as a short brief under 200 words.

Voice rules: no buzzwords, no filler. Get to the point.
```

### Step 4 — Delivery
Options (pick one):
- **Email**: Python `smtplib` to pratik@whitecarrot.io
- **Slack**: Webhook to a #outbound-daily channel
- **File**: Write to `results/YYYY-MM-DD.md` — you read it each morning in this project

Recommended: write to results/ folder daily + Slack ping.

### Step 5 — Schedule
Run daily at 9am UAE time (UTC+4):
- Use GitHub Actions cron, Render cron job, or any scheduler with Python support
- Alternatively: Claude's built-in scheduled task (ask Claude to "run the outbound brief every morning at 9am")

---

## Human Review Gates (Non-Negotiable)

| Action | Human Required? |
|--------|----------------|
| Pull stats and generate brief | No — fully automated |
| Suggest a copy change | No — Claude generates, marks as [DRAFT] |
| Apply copy change to Instantly | **Yes — Pratik manually edits in Instantly UI** |
| Pause / kill a campaign | **Yes — Pratik clicks pause in Instantly** |
| Scale up send volume | **Yes — Pratik adjusts in Instantly settings** |
| Send a reply to an inbound lead | **Yes — Claude drafts, Pratik sends** |

---

## Instantly API Endpoints Needed

| What | Endpoint |
|------|----------|
| List campaigns | `GET /campaign/list` |
| Campaign analytics summary | `GET /analytics/campaign/summary` |
| Get campaign leads/contacts | `GET /lead/list?campaign_id=...` |
| Get replies | `GET /reply/list` |
| Get email stats per step | `GET /analytics/campaign/step` |

Full API docs: https://developer.instantly.ai

---

## Quick Start (Minimum Viable Version)

If you want to get this running in 30 minutes without building the full pipeline:

1. Every morning, open Instantly → Analytics
2. Copy the stats table as JSON (right-click → copy)
3. Paste into Claude here with: "Score these campaigns and tell me what to do"
4. Claude applies the kill/scale rules, suggests any changes
5. You apply changes manually

This manual version gives you 80% of the value immediately while the automation is being built.

---

## Files This System Writes To

| File | What Goes In It |
|------|----------------|
| `results/YYYY-MM-DD.md` | Daily brief — stats, scores, recommendations |
| `CAMPAIGN-LOG.md` | Updated weekly with kill/scale status per campaign |
| `02_copywriting/campaigns/*/email_v2.md` | New copy variants (drafts only — Pratik approves before use) |


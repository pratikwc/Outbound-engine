# WC Outbound — Instantly Engine

## Goal

Book 12–14 meetings/month with HR leaders and decision-makers at UAE/KSA companies via cold email on Instantly.ai.

Target: Open rate >22% | Reply rate >5% | Positive reply rate >60% of replies | Meetings 4–8/month

---

## How This Works — 3-Step Process

### Step 1 — Research (run first)

Read: `agents/research_agent.md`

Give the agent a batch of contacts (10–40 per session) from the lead list. It will:
- Collect signals from LinkedIn posts, job postings, and company website using Apify
- Classify each company into the correct industry bucket (using `knowledge/industry_map.md`)
- Determine persona (A/B/C) based on title
- Output one structured research brief per person

Output: Research briefs (one per person), ready for Step 2.

---

### Step 2 — Outreach (run after research)

Read: `agents/outreach_agent.md`

Feed the research briefs to the outreach agent. It will:
- Pick the right angle for each person (using `knowledge/angles.md` + the rubric)
- Select the matching social proof (using `knowledge/social_proof.md`)
- Write all 4 emails in the sequence
- Output a CSV with columns: email bodies, subject line, angle used, signal used, fallback flag

Output: One CSV per batch, saved to `outputs/`.

---

### Step 3 — Upload to Instantly

1. Open the CSV from `outputs/`
2. Filter by `angle_used` column
3. Upload each angle's rows to its corresponding Instantly campaign:
   - A1 → C01-All-ROI-NoATS
   - A2 → C02-TA-OneLiner-NoATS
   - A10 → C03-HR-Permission-NoATS
   - A13 → C04-All-Audit-NoATS
4. Review any rows where `fallback_flag = Yes` — decide to send or hold
5. Run spam check in Instantly before launching
6. Mridul reviews and approves all copy before any campaign goes live

---

## Performance Thresholds

| Status | Condition | Action |
|---|---|---|
| Kill | <2% reply after 50 sends | Pause. Change one variable. Log in `performance/iteration_log.md`. |
| Test More | 2–5% reply | Keep running. Try one variation. |
| Scale | >5% reply | Add more leads. Duplicate to next segment. |

**A/B test rule:** Change only ONE variable per test (subject line OR opening line OR CTA — never two at once). Log the change in `performance/iteration_log.md` before seeing results.

---

## Operating Rules

- **No autopilot.** Pratik drafts (with Claude), Mridul approves, Pratik sends. No exceptions.
- **Reply handling:** Review every reply in Instantly Unibox. Positive reply → send Calendly for 15-min discovery call.
- **Reply agent:** Not live yet. Handle replies manually until real objections are logged in `performance/iteration_log.md`.
- **Lead validation:** Run all lead batches through Instantly's email validator before uploading (target >85% pass rate).

---

## Lead Segments

| Segment | Companies | Status |
|---|---|---|
| No ATS | 328 | Active — run all campaigns here first |
| Has ATS (legacy) | 339 | Pending — start after No ATS has a winning angle |

Total pipeline (June 2026): 667 companies, 1,469 contacts across 3 persona CSVs.

---

## File Index

| File | What it is |
|---|---|
| `knowledge/whitecarrot.md` | ICP, offer, verified stats, personas, why people buy — single source of truth about WC |
| `knowledge/angles.md` | Approved email angles with selection rubric — outreach agent reads this |
| `knowledge/social_proof.md` | Client bank by industry with outcome lines |
| `knowledge/industry_map.md` | How to classify companies into industry buckets |
| `agents/research_agent.md` | Step 1: research instructions, data collection, brief output format |
| `agents/outreach_agent.md` | Step 2: angle selection, email writing rules, CSV output format |
| `performance/iteration_log.md` | Every A/B test logged before results come in |
| `performance/weekly_tracker.md` | Weekly metrics per campaign |
| `leads/apollo_export_log.md` | Lead batches: date, count, validation status |
| `outputs/` | Generated CSVs from outreach agent — ready for Instantly upload |
| `archive/` | Old files — kept for reference, not used by agents |

---

*Last updated: June 11, 2026.*

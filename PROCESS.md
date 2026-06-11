# Outbound Process — Whitecarrot x Instantly

## The Goal
Book 4–8 meetings per month with HR Directors, CHROs, and TA leaders at 100–1,000 employee companies in UAE and KSA.

---

## Three Personas (never mix in the same campaign)

| Persona | Titles | Pain to lead with |
|---|---|---|
| A — Decision Maker | CEO, Founder, Owner, CHRO, Chief People Officer | Paying agencies 8–15% per hire, no internal system |
| B — TA Champion | TA Manager, TA Director, Head of TA, Recruitment Manager | 18+ hours screening CVs per role manually |
| C — HR Champion | HR Manager, HR Director, VP People, Head of HR | No single pipeline view — candidates tracked in email/WhatsApp/spreadsheets |

---

## Two Lead Segments (test No ATS first)

| Segment | Size | Signal | Pitch angle |
|---|---|---|---|
| No ATS | 328 companies | No ATS detected in tech stack | "Replace the spreadsheet chaos" |
| Has ATS | 339 companies | Legacy ATS (Zoho, BambooHR, SAP) | "Replace the tool that doesn't actually work" |

Start all 4 campaigns on the No ATS segment. Once you find a winning angle, adapt it for Has ATS.

---

## Phase 1 — Lead Generation (Done)

1. Sales Navigator → filter by ICP (UAE/KSA, 100–1,000 employees, target industries)
2. Apify → scrape company profiles
3. Clay → enrich company data
4. GTM Sheet → master list of target companies
5. Apollo → filter personas per company (June 2026 list: 667 companies, 1,469 contacts)
6. **Validate emails** → Instantly lead validation tool (target >85% pass rate)
7. Export 3 CSVs — one per persona (A, B, C) — never mix

---

## Phase 2 — Campaign Setup (Current)

4 campaigns, each testing a different strategy from the Instantly masterclass:

| Campaign ID | Strategy | Persona | Segment |
|---|---|---|---|
| C01-All-ROI-NoATS | 25% Formula (ROI + case study + CTA) | All personas — adapt CTA per title | No ATS |
| C02-TA-OneLiner-NoATS | One-Liner (curiosity trigger) | B — TA Champion | No ATS |
| C03-HR-Permission-NoATS | Permission (ask before pitching) | C — HR Champion | No ATS |
| C04-All-Audit-NoATS | Free Audit (value-first) | A/B/C | No ATS |

Each campaign has a 4-email sequence:
- Email 1: Initial (Day 0)
- Email 2: Quick Bump (Day 2) — 1–2 lines only
- Email 3: Value add (Day 4) — new angle or case study
- Email 4: Breakup (Day 7) — human, not passive-aggressive

**Before launching any campaign:**
- [ ] Run spam check in Instantly's AI checker
- [ ] Mridul reviews and approves all 4 copies
- [ ] Upload correct persona CSV to each campaign (no mixing)

---

## Phase 3 — Live Running Loop (Daily)

**Every morning (15–30 min block):**
- Write 1 new campaign variation (change ONE variable — subject line, opening line, CTA, or angle)
- Log the change in `04_performance/iteration_log.md` before you see results

**Every afternoon (1pm check):**
- Review replies in Instantly
- Respond within 1–3 hours of seeing a positive reply
- Positive = interested / asking a question / wants more info → send Calendly link for 15-min discovery call

**Every week (Friday):**
- Review open rate, reply rate, positive reply rate per campaign
- Kill: under 2% reply after 50 sends
- Scale: above 5% reply → add more leads, duplicate to new segment
- Test more: 2–5% reply → keep running, try 1 variation

---

## Personalization Rules (from Mridul call, June 10)

- Pain point goes **inside the personalization section** — not a separate paragraph. Open with the prospect's world, weave in the pain, then pivot to offer.
- **Never reference a specific job role** the company is currently hiring for (e.g., "I saw you're hiring an engineer"). This signals you only help with one role. We help end-to-end, across all roles.
- Keep personalization to **1 sentence** — it opens the door, the offer closes it.

---

## Has ATS Segment — Copy Angle (when ready)

When prospect is using a legacy ATS (Zoho, BambooHR, SAP, Taleo):
- Identify their ATS from enrichment data
- Lead with: "We have customers who moved from [their ATS] and are now [outcome]"
- Don't attack their tool — frame as "companies who've made the switch"
- Longer sales cycle than No ATS — run this segment after No ATS is optimised

---

## Iteration Rules (from Instantly masterclass)
1. Change only ONE variable per A/B test
2. Log the reason before you see results — prevents post-hoc rationalisation
3. Run at least 50 sends before killing a campaign
4. When you find a winner, keep testing next to it — every winning angle eventually saturates
5. Target: winning combo found within 4 weeks and 4–10 campaign iterations

---

## Stats to track (Instantly dashboard)

| Metric | Target | Action if missed |
|---|---|---|
| Open rate | >22% | Fix subject line |
| Reply rate | >5% | Fix email body / offer |
| Positive reply rate | >60% of replies | Fix targeting or persona fit |
| Meeting booked | 4–8/month | Scale winning campaigns |

---

## Key stats for email copy (never make up numbers)
- 91 companies across UAE/KSA use Whitecarrot
- Time-to-hire: 42 days → 2 days
- CV screening: 18 hours → minutes per role
- Agencies charge 8–15% annual CTC per hire
- 78% of employers in the region still use agencies
- Beehive: switched from BambooHR, HMs now fill junior roles without assigning a recruiter
- Other clients: Bayzat, HalaTaxi (Careem), Sara Group, Alabbar Enterprises Group, EDF Energy, Bidfood

---

## Reply handling (manual — no autopilot yet)
- Review every reply before responding
- Pratik drafts reply → sends
- Positive reply → offer 15-min discovery call (Calendly)
- Objection → log in `05_reply_agent/objection_handling.md`, draft response manually
- Reply Agent only goes live after you understand the real objections coming in

---

## Files in this project

| File | Purpose |
|---|---|
| `01_icp_and_offer/avatar_cheat_sheet.md` | 3 personas — pain, angle, CTA, objections |
| `01_icp_and_offer/icp_definition.md` | Company segments, filters, buying triggers |
| `01_icp_and_offer/offer_summary.md` | What Whitecarrot does, what to say/not say |
| `01_icp_and_offer/case_studies.md` | Social proof for email copy |
| `02_copywriting/campaigns/C01-All-ROI-NoATS/` | Campaign 01 copy + sequence |
| `02_copywriting/campaigns/C02-TA-OneLiner-NoATS/` | Campaign 02 copy + sequence |
| `02_copywriting/campaigns/C03-HR-Permission-NoATS/` | Campaign 03 copy + sequence |
| `02_copywriting/campaigns/C04-All-Audit-NoATS/` | Campaign 04 copy + sequence |
| `02_copywriting/subject_line_bank.md` | All subject lines being tested |
| `02_copywriting/spam_word_log.md` | Words that hurt deliverability |
| `03_leads/apollo_export_log.md` | Every lead batch — date, count, validation status |
| `03_leads/lead_segments.md` | Segment definitions and filter details |
| `04_performance/iteration_log.md` | Daily log — what changed, why, result |
| `04_performance/weekly_tracker.md` | Weekly metrics per campaign |
| `04_performance/winning_campaigns.md` | Campaigns above 5% reply — archive of what worked |
| `05_reply_agent/objection_handling.md` | Real objections + how to respond |

# WC Outbound — Instantly Engine

## Project Goal
Book 4–8 meetings/month with HR leaders and decision-makers at UAE/KSA companies via cold email on Instantly.ai.

---

## ICP Definition

- **Titles**: HR Director, CHRO, VP People, Talent Acquisition Lead, Head of HR, CEO/Founder (entry point)
- **Company size**: 100–500 employees (sweet spot), 501–1,000 (high value)
- **Location**: UAE and KSA
- **Buying trigger**: Scaling headcount fast, no ATS or using spreadsheets/email to manage hiring

---

## Three Personas (never mix in the same campaign)

| Persona | Titles | Lead with |
|---|---|---|
| A — Decision Maker | CEO, Founder, Owner, CHRO, Chief People Officer | Agency cost pain / no internal system |
| B — TA Champion | TA Manager, TA Director, Head of TA, Recruitment Manager | 18+ hrs screening CVs manually per role |
| C — HR Champion | HR Manager, HR Director, VP People, Head of HR | No single pipeline view — chaos across email/WhatsApp/spreadsheets |

**CEO/Founder CTA**: Intro-ask ("Is there someone on your team who handles recruitment?")
**All other personas CTA**: Direct ask ("Worth 15 mins?")

---

## Campaign Map (current)

| Campaign ID | Strategy | Persona | Segment |
|---|---|---|---|
| C01-All-ROI-NoATS | 25% Formula (ROI + case study + CTA) | All personas — use title to adapt CTA | No ATS |
| C02-TA-OneLiner-NoATS | One-Liner (curiosity trigger) | B — TA Champion | No ATS |
| C03-HR-Permission-NoATS | Permission (ask before pitching) | C — HR Champion | No ATS |
| C04-All-Audit-NoATS | Free Audit (value-first) | A/B/C | No ATS |

**Naming convention**: `C[number]-[Persona]-[Strategy]-[Segment]` — use this in Instantly, iteration log, and weekly tracker so results are readable at a glance.

**C01 decision (June 11)**: All personas/titles go into C01 — not CEO only. Copy is adapted per persona already (CEO gets intro-ask, everyone else gets direct CTA). Do not split by title.

---

## Lead Segments

| Segment | Companies | Signal |
|---|---|---|
| No ATS | 328 | No ATS in tech stack |
| Has ATS (legacy) | 339 | Zoho, BambooHR, SAP, Taleo detected |

Run all campaigns on No ATS first. Adapt for Has ATS after finding winning angle.
**Total pipeline** (June 2026): 667 companies, 1,469 contacts across 3 persona CSVs.

---

## Whitecarrot Offer

AI recruitment software that centralises the hiring pipeline, saves recruiter time, integrates with BambooHR. Pays for itself in recruiter time savings in under 11 months.

**Verified stats — never make up numbers, use only these:**
- 91 companies in UAE/KSA use Whitecarrot
- Time-to-hire: 42 days → 2 days
- CV screening: 18 hours → minutes per role
- Agencies charge 8–15% annual CTC per hire
- 78% of employers in the region still use agencies
- Admin time: 42 hrs/week/recruiter → 6 hrs (Alabbar)

---

## Case Studies (match by industry — no mismatches)

| Client | Industry | One-liner |
|---|---|---|
| Alabbar Enterprises | Hospitality/Enterprise, Dubai | 8 recruiters → 3, 350 hires → 850/year |
| Beehive | FinTech/Financial Services, UAE | Moved from BambooHR — HMs now fill junior roles without a recruiter |
| RSM UAE | Professional Services | 30+ annual hires, lateral + multi-role, single pipeline |
| X-Architects | Architecture, UAE | 50+ active roles managed simultaneously |
| ELECTRA | Construction/Engineering | 50+ active roles, document + compliance in one platform |

---

## Brand Voice Rules

- Model tone on Mridul's writing: grounded, human, no filler, no guesses
- Emails under 15 seconds silent reading time — no exceptions
- No buzzwords: "skyrocket", "leverage", "synergy", "game-changer" — never
- No long intros. Line 1 gets to the point.
- Never start with "I". Never use "hope this finds you well" or "just reaching out"
- Write like a founder who did 10 minutes of research, not a sales rep

---

## Personalisation Rules (from Mridul call, June 10)

1. Pain goes **inside** the personalisation section — open with their world, weave in pain, then pivot to offer
2. **Never reference a specific job role** they're hiring for (signals you only help with one role)
3. Keep personalisation to **1 sentence** — it opens the door, the offer closes it

---

## Email Sequence (every campaign)

- Email 1: Initial (Day 0) — personalised
- Email 2: Quick Bump (Day 2) — 1–2 lines only
- Email 3: Value Add (Day 4) — new angle or case study, not a repeat of E1
- Email 4: Breakup (Day 7) — human, not passive-aggressive

---

## Performance Thresholds

| Status | Condition | Action |
|---|---|---|
| Kill | <2% reply after 50 sends | Pause. Change one variable. |
| Test More | 2–5% reply | Keep running. Try 1 variation. |
| Scale | >5% reply | Add more leads. Duplicate to next segment. |

**Targets**: Open rate >22%, Reply rate >5%, Positive reply rate >60% of replies, Meetings 4–8/month

---

## Iteration Rules

1. Change only ONE variable per A/B test (subject line OR opening line OR CTA — never two at once)
2. Log the change in `04_performance/iteration_log.md` **before** seeing results
3. Run at least 50 sends before killing
4. When you find a winner, keep testing next to it — every angle saturates eventually

---

## Before Launching Any Campaign

- [ ] Spam check run in Instantly AI checker
- [ ] Mridul reviewed and approved all 4 email copies
- [ ] Correct persona CSV uploaded (no mixing)
- [ ] All facts verified — no made-up signals or stats

---

## Contact Personalization Workflow (write-to-sheet)

When Pratik uploads a contacts file (CSV or similar) and asks for personalization:

1. Read the file — extract: First Name, Last Name, Title, Company, Email, City, Country, Has ATS, Seniority, Departments
2. For each contact generate:
   - `qualify_contact` — yes/no based on title (HR/People/Talent/Recruiter = yes; C-suite at ≤1000 emp = yes)
   - `persona_brief` — 1 sentence, who they are + why they fit, max 20 words
   - `research_signal` — the hook for outreach, max 15 words, grounded in ATS status / industry / size
   - `email_body` — full cold email: Subject line first, then body, under 80 words, sign off as Pratik, Whitecarrot
   - `fallback_flag` — "yes" if no specific signal found, "no" if personalized
3. Write the output to `pending_sheet_updates.json` in this project folder using this exact format:
   ```json
   [
     {
       "email": "contact@company.com",
       "qualify_contact": "yes",
       "persona_brief": "...",
       "research_signal": "...",
       "email_body": "Subject: ...\n\n...",
       "fallback_flag": "no"
     }
   ]
   ```
4. The `sheet_watcher.py` process (running locally) will detect the file and write directly to the Apollo Contacts Found sheet columns AB–AF, matched by email.
5. Confirm to Pratik how many contacts were written to the file and remind him the watcher will push it to the sheet within 3 seconds.

**Voice rules (non-negotiable)**: under 15 seconds reading time, no buzzwords, no "I" openers, no "hope this finds you well", sign off as Pratik from Whitecarrot.

---

## Operating Rules

- **No autopilot.** Claude drafts, Pratik sends — no exceptions
- **Reply handling**: Review every reply. Positive reply → send Calendly for 15-min discovery call
- **Reply agent**: Only goes live after real objections are understood and logged

---

## Key Files

| File | Purpose |
|---|---|
| `PROCESS.md` | Full operating SOP — read for detailed workflow |
| `01_icp_and_offer/case_studies.md` | Full case study details with quotes |
| `01_icp_and_offer/avatar_cheat_sheet.md` | Persona pain/angle/CTA/objections |
| `02_copywriting/campaigns/C01-All-ROI-NoATS/` | Campaign 01 copy + sequence |
| `02_copywriting/campaigns/C02-TA-OneLiner-NoATS/` | Campaign 02 copy + sequence |
| `02_copywriting/campaigns/C03-HR-Permission-NoATS/` | Campaign 03 copy + sequence |
| `02_copywriting/campaigns/C04-All-Audit-NoATS/` | Campaign 04 copy + sequence |
| `03_leads/research_agent_workflow.md` | Research runbook before writing any email |
| `03_leads/apollo_export_log.md` | Lead batch log — date, count, validation status |
| `04_performance/iteration_log.md` | Daily change log |
| `04_performance/weekly_tracker.md` | Weekly metrics per campaign |
| `05_reply_agent/objection_handling.md` | Real objections + how to respond |

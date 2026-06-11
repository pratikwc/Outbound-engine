# Campaign 01 — 25% Formula (Full Personalisation)

**Persona**: A — Decision Maker (CEO / Founder / CHRO)

**How this campaign works**: Email 1 is fully generated per person using Apollo + Apify research. Not a fixed template — the entire body is built from research and written by Claude. Emails 2–4 are fixed follow-ups.

**Research runbook**: `03_leads/research_agent_workflow.md` — follow this before writing any email.

**Instantly setup**: Full personalised body goes into `{{email_body}}` in the lead CSV. Email template just calls `{{email_body}}`. Subject line stays fixed.

---

## Subject Lines (A/B test one at a time)

- `hiring at {{company_name}}`
- `{{first_name}} — quick question`
- `filling roles at {{company_name}}`

---

## The Formula (Instantly 25% Formula — adapted for Whitecarrot)

The email body must hit all 8 elements, in order. The whole email stays under 120 words.

| # | Element | What it means for us |
|---|---|---|
| 1 | **Personalisation** | Something specific about this person or their company from research. Shows you did the work. |
| 2 | **Your Value Prop** | What Whitecarrot does — AI recruitment software, one platform, less manual work |
| 3 | **Target Niche** | Their specific industry + company stage + region (UAE/KSA) |
| 4 | **Their Goal** | What they're trying to achieve — hire faster, reduce agency cost, scale without adding HR headcount |
| 5 | **Their Value Prop** | What they gain specifically — less admin, faster decisions, no recruiter bottleneck |
| 6 | **Relevant Case Study** | A customer from their industry. Name + outcome. Match exactly. |
| 7 | **Cliffhanger Value Prop** | One sharp insight or contrast that leaves a question in their head |
| 8 | **CTA** | One ask. 15-min call. No options, no menu. |

---

## Research Brief — What to Collect Per Person

The research agent runs these lookups before writing the email. Output is structured inputs, not prose.

### From LinkedIn (person)
- Title and tenure at current company
- Any recent posts, articles, or comments they've made — especially about hiring, growth, team building
- If they're a new joiner (under 12 months) — this is a hot signal
- Career background — do they come from ops, HR, or finance? Shapes the angle.

### From LinkedIn (company)
- Industry (use LinkedIn taxonomy exactly)
- Headcount — is it growing? LinkedIn shows headcount trend
- Number of open roles visible on LinkedIn Jobs — not the specific roles, just the count
- Any expansion posts, announcements, or milestones shared on the company page

### From company website
- Does the company have a careers page? Is it branded or just a list of emails?
- Any press releases — awards, new offices, partnerships, government contracts
- About us / story — what's their growth narrative?

### UAE/KSA-specific signals to look for
- Great Place to Work, Forbes Middle East, or similar regional recognition
- New branch opening in a different emirate or KSA city
- Government contract win or regulatory approval
- Saudization/Emiratization mentions (especially in KSA — Nitaqat compliance is a real hiring pressure)
- Headcount at a known inflection point: 100, 250, 500 employees — where manual hiring breaks

---

## Personalisation Angles by Persona

### CEO / Founder
These people aren't in the hiring weeds. They care about the business. Personalise at the company level — not the person's bio.

- Company won an award or got recognised → "Saw {{company_name}} picked up [recognition] recently."
- Company is expanding → "Noticed {{company_name}} just opened in [city/market]."
- Company is growing fast and clearly scaling → "{{company_name}} has been moving fast — [public signal]."
- Ask: If they're clearly not the hiring decision-maker, use the intro ask: "Is there someone on your team handling recruitment who'd be the right person to speak with?"

### CHRO / Head of HR / VP People
These people own the hiring process. They feel the pain directly. Personalise at both person and company level.

- New to the role (< 12 months) → they're looking to make their mark fast, probably auditing tools
- Company is actively hiring at volume → [N]+ roles open, small HR team visible on LinkedIn = clear pain
- They've posted about HR challenges → reference what they said

### HR Director / HR Manager (at smaller companies)
These are often the only HR person or one of two. Drowning in admin. Personalise at company level — show you understand their size and stage.

- Company has 100–300 employees but only 1–2 people in HR on LinkedIn → call out the ratio
- High open role count relative to HR team size → you can see the pressure without naming specific roles

---

## Email 1 — Initial (Fully Personalised — built per person)

Subject: `hiring at {{company_name}}`

```
{{first_name}},

[1–2 sentences from research. Company or person-specific. Something that shows you looked.]

[1 sentence: what Whitecarrot does, tied to their niche and stage]

[Case study: customer from their exact industry + outcome in one sentence]

[1 sentence: what that could mean for {{company_name}} specifically]

Worth 15 mins?

Mridul
CEO - Whitecarrot.ai
```

**Tone rules:**
- UAE/KSA: lead with acknowledgment, not pain. People here respond to relationship signals first.
- Don't push. Ask.
- Sound like a founder who did 10 minutes of research, not a sales rep reading from a script.
- Never start with "I". Never use "hope this finds you well", "quick question", or "just reaching out".

---

## Example Emails (Research Agent Should Produce These)

### Example A — CEO, Hospitality company (Dubai, 200 employees, expanding)

Subject: `hiring at {{company_name}}`

```
{{first_name}},

Saw {{company_name}} just opened the second property in JBR — congrats on that.

Most hospitality operators at your stage are still running hiring across WhatsApp, email, and spreadsheets. No pipeline visibility, roles take 3–4 weeks to fill.

Alabbar Enterprises had the same setup — 8 recruiters struggling with 350 hires a year. After Whitecarrot, 3 recruiters now handle 850, and time-to-hire dropped from 44 days to 2.

Worth 15 mins to see if the same is doable at {{company_name}}?

Mridul
CEO - Whitecarrot.ai
```

---

### Example B — CHRO, Financial Services (UAE, new to role 8 months ago)

Subject: `hiring at {{company_name}}`

```
{{first_name}},

Looks like you've been building out the people function at {{company_name}} since last year — always a busy first 12 months.

A lot of financial services firms we speak to in UAE are still piecing together hiring across email, LinkedIn DMs, and spreadsheets — no single view of who's in the pipeline.

Beehive had that exact problem. They were on BambooHR but still doing everything manually. After Whitecarrot, hiring managers fill junior roles themselves without ever looping in a recruiter.

Happy to show you how it works in 15 mins.

Mridul
CEO - Whitecarrot.ai
```

---

### Example C — HR Director, Professional Services (KSA, 300 employees, 8+ open roles visible)

Subject: `hiring at {{company_name}}`

```
{{first_name}},

Noticed {{company_name}} has been actively hiring — looks like a busy period for your team.

Professional services firms at your scale in KSA often hit a point where the volume of roles outpaces what a small HR team can manage on spreadsheets — processes break, candidates go cold, agencies get called in.

RSM UAE runs 30+ hires a year through Whitecarrot — lateral hiring, multi-role batches, full pipeline in one place.

Worth a 15-minute call to see if it fits what you're dealing with at {{company_name}}?

Mridul
CEO - Whitecarrot.ai
```

---

### Example D — HR Director, construction (KSA, Saudization + high expat hire volume)

Subject: `hiring at {{company_name}}`

```
{{first_name}},

Saw {{company_name}} has been scaling headcount in KSA — looks like a busy period.

Construction companies here deal with a specific combination: high volume, high expat ratio, and Nitaqat quotas to maintain. Most manage the Saudization tracking on a separate spreadsheet while running the actual hiring on email. It adds up.

Whitecarrot supports the full process — document collection, nationality verification, and the compliance paperwork for every Saudi national hire — inside the same platform handling sourcing and screening. ELECTRA runs 50+ active roles through it.

Worth 15 mins to see how it fits {{company_name}}?

Mridul
CEO - Whitecarrot.ai
```

---

### Example E — CHRO, retail (KSA, document verification pain with high expat turnover)

Subject: `hiring at {{company_name}}`

```
{{first_name}},

Retail in KSA means constant hiring — and every new expat hire triggers the same document and visa cycle all over again.

Most HR teams manage that over WhatsApp and email alongside the actual recruitment process. It's slow, it's a compliance risk, and it burns recruiter time on admin that shouldn't require a person.

Whitecarrot handles document collection, verification, and visa coordination inside the hiring platform — same place the screening and interviews happen. No separate track.

Happy to show you how it works in 15 mins.

Mridul
CEO - Whitecarrot.ai
```

---

## Emails 2–4 — Follow-up Sequence (Fixed)

### Email 2 — Quick Bump (Day 2)

Subject: `re: hiring at {{company_name}}`

```
{{first_name}}, bumping this up — did this land?

Pratik
```

---

### Email 3 — Value (Day 4)

Subject: `re: hiring at {{company_name}}`

```
{{first_name}},

The pattern I see at companies your stage — when hiring picks up, the manual process breaks. Roles stay open 40+ days, agencies get called in, costs compound.

Alabbar Enterprises had 3 disconnected systems and 8 recruiters handling 350 hires a year. After Whitecarrot, admin went from 42 hours a week to 6, and 3 recruiters now handle 850.

Happy to show you how it works in 15 mins.

Pratik
```

---

### Email 4 — Breakup (Day 7)

Subject: `re: hiring at {{company_name}}`

```
{{first_name}}, last one from me.

If hiring isn't a priority right now, no worries — just say the word and I'll stop. If it is, happy to reconnect.

Pratik
```

---

## Checklist Before Uploading

- [ ] Each email reviewed by Pratik before upload — no batch-launching without a read
- [ ] Mridul approved the formula and examples
- [ ] Persona A CSV only — CEO/Founder/CHRO titles
- [ ] Industry-matched case study used in each email (no mismatches)
- [ ] No job-role references ("saw you're hiring a Marketing Manager" — never)
- [ ] Spam check run in Instantly AI checker
- [ ] All facts verified — no made-up signals

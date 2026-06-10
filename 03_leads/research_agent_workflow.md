# Research Agent Workflow — Campaign 01

How to go from a person's name + company to a fully personalised email using the 25% formula.

**Tools:** Apollo (MCP), Apify scraper (MCP)
**Output:** Full email body per person, ready to upload to Instantly as `{{email_body}}`

---

## Input required per person

- First Name	
- Last Name	
- Job title
- Company name
- Person Linkedin Url	
- Website	
- Company Linkedin Url

---

## Phase 1 — Data Collection (always run all available steps)

Run all steps you have inputs for. Don't decide on angle yet — just collect.

### Step 1 — Company data via Apollo
**Tool:** `apollo_organizations_enrich`

Collect:
- Industry (LinkedIn taxonomy)
- Headcount + growth trend
- Company description
- Location (UAE / KSA / city)
- Recent funding or notable growth events

### Step 2 — Job posting signals via Apollo
**Tool:** `apollo_organizations_job_postings`

Collect:
- Number of active job postings (count only — no specific titles)
- Broad function areas (Sales, Ops, Tech, HR — not specific roles)
- Whether they're hiring a Recruiter or TA role → flag this, it's a strong signal

### Step 3 — Person profile via Apify
**Actor:** `harvestapi/linkedin-profile-scraper`
**Input:** `profileUrls: [LinkedIn URL]`

Collect:
- Current title + tenure (how long in this role)
- Career background — HR, Ops, Finance? Shapes angle
- Flag if tenure < 12 months — new to role is a hot buying signal

### Step 4 — Person's recent posts via Apify ⭐ (critical for personalization)
**Actor:** `harvestapi/linkedin-profile-posts`
**Input:** `targetUrls: [LinkedIn URL]`, `maxPosts: 10`, `postedLimit: "3months"`

Collect:
- Any post about hiring, expansion, team growth, awards, new offices → this is the personalization hook
- Specific language they used ("we're expanding", "we're hiring across all studios") → mirror their framing
- Any industry recognition they shared or celebrated

### Step 5 — Company's recent posts via Apify ⭐ (critical for personalization)
**Actor:** `harvestapi/linkedin-company-posts`
**Input:** `targetUrls: [Company LinkedIn URL]`, `maxPosts: 10`, `postedLimit: "3months"`

Collect:
- Company expansion announcements ("growing our teams", new office, new city)
- Awards and recognition (Great Place to Work, D&AD, Forbes, industry awards)
- Hiring campaigns posted by the company itself
- Any signal that's specific, dated, and verifiable

> **Note:** Steps 4 and 5 are what separate a generic email from one that gets replied to. Run them even if you think you already have a signal — there's almost always something better in recent posts.

### Step 6 — Company website via Apify (supplementary)
**Actor:** Apify web scraper
**Input:** Company domain — target `/about`, `/careers`, `/news`, `/press`

Collect:
- Careers page: real branded page or just an email address?
- Awards or recognition not visible on LinkedIn

---

## Phase 2 — Research Brief (synthesize everything)

Once all data is collected, combine into a single structured brief:

```
Person:         [Name] | [Title] | [Tenure]
Company:        [Name] | [Industry] | [Headcount] | [Location: UAE/KSA + city]
Strongest signal: [The single most specific, verifiable thing found — 1 sentence]
Signal source:  [Apollo / LinkedIn / Website / Job postings]
Supporting signals: [Any secondary signals worth noting]
KSA flag:       [Yes/No — if KSA, note Saudization or document verification relevance]
New to role:    [Yes/No]
Job posting volume: [X active roles / hiring HR function: Yes/No]
```

---

## Phase 3 — Angle Selection (decide here, not before)

With the research brief in hand, pick the angle using this priority order:

**1. Strongest specific signal wins**
If you found something real and verifiable — company expansion, award, recent post, funding — lead with that. This is always better than any fallback.

**2. Match persona angle**
Use the persona guides in `email_v1.md`:
- CEO/Founder → company-level signal, not personal bio. Consider intro ask if hiring isn't directly their role.
- CHRO/VP People → person + company level. New to role = lead with that.
- HR Director/Manager → company level. HR team size vs. headcount ratio is the angle.

**3. Select case study**
Pull from `agent_context.md` Section 5. Match their exact industry mentioned on their Linkedin company profile. No cross-industry proof.

**4. KSA-specific add if relevant**
If KSA + construction/manufacturing/retail with high expat volume → add document verification / Saudization procedural support angle.

**5. If no strong signal found**
Fall back to the industry line from `personalisation_lines.md`. Flag the row as "fallback used" for Pratik's review.

---

## Phase 4 — Write the Email

Using the brief and selected angle, write the full email body following the 25% formula in `email_v1.md`.

Constraints:
- Under 120 words
- All 8 formula elements present but compressed
- Lead with acknowledgment, not pain (UAE/KSA relationship culture)
- Never reference a specific job title from their postings
- Never start with "I"
- Case study = one sentence, name + outcome

---

## Phase 5 — Output for Instantly

One CSV row per person:

| Column | Value |
|---|---|
| `first_name` | First name |
| `last_name` | Last name |
| `email` | Work email |
| `company_name` | Company name |
| `title` | Job title |
| `linkedin_url` | LinkedIn URL |
| `email_body` | Full personalised email body (body only — no subject, no greeting, no sign-off) |
| `research_signal` | One-line note: what signal was used and source |
| `fallback_flag` | Yes/No — was a fallback industry line used instead of a real signal? |

**Instantly email template:** calls `{{email_body}}`. Subject stays fixed: `hiring at {{company_name}}`

---

## Review before upload

- Read every `email_body` — no batch uploading without a read
- Any row with `fallback_flag = Yes` → decide whether to send or hold
- Verify case study matches industry — no mismatches
- Verify no specific job roles referenced
- Verify all facts — if a signal is uncertain, rewrite or skip

---

## Daily target

40 people → 40 research runs → 40 email bodies → 1 CSV → upload to Campaign 01

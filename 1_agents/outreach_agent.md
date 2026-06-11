# Outreach Agent

**Job:** Take a batch of research briefs, pick the right angle for each person, and write a full 4-email sequence. Output a CSV ready to upload to Instantly.

This agent reads:
- `0_0_knowledge/angles.md` — the angle definitions and selection rubric
- `0_0_knowledge/whitecarrot.md` — company context, offer, verified stats
- `0_0_knowledge/social_proof.md` — client bank by industry
- The research brief for each person (produced by the research agent)

---

## Step 1 — Angle Selection

For each person, read their research brief and pick one angle from `0_0_knowledge/angles.md`.

Use the selection rubric in angles.md (summarised below for quick reference):

| Situation | Angle |
|---|---|
| Strong signal + any persona | A1 — 25% Formula |
| CEO / Founder | A4 — Intro Ask (standalone or as CTA inside A1) |
| TA persona + average/weak signal | A2 — One-Liner |
| HR persona + senior title | A10 — Permission |
| No usable signal | A18 — Spontaneous |
| Category "ATS" feels stale | A16 — Ambiguous |
| Email 3 (Value Add) in any sequence | A13 — Free Audit |
| Specific observable pain (e.g. email-only careers page) | A17 — Upfront |

**Record which angle you picked and why in the output CSV** — this is how we track angle performance later.

---

## Step 2 — Select Social Proof

From `0_0_knowledge/social_proof.md`, pick the right client based on the industry bucket in the research brief.

Rules:
- Match the industry bucket exactly. No cross-industry proof.
- If the industry has no client match, use the strongest general stat: Alabbar (2.3× hires with 60% fewer recruiters) — only if it's not wildly out of context.
- One sentence max. Company name + outcome. Nothing else.
- ROI/time-to-hire numbers: only for Alabbar and Beehive. Volume stats for everyone else.

---

## Step 3 — Write the Email Sequence

Write all 4 emails per person. Follow the sequence structure below exactly.

---

### Email 1 — Initial (Day 0)

This is the angle email. Structure and word count depend on the angle chosen (see angles.md for each angle's template). For most angles:

**Personalization rules:**
- 1 sentence max — opens the door, doesn't close the deal
- Pain goes INSIDE the personalization line — weave it in, don't make it a separate section
- Must be specific and verifiable — never fabricate a signal
- Never reference a specific job title they're hiring for — it signals Whitecarrot only helps with one role
- Never start with "I"

**Offer framing:**
- State what WC does in their context — "manage all your hiring in one place" / "cut time-to-hire significantly"
- Follow immediately with industry-matched social proof

**CTA:**
- CEO/Founder: "Is there someone on your team who handles recruitment I should speak with?"
- All other personas: "Worth 15 minutes?"

**Hard limits:**
- Under 120 words (A1, A10, A13, A16, A17, A18)
- Under 50 words (A2, A4)
- No em-dashes (—) anywhere in the email
- No buzzwords: skyrocket, leverage, synergy, game-changer, cutting-edge, next-gen, innovative
- No "hope this finds you well", "just reaching out", "I wanted to"
- Plain text only — no bullet points, no bold, no formatting

---

### Email 2 — Quick Bump (Day 2)

1–2 lines only. No new pitch. Just a human nudge.

Options (pick one that fits):
- "Hey [First Name], just making sure this didn't get buried."
- "Hey [First Name], is there anyone else at [Company] I should be talking to about this?"
- "Still relevant?" (only if Email 1 mentioned a time-sensitive signal)

**Word limit:** Under 20 words.

---

### Email 3 — Value Add (Day 4)

Different angle from Email 1. Never repeat Email 1. Use one of:
- A13 (Free Audit) — most common choice: offer a 15-minute audit of their current hiring setup
- A8 (Loom) — if the account is high-value: "I put together a quick 2-minute breakdown of how [similar company] reduced their time-to-hire — want me to send it over?"
- New case study they haven't seen — industry-matched, different outcome from Email 1

**Word limit:** Under 80 words. No buzzwords. Same voice rules as Email 1.

---

### Email 4 — Breakup (Day 7)

Human close. Not passive-aggressive. Leave the door open.

Options:
- "At this point I'll assume hiring process improvements aren't a priority right now. No worries — feel free to reach out if that changes."
- "I'll leave it here. If you ever want to see how teams in [industry] are handling [their pain], happy to share. Take care."

**Word limit:** Under 30 words. No guilt-trip. No "I guess you're not interested."

---

## Email Writing Rules (apply to every email)

These rules apply to all 4 emails in every sequence, regardless of angle:

1. **No em-dashes (—).** Use a comma, a period, or rewrite the sentence.
2. **No buzzwords.** Never write: skyrocket, leverage, synergy, game-changer, cutting-edge, next-gen, innovative, transformative, revolutionary.
3. **Never start with "I".** Restructure the sentence.
4. **No openers:** "Hope this finds you well", "Just reaching out", "I wanted to", "I came across your profile"
5. **No specific job titles from their postings.** We cover all hiring, not one role.
6. **Pain goes inside personalization.** Open with their world, weave pain in, pivot to offer. Pain is not a separate paragraph.
7. **One social proof per email.** Company name + outcome. One sentence.
8. **Write like a human sending one email, not a template going to 500 people.**
9. **Read it aloud.** If it sounds like a bot, rewrite it.

---

## Output Format — CSV for Instantly

One row per person. This CSV is imported directly into Instantly.

| Column | Value |
|---|---|
| `first_name` | First name |
| `last_name` | Last name |
| `email` | Work email |
| `company_name` | Company name |
| `title` | Job title |
| `linkedin_url` | LinkedIn URL |
| `email_1` | Full Email 1 body (no subject, no greeting, no sign-off — just the body) |
| `email_2` | Full Email 2 body |
| `email_3` | Full Email 3 body |
| `email_4` | Full Email 4 body |
| `subject_line` | Subject for Email 1 — lowercase, personal, no spam words |
| `angle_used` | Angle code (A1, A2, A4, A10, A13, A16, A17, A18) |
| `signal_used` | 1-line note: what signal was used and source |
| `fallback_flag` | Yes/No — was a fallback used because no real signal was found? |
| `industry_bucket` | Industry bucket from research brief |

**Instantly template:** Email body calls `{{email_1}}`, `{{email_2}}` etc. Subject line is fixed per campaign.

---

## Before Outputting

Read every email body before adding it to the CSV:
- No row gets through without a human read
- Any `fallback_flag = Yes` row → flag for Pratik to decide whether to send or hold
- Verify case study matches industry bucket — no mismatches
- Verify no specific job titles are referenced
- Verify all facts are from the research brief — nothing fabricated

---

## How Angles Map to Instantly Campaigns

The outreach agent picks angles per person. When you export, filter by `angle_used` column and upload each angle's rows to the matching Instantly campaign:

| Angle | Instantly Campaign |
|---|---|
| A1 | C01-All-ROI-NoATS |
| A2 | C02-TA-OneLiner-NoATS |
| A10 | C03-HR-Permission-NoATS |
| A13 | C04-All-Audit-NoATS |
| A4 | Part of C01 (CEO variant) |
| A16, A17, A18 | Create new campaign when volume warrants it |

This is how we track which angles are generating replies at campaign level in Instantly analytics.

---

*Last updated: June 11, 2026.*

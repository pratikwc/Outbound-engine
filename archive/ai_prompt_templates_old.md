# AI Prompt Templates

## Which campaigns use which approach

| Campaign | Personalisation method |
|---|---|
| Campaign 01 (25% Formula) | Claude research agent — full email body generated per person. NOT Instantly AI prompts. |
| Campaign 02 (One-liner) | Instantly AI prompt — generates a single opening line from company description |
| Campaign 03 (Permission) | Instantly AI prompt — generates a single opening line from company description |
| Campaign 04 (Free Audit) | No personalisation needed — runs as-is |

The templates below are for Campaigns 02 and 03 only.

---

## How to use these in Instantly

1. Go to Campaign → Sequences → Email 1
2. Click the AI variable you want to populate (e.g. `{{personalisation_line}}`)
3. Paste the prompt below into the AI Prompt field
4. Map your CSV columns to the variables in the prompt
5. Generate and review a sample of 10–20 before launching

---

## Template 1 — Industry-matched opening line (recommended for Campaign 02 and 03)

Use this when your CSV has `{{industry}}` and `{{company_description}}` columns.

```
You are writing the opening line of a cold email to {{first_name}}, {{title}} at {{company_name}}.

Their industry: {{industry}}
Company description: {{company_description}}

We are Whitecarrot — AI recruitment software used by companies in UAE and KSA to run hiring in one place. Our customers include:

- Hospitality: Alabbar Enterprises (8 recruiters → 3 handling 850 hires/year), Madi International (405 hires across 163 roles)
- Food and Beverage: SARA Group (689 hires across 91 roles)
- Financial Services: Beehive (replaced BambooHR, hiring managers now self-serve junior roles)
- Real Estate: PRYPCO (77 roles, 694 candidates reviewed)
- Construction: ELECTRA (50 roles, 430 candidates reviewed)
- Accounting / Professional Services: RSM UAE (30 hires, 19 roles)
- Wellness and Fitness: Enhance Fitness (122 hires, 718 requisitions)
- Retail: Chemist Warehouse UAE, The Luxury Closet
- Wholesale: Daikan Hospitality Group (62 hires, 107 roles)
- IT Services: TPConnects (9 hires from 367 candidates)
- Software Development: Bayzat (26 hires, 948 candidates)

Write one sentence (max 15 words) that:
- References something true and specific about their hiring situation, growth, or company stage
- Sounds like it came from a person, not a tool
- Does NOT start with "I" or "I noticed"
- Does NOT mention a specific job title or job posting
- Does NOT use: leverage, synergy, game-changer, skyrocket, innovative, cutting-edge

Output only the sentence. No label, no quotes.
```

---

## Template 2 — Growth or expansion trigger

Use this when your CSV has a `{{growth_signal}}` column (e.g. "opened 2nd office in Riyadh", "raised Series B", "won government contract").

```
{{company_name}} recently: {{growth_signal}}

Write one short, human sentence (max 12 words) that acknowledges this and naturally connects to hiring that usually follows growth.

No exclamation marks. No buzzwords. Don't start with "I". Output only the sentence.
```

---

## Template 3 — No enrichment available (company name only)

Use this as a last resort when you only have company name and title, no description or signal.

```
You are writing the opening line of a cold email to {{first_name}}, {{title}} at {{company_name}} — a company based in UAE or KSA.

Write one sentence (max 15 words) that:
- Speaks to the hiring challenges common for a {{title}} at a company their size in the region
- Sounds human — like a colleague who knows the market, not a template
- Does NOT start with "I"
- Does NOT reference a specific job role or posting
- Does NOT use buzzwords

Output only the sentence. No label, no quotes.
```

---

## Quality check before launch

- Generate 20 sample lines and read them out loud
- Kill any that sound like a bot wrote them
- Kill any that make a claim you can't verify
- Flag any that reference specific job roles — those violate voice rules
- Log bad outputs below so the prompts can be improved

---

## Bad output log

| Date | Template | Bad output | Why bad |
|---|---|---|---|
| — | — | — | — |

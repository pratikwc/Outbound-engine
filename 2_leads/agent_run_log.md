# Agent Run Log

Track every research and outreach agent run — what went in, what came out.

---

## Log Format

Each entry covers one batch (research + outreach together). Fill in after each session.

```
### YYYY-MM-DD | Batch Name
**Source:** [GTM sheet tab + filter used, e.g. "Apollo Contacts Found — No ATS, rows 2–42"]
**Contacts:** [count]
**Personas:** A: [n] | B: [n] | C: [n]

**Research Agent**
- Apify signals collected: [LinkedIn posts / job postings / website — note any failures]
- Industries classified: [list buckets used, e.g. "Retail x8, BFSI x6, Logistics x4"]

**Outreach Agent**
- Output file: `3_outputs/[filename].csv`
- Angle distribution: A1: [n] | A2: [n] | A10: [n] | A13: [n]
- Fallback flag (Yes): [count] — [brief note on why]

**Notes:** [anything unusual — missing LinkedIn URLs, manual angle overrides, contacts skipped, etc.]
```

---

## Runs

### 2026-06-11 | Batch 00 — Test Run (Example)
**Source:** Apollo Contacts Found — No ATS, rows 2–12  
**Contacts:** 10  
**Personas:** A: 4 | B: 5 | C: 1

**Research Agent**
- Apify signals collected: LinkedIn posts ✓ | Job postings ✓ | Website ✓ (1 failed — Acme Corp, no website found)
- Industries classified: Retail x4, Logistics x3, BFSI x2, Other x1

**Outreach Agent**
- Output file: `3_outputs/2026-06-11_batch-00_test.csv`
- Angle distribution: A1: 5 | A2: 2 | A10: 2 | A13: 1
- Fallback flag (Yes): 2 — no strong signal found for 2 contacts, used generic ROI angle

**Notes:** Test run only — not uploaded to Instantly. Mridul to review copy before next batch goes live.

---

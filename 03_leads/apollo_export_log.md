# Apollo Export Log

One row per export batch. Log every pull — no exceptions.

| Date | List Name | Apollo List Link | Type | Filters Used | Raw Count | Post-Validation Count | Pass Rate | Uploaded To | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-06-05 | June 2026 - Target personas | [Link](https://app.apollo.io/#/lists/6a23cc0bd0732a0014a24633) | Contacts | UAE · 201–1,000 employees · Titles: HR Director, CHRO, VP People, Head of HR, TA Lead · Industries: Professional Services, Consumer Services, Entertainment, Retail, Healthcare · Excluded: Staffing & Recruiting, HR Services · Source companies: GTM Sheet - June list · Has verified email: Yes | 1,469 contacts · 667 companies | pending | pending | pending | 1,469 target persons · 667 unique target companies. Validate contacts in Instantly before uploading. Do not mix role types in same campaign sequence. |
| 2026-06-05 | GTM Sheet - June | [Link](https://app.apollo.io/#/lists/6a227d11cf4c5d001037b7d2) | Companies | UAE · 201–1,000 employees · Industries: Professional Services, Consumer Services, Entertainment, Retail, Healthcare · Excluded: all prior GCC lists (50–200 PS/TIM, 200+ GCC 1–6, 5k+ GCC) · HR dept headcount ≥ 1 | 95 | — | — | GTM Sheet [Master] Target Companies | Scraped via Apify, enriched in Clay (06-05-2026). Company source for June personas list above. |

## Filter Reference

### Standard filters for UAE/KSA ICP:
- Location: United Arab Emirates + Saudi Arabia
- Employee count: > 200 Employees
- Job title (decision-maker): HR Director, CHRO, VP People, Head of HR, Talent Acquisition Lead
- Industry: Professional Services, Financial Services, Hospitality, Consumer Services
- Has email: Yes (verified preferred)


## Research Batches (Apify — per-person signal scraping)

| Date | Batch | People Researched | Method | Signals Found | Emails Written | Stale Leads | Notes |
|---|---|---|---|---|---|---|---|
| 2026-06-11 | Batch 01 | 3 (Amina Gaco / STUDIOI, Shahenda Elhomosany / Qoyod, Reda Raad / TBWA\Raad) | Apify: `harvestapi/linkedin-profile-scraper`, `harvestapi/linkedin-company`, `harvestapi/linkedin-profile-posts`, `harvestapi/linkedin-company-posts` | STUDIOI June 9 hiring-across-all-studios post; TBWA\Raad D&AD Yellow Pencil MENA win June 1 | 2 of 3 | 1 — Shahenda left Qoyod Feb 2026, now at Deloitte Cairo | CSV: `instantly_upload_batch_01_v2.csv`. Both emails use specific verifiable recent signals. |

---

## Validation Tool
- Tool used: Apolllo, instantly
- Target pass rate: >85% before uploading

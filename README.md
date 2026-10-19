# Medical Knowledge Base

A curated, source-cited medical reference designed to be loaded as context by AI assistants, so their answers about health, diseases, and medicines are accurate, safe, and verifiable.

> **Disclaimer:** This repository is for informational and educational use. It is not a substitute for professional medical advice, diagnosis, or treatment. Doses and recommendations vary by country, formulary, and patient; always verify against current official labeling and local guidelines.

## How an assistant should use this repo

1. Read [`AGENTS.md`](AGENTS.md) first — it defines the answering rules.
2. Look up the relevant file below before answering clinical questions.
3. When this repo is silent or outdated, use the live sources in [`integrations/`](integrations/) (MCP servers, APIs) and cite them.

## Structure

| Path | Contents |
|------|----------|
| [`AGENTS.md`](AGENTS.md) | Core rules: answer protocol, safety, citation, uncertainty |
| [`guidelines/`](guidelines/) | Answering protocol, emergency red flags, communication rules |
| [`medicines/`](medicines/) | Drug monograph template, monographs, high-alert medications |
| [`interactions/`](interactions/) | Clinically major drug–drug interactions |
| [`special-populations/`](special-populations/) | Pregnancy/lactation, pediatrics, older adults, renal and hepatic impairment |
| [`clinical-reference/`](clinical-reference/) | Lab reference ranges, clinical formulas, unit conversions, unsafe abbreviations |
| [`integrations/`](integrations/) | Medical MCP servers, plugins, skills, and public APIs |
| [`skills/`](skills/) | Reusable agent skill for medical question answering |
| [`sources.md`](sources.md) | Trusted sources and evidence hierarchy |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Content standards, review rules, file template |

## Roadmap — what else to include

- [ ] **Diseases/conditions** — one file per condition: definition, diagnostic criteria, first-line treatment, red flags, guideline source (e.g. hypertension, T2DM, asthma, COPD, CAP, UTI, depression).
- [ ] **More monographs** — top 200 prescribed drugs, antibiotics, anticoagulants, insulin types, opioids.
- [ ] **Antimicrobial stewardship** — empiric therapy by infection site, local resistance caveats.
- [ ] **Vaccination schedules** — WHO/CDC/national schedules, catch-up rules, contraindications.
- [ ] **Toxicology & antidotes** — overdose management, antidote table, poison center contacts.
- [ ] **Allergy & cross-reactivity** — penicillin/cephalosporin, sulfonamide, contrast media.
- [ ] **Pharmacogenomics** — CPIC gene–drug pairs (CYP2C19–clopidogrel, HLA-B*57:01–abacavir, TPMT/NUDT15–thiopurines).
- [ ] **Brand ↔ generic mapping by country** — avoids confusing look-alike / sound-alike names.
- [ ] **Look-alike/sound-alike (LASA) drug list** — ISMP list.
- [ ] **Clinical scores** — CHA₂DS₂-VASc, HAS-BLED, Wells, CURB-65, qSOFA, GCS, NEWS2.
- [ ] **ICD-10 / SNOMED / LOINC / ATC quick maps** — coding references.
- [ ] **First aid & emergency** — CPR/BLS steps, choking, burns, bleeding.
- [ ] **Mental health** — crisis lines by country, safe-messaging guidelines.
- [ ] **Nutrition & supplements** — herb–drug interactions (St John's wort, grapefruit).
- [ ] **Regional context** — local guidelines/formularies (e.g. DRAP for Pakistan, NICE/BNF for UK, FDA for US).
- [ ] **Evaluation set** — Q&A test cases with expected answers to check assistant accuracy over time.
- [ ] **Changelog of guideline updates** — track when a recommendation changes.

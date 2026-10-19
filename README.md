# Medical Knowledge Base

A curated, source-cited medical reference designed to be loaded as context by AI assistants, so their answers about health, diseases, and medicines are accurate, safe, and verifiable.

> **Disclaimer:** This repository is for informational and educational use. It is not a substitute for professional medical advice, diagnosis, or treatment. Doses and recommendations vary by country, formulary, and patient; always verify against current official labeling and local guidelines.

## ChatGPT integration

For consistent use in ChatGPT, see **[CHATGPT.md](CHATGPT.md)** for setup and Project instructions, and **[KB-INDEX.md](KB-INDEX.md)** for a topic-to-file retrieval map. These files improve discoverability but do not cause automatic background synchronization or guarantee retrieval when ChatGPT lacks repository access.

## How an assistant should use this repo

1. Read [`AGENTS.md`](AGENTS.md) first — it defines the answering rules.
2. Look up the relevant file below before answering clinical questions.
3. When this repo is silent or outdated, use the live sources in [`integrations/`](docs/integrations/) (MCP servers, APIs) and cite them.

## Structure

| Path | Contents |
|------|----------|
| [`AGENTS.md`](AGENTS.md) | Core rules: answer protocol, safety, citation, uncertainty |
| [`guidelines/`](docs/guidelines/) | Answering protocol, emergency red flags, communication rules |
| [`medicines/`](docs/medicines/) | Drug monograph template, monographs, high-alert medications |
| [`interactions/`](docs/interactions/), [`allergy/`](docs/allergy/), [`pharmacogenomics/`](docs/pharmacogenomics/), [`toxicology/`](docs/toxicology/) | Interactions, drug allergy, gene–drug pairs, poisoning and antidotes |
| [`special-populations/`](docs/special-populations/) | Pregnancy/lactation, pediatrics, older adults, renal and hepatic impairment |
| [`clinical-reference/`](docs/clinical-reference/) | Lab reference ranges, clinical formulas, unit conversions, unsafe abbreviations |
| [`integrations/`](docs/integrations/) | Medical MCP servers, plugins, skills, and public APIs |
| [`mkdocs.yml`](mkdocs.yml), [`overrides/`](overrides/) | Website configuration and theme |
| [`skills/`](skills/) | Reusable agent skill for medical question answering |
| [`docs/conditions/`](docs/conditions/) | Condition pages (diagnosis, red flags, management) |
| [`evals/`](evals/) | Q&A test set to measure answer accuracy |
| [`sources.md`](docs/sources.md) | Trusted sources and evidence hierarchy |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Content standards, review rules, file template |

## Roadmap — what else to include

- [x] **Diseases/conditions** — one file per condition: definition, diagnostic criteria, first-line treatment, red flags, guideline source (e.g. hypertension, T2DM, asthma, COPD, CAP, UTI, depression).
- [ ] **More monographs** — 23 done; continue with top 200 prescribed drugs.
- [x] **Antimicrobial stewardship** — empiric therapy by infection site, local resistance caveats.
- [x] **Vaccination schedules** — WHO/CDC/national schedules, catch-up rules, contraindications.
- [x] **Toxicology & antidotes** — overdose management, antidote table, poison center contacts.
- [x] **Allergy & cross-reactivity** — penicillin/cephalosporin, sulfonamide, contrast media.
- [x] **Pharmacogenomics** — CPIC gene–drug pairs (CYP2C19–clopidogrel, HLA-B*57:01–abacavir, TPMT/NUDT15–thiopurines).
- [x] **Brand ↔ generic mapping by country** — avoids confusing look-alike / sound-alike names.
- [x] **Look-alike/sound-alike (LASA) drug list** — ISMP list.
- [x] **Clinical scores** — CHA₂DS₂-VASc, HAS-BLED, Wells, CURB-65, qSOFA, GCS, NEWS2.
- [x] **ICD-10 / SNOMED / LOINC / ATC quick maps** — coding references.
- [x] **First aid & emergency** — CPR/BLS steps, choking, burns, bleeding.
- [x] **Mental health** — crisis lines by country, safe-messaging guidelines.
- [x] **Nutrition & supplements** — herb–drug interactions (St John's wort, grapefruit).
- [x] **Regional context** — local guidelines/formularies (e.g. DRAP for Pakistan, NICE/BNF for UK, FDA for US).
- [x] **Evaluation set** — Q&A test cases with expected answers to check assistant accuracy over time.
- [x] **Changelog of guideline updates** — track when a recommendation changes.

## Web view

The `docs/` folder is published as a searchable website with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

```bash
pip install -r requirements-docs.txt
mkdocs serve        # preview at http://127.0.0.1:8000
mkdocs build        # static site in site/
```

Publishing: enable **Settings → Pages → Source: GitHub Actions**; [`.github/workflows/docs.yml`](.github/workflows/docs.yml) deploys on every push to `main`.

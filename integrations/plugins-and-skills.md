# Plugins & Skills

## Recommended setup
1. **Rules file** — load [`../AGENTS.md`](../AGENTS.md) as the project instruction file of your assistant.
2. **Skill** — copy [`../skills/medical-answering/`](../skills/medical-answering/) into your assistant's skills directory.
3. **Connectors** — enable PubMed, ClinicalTrials.gov, and ICD-10 at minimum ([mcp-servers.md](mcp-servers.md)).
4. **Custom MCP server** — add openFDA/RxNorm/DailyMed tools for drug labels.

## Available plugin bundles
| Plugin | Contents |
|--------|----------|
| Bio-research | PubMed, bioRxiv, ClinicalTrials.gov, ChEMBL, Open Targets, Consensus, BioRender, Synapse, Owkin, Wiley; skills for single-cell QC, nf-core pipelines, scvi-tools |
| Healthcare | CMS Coverage, ICD-10, NPI Registry, PubMed; skills for prior authorization and clinical documentation (check marketplace availability) |

## Skill ideas to build
| Skill | Purpose |
|-------|---------|
| `medical-answering` | Enforces the answer protocol (included) |
| `drug-lookup` | Fetch label from openFDA/DailyMed and summarize dose, contraindications, interactions |
| `dose-check` | Validate a dose against weight, age, renal function, and max daily dose |
| `interaction-check` | Check a medication list against [`../interactions/`](../interactions/) and a live source |
| `lab-interpreter` | Interpret a lab report using the patient's lab ranges |
| `guideline-summary` | Summarize a named guideline with year and recommendation strength |
| `patient-leaflet` | Turn clinical content into plain-language patient information |

# Medical MCP Servers & Connectors

MCP (Model Context Protocol) servers give an assistant live access to authoritative data, so answers are not limited to training memory. Availability changes — confirm in your assistant's connector directory before relying on one.

## Hosted connectors (Healthcare & Life Sciences)
| Connector | Data | Use for |
|-----------|------|---------|
| PubMed | Biomedical literature (NLM) | Evidence lookup, citations |
| ClinicalTrials.gov | Registered clinical trials | Trial status, eligibility, results |
| bioRxiv / medRxiv | Preprints | Very recent research (not peer-reviewed — flag it) |
| ChEMBL | Bioactive molecules, drug targets | Pharmacology, mechanism |
| Open Targets | Target–disease associations | Drug discovery, genetics |
| Consensus | Research-paper answer engine | Quick evidence summaries |
| CMS Coverage Database | US Medicare coverage determinations | Coverage/prior-auth questions |
| ICD-10 | Diagnosis/procedure codes | Coding |
| NPI Registry | US provider identifiers | Provider verification |

Bio-research connectors (BioRender, Synapse, Owkin, Wiley, Benchling, 10x Genomics) are research-focused rather than clinical.

## Self-hosted / custom servers
Build a small MCP server over free public APIs ([public-apis.md](public-apis.md)). Suggested tools:

| Tool | Backing API |
|------|-------------|
| `drug_label(name)` | openFDA `/drug/label` or DailyMed SPL |
| `normalize_drug(name)` | RxNorm `rxcui` / `approximateTerm` |
| `adverse_events(drug)` | openFDA `/drug/event` |
| `drug_recalls(drug)` | openFDA `/drug/enforcement` |
| `search_trials(condition)` | ClinicalTrials.gov API v2 |
| `search_pubmed(query)` | NCBI E-utilities |
| `icd10_lookup(term)` | NLM Clinical Tables |
| `patient_info(icd10)` | MedlinePlus Connect |

Rules for a custom server:
- Return the **source URL and retrieval date** with every result.
- Never return PHI to logs; keep API keys in environment variables.
- Prefer read-only tools.

## EHR integration
For clinical systems, use **HL7 FHIR R4** APIs (with SMART on FHIR authorization). Requires institutional approval, HIPAA/GDPR compliance, and a business associate agreement where applicable.

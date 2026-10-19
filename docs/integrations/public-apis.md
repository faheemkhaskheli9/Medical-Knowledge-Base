# Free Public Medical APIs

| API | Base URL | Example |
|-----|----------|---------|
| openFDA (labels, adverse events, recalls) | `https://api.fda.gov` | `/drug/label.json?search=openfda.generic_name:"metformin"&limit=1` |
| DailyMed (FDA SPL labels) | `https://dailymed.nlm.nih.gov/dailymed/services/v2` | `/spls.json?drug_name=metformin` |
| RxNorm / RxNav | `https://rxnav.nlm.nih.gov/REST` | `/rxcui.json?name=metformin` |
| ClinicalTrials.gov v2 | `https://clinicaltrials.gov/api/v2` | `/studies?query.cond=type+2+diabetes` |
| PubMed E-utilities | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils` | `/esearch.fcgi?db=pubmed&term=metformin+lactic+acidosis` |
| NLM Clinical Tables (ICD-10-CM, LOINC, etc.) | `https://clinicaltables.nlm.nih.gov/api` | `/icd10cm/v3/search?terms=diabetes` |
| MedlinePlus Connect | `https://connect.medlineplus.gov/service` | `?mainSearchCriteria.v.cs=2.16.840.1.113883.6.90&mainSearchCriteria.v.c=E11.9&knowledgeResponseType=application/json` |
| NPPES NPI Registry | `https://npiregistry.cms.hhs.gov/api` | `/?version=2.1&last_name=smith&state=NY` |
| WHO Global Health Observatory | `https://ghoapi.azureedge.net/api` | `/Indicator` |

Notes:
- The RxNav **drug–drug interaction API was discontinued in January 2024**; use a licensed interaction source (DrugBank, Lexicomp, Micromedex) or label sections.
- NCBI E-utilities: include an API key for > 3 requests/second.
- openFDA data (FAERS) shows reported events, **not** proven causation.

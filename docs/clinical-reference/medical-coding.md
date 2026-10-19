---
title: Medical Coding Systems
last_reviewed: 2026-10-19
sources:
  - WHO ICD-10 and ICD-11
  - CMS ICD-10-CM
  - SNOMED International
  - Regenstrief Institute (LOINC)
  - NLM RxNorm; WHO ATC/DDD
region: global
---

# Medical Coding Systems

| System | Codes | Owner | Access |
|--------|-------|-------|--------|
| ICD-10 | Diagnoses (WHO international) | WHO | Free |
| ICD-10-CM / ICD-10-PCS | US diagnoses / inpatient procedures | CDC / CMS | Free |
| ICD-11 | Diagnoses — WHO standard since January 2022 | WHO | Free (icd.who.int) |
| SNOMED CT | Clinical terms for EHRs | SNOMED International | Licence (free in member countries) |
| LOINC | Lab tests and observations | Regenstrief | Free |
| RxNorm | US normalized drug names | NLM | Free |
| ATC | Drug classification by organ/system | WHO | Free |
| NDC | US drug product identifiers | FDA | Free |
| CPT | US procedures | AMA | Licensed |

Lookup APIs: [Public APIs](../integrations/public-apis.md).

## Common ICD-10 codes
| Code | Condition |
|------|-----------|
| I10 | Essential (primary) hypertension |
| E11 | Type 2 diabetes mellitus |
| E10 | Type 1 diabetes mellitus |
| I48 | Atrial fibrillation and flutter |
| J45 | Asthma |
| J44 | Other chronic obstructive pulmonary disease |
| J18.9 | Pneumonia, unspecified organism |
| N39.0 | Urinary tract infection, site not specified |
| F32 | Depressive episode |
| A01.0 | Typhoid fever |
| A90 / A91 | Dengue fever / severe dengue (ICD-10 WHO) |
| U07.1 | COVID-19, virus identified |

## Common LOINC codes
| Code | Test |
|------|------|
| 4548-4 | Hemoglobin A1c / hemoglobin total in blood |
| 2345-7 | Glucose, serum/plasma |
| 2160-0 | Creatinine, serum/plasma |
| 2951-2 | Sodium, serum/plasma |
| 2823-3 | Potassium, serum/plasma |

## Common SNOMED CT concepts
| Concept ID | Term |
|------------|------|
| 44054006 | Diabetes mellitus type 2 |
| 38341003 | Hypertensive disorder |

## ATC structure (example: metformin A10BA02)
A = Alimentary tract and metabolism · A10 = Drugs used in diabetes · A10B = Blood glucose lowering drugs, excl. insulins · A10BA = Biguanides · A10BA02 = Metformin

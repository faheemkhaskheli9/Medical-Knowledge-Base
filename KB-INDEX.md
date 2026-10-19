# Knowledge Base Retrieval Index

**Repository:** https://github.com/faheemkhaskheli9/Medical-Knowledge-Base

This is a routing index, not a clinical guideline. Read [AGENTS.md](AGENTS.md) first. Fetch the relevant files before drawing conclusions; filenames and this index alone do not establish medical facts.

| Question or task | Files to retrieve |
|---|---|
| All medical questions, clinical answer rules, source quality | [AGENTS.md](AGENTS.md), [docs/sources.md](docs/sources.md), [docs/guidelines/answering-protocol.md](docs/guidelines/answering-protocol.md) |
| Symptoms, triage, urgent warning signs | [docs/guidelines/red-flags.md](docs/guidelines/red-flags.md) |
| Medication safety and high-risk drug classes | [docs/medicines/high-alert-medications.md](docs/medicines/high-alert-medications.md) |
| Major drug interactions | [docs/interactions/major-interactions.md](docs/interactions/major-interactions.md) |
| Paracetamol/acetaminophen | [docs/medicines/monographs/paracetamol.md](docs/medicines/monographs/paracetamol.md) |
| Ibuprofen | [docs/medicines/monographs/ibuprofen.md](docs/medicines/monographs/ibuprofen.md) |
| Metformin | [docs/medicines/monographs/metformin.md](docs/medicines/monographs/metformin.md) |
| Warfarin | [docs/medicines/monographs/warfarin.md](docs/medicines/monographs/warfarin.md) |
| Amoxicillin, co-amoxiclav | [docs/medicines/monographs/amoxicillin.md](docs/medicines/monographs/amoxicillin.md) |
| Atorvastatin, statins | [docs/medicines/monographs/atorvastatin.md](docs/medicines/monographs/atorvastatin.md) |
| Amlodipine | [docs/medicines/monographs/amlodipine.md](docs/medicines/monographs/amlodipine.md) |
| Lisinopril, ramipril, enalapril (ACE inhibitors) | [docs/medicines/monographs/ace-inhibitors.md](docs/medicines/monographs/ace-inhibitors.md) |
| Omeprazole, PPIs | [docs/medicines/monographs/omeprazole.md](docs/medicines/monographs/omeprazole.md) |
| Salbutamol/albuterol, asthma relievers | [docs/medicines/monographs/salbutamol.md](docs/medicines/monographs/salbutamol.md) |
| Apixaban, DOACs | [docs/medicines/monographs/apixaban.md](docs/medicines/monographs/apixaban.md) |
| Sertraline, SSRIs | [docs/medicines/monographs/sertraline.md](docs/medicines/monographs/sertraline.md) |
| Levothyroxine | [docs/medicines/monographs/levothyroxine.md](docs/medicines/monographs/levothyroxine.md) |
| Insulin types | [docs/medicines/monographs/insulin.md](docs/medicines/monographs/insulin.md) |
| New drug content format | [docs/medicines/_template.md](docs/medicines/_template.md), [CONTRIBUTING.md](CONTRIBUTING.md) |
| Pregnancy and breastfeeding | [docs/special-populations/pregnancy-lactation.md](docs/special-populations/pregnancy-lactation.md) |
| Children and adolescents | [docs/special-populations/pediatrics.md](docs/special-populations/pediatrics.md) |
| Older adults | [docs/special-populations/older-adults.md](docs/special-populations/older-adults.md) |
| Kidney/liver disease and dosing considerations | [docs/special-populations/renal-hepatic.md](docs/special-populations/renal-hepatic.md) |
| Lab measurements and typical reference intervals | [docs/clinical-reference/lab-reference-ranges.md](docs/clinical-reference/lab-reference-ranges.md) |
| Hypertension | [docs/conditions/hypertension.md](docs/conditions/hypertension.md) |
| Type 2 diabetes, hypoglycemia, sick-day rules | [docs/conditions/type-2-diabetes.md](docs/conditions/type-2-diabetes.md) |
| Confusable drug names | [docs/medicines/look-alike-sound-alike.md](docs/medicines/look-alike-sound-alike.md) |
| Drug allergy, penicillin/cephalosporin, sulfa, contrast | [docs/allergy/cross-reactivity.md](docs/allergy/cross-reactivity.md) |
| Genetic testing before prescribing | [docs/pharmacogenomics/gene-drug-pairs.md](docs/pharmacogenomics/gene-drug-pairs.md) |
| Poisoning, overdose, antidotes | [docs/toxicology/antidotes.md](docs/toxicology/antidotes.md) |
| Risk scores (CHA₂DS₂-VASc, HAS-BLED, CURB-65, qSOFA, GCS, Wells) | [docs/clinical-reference/clinical-scores.md](docs/clinical-reference/clinical-scores.md) |
| Antibiotic choice, resistance, AWaRe | [docs/infections/antimicrobial-stewardship.md](docs/infections/antimicrobial-stewardship.md) |
| Vaccines and schedules | [docs/vaccination/vaccination.md](docs/vaccination/vaccination.md) |
| Brand vs generic, INN vs US names | [docs/medicines/drug-names-by-region.md](docs/medicines/drug-names-by-region.md) |
| Herbal/supplement/food interactions | [docs/medicines/herb-drug-interactions.md](docs/medicines/herb-drug-interactions.md) |
| ICD-10/ICD-11, SNOMED, LOINC, ATC | [docs/clinical-reference/medical-coding.md](docs/clinical-reference/medical-coding.md) |
| First aid and CPR | [docs/first-aid/first-aid.md](docs/first-aid/first-aid.md) |
| Suicide/self-harm and crisis lines | [docs/mental-health/crisis-support.md](docs/mental-health/crisis-support.md) |
| Pakistan-specific context | [docs/regional/pakistan.md](docs/regional/pakistan.md) |
| Recent guideline changes | [docs/guideline-changes.md](docs/guideline-changes.md) |
| Medical calculations | [docs/clinical-reference/formulas.md](docs/clinical-reference/formulas.md) |
| Medication orders and unsafe shorthand | [docs/clinical-reference/unsafe-abbreviations.md](docs/clinical-reference/unsafe-abbreviations.md) |
| Current drug labels, research and clinical trials | [docs/integrations/public-apis.md](docs/integrations/public-apis.md), [docs/integrations/mcp-servers.md](docs/integrations/mcp-servers.md) |
| Agent skills and connector options | [skills/medical-answering/SKILL.md](skills/medical-answering/SKILL.md), [docs/integrations/plugins-and-skills.md](docs/integrations/plugins-and-skills.md) |
| Connecting this repository to ChatGPT | [CHATGPT.md](CHATGPT.md) |

## Retrieval procedure

1. Read `AGENTS.md` and the matching files above **in the current session** using the GitHub connector, or fetch the public GitHub content.
2. For symptom-related questions, also consult `docs/guidelines/red-flags.md`; for medication questions, consider the interactions and special-population files.
3. Treat this repository as a curated *reference*, not as proof that a recommendation is current. Check current official drug labeling and relevant local/national guidelines when accuracy or timeliness matters.
4. Cite the actual retrieved repository file(s) and current authoritative sources. Distinguish clinical facts from preliminary notes.
5. If a requested topic is not covered or the repository cannot be retrieved, say so. Do not claim this repository was consulted when it was not.

**Coverage note:** This repository currently has 14 drug monographs and two condition pages; other pages are summaries. Absence of a medication or disease is not evidence of safety or lack of guidance. Do not infer exhaustive coverage.

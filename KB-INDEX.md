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
| New drug content format | [docs/medicines/_template.md](docs/medicines/_template.md), [CONTRIBUTING.md](CONTRIBUTING.md) |
| Pregnancy and breastfeeding | [docs/special-populations/pregnancy-lactation.md](docs/special-populations/pregnancy-lactation.md) |
| Children and adolescents | [docs/special-populations/pediatrics.md](docs/special-populations/pediatrics.md) |
| Older adults | [docs/special-populations/older-adults.md](docs/special-populations/older-adults.md) |
| Kidney/liver disease and dosing considerations | [docs/special-populations/renal-hepatic.md](docs/special-populations/renal-hepatic.md) |
| Lab measurements and typical reference intervals | [docs/clinical-reference/lab-reference-ranges.md](docs/clinical-reference/lab-reference-ranges.md) |
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

**Coverage note:** This repository currently has four individual drug monographs. Absence of a medication or disease is not evidence of safety or lack of guidance. Do not infer exhaustive coverage.

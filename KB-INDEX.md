# Knowledge Base Retrieval Index

**Repository:** https://github.com/faheemkhaskheli9/Medical-Knowledge-Base

This is a routing index, not a clinical guideline. Read [AGENTS.md](AGENTS.md) first. Fetch the relevant files before drawing conclusions; filenames and this index alone do not establish medical facts.

| Question or task | Files to retrieve |
|---|---|
| All medical questions, clinical answer rules, source quality | [AGENTS.md](AGENTS.md), [sources.md](sources.md), [guidelines/answering-protocol.md](guidelines/answering-protocol.md) |
| Symptoms, triage, urgent warning signs | [guidelines/red-flags.md](guidelines/red-flags.md) |
| Medication safety and high-risk drug classes | [medicines/high-alert-medications.md](medicines/high-alert-medications.md) |
| Major drug interactions | [interactions/major-interactions.md](interactions/major-interactions.md) |
| Paracetamol/acetaminophen | [medicines/monographs/paracetamol.md](medicines/monographs/paracetamol.md) |
| Ibuprofen | [medicines/monographs/ibuprofen.md](medicines/monographs/ibuprofen.md) |
| Metformin | [medicines/monographs/metformin.md](medicines/monographs/metformin.md) |
| Warfarin | [medicines/monographs/warfarin.md](medicines/monographs/warfarin.md) |
| New drug content format | [medicines/_template.md](medicines/_template.md), [CONTRIBUTING.md](CONTRIBUTING.md) |
| Pregnancy and breastfeeding | [special-populations/pregnancy-lactation.md](special-populations/pregnancy-lactation.md) |
| Children and adolescents | [special-populations/pediatrics.md](special-populations/pediatrics.md) |
| Older adults | [special-populations/older-adults.md](special-populations/older-adults.md) |
| Kidney/liver disease and dosing considerations | [special-populations/renal-hepatic.md](special-populations/renal-hepatic.md) |
| Lab measurements and typical reference intervals | [clinical-reference/lab-reference-ranges.md](clinical-reference/lab-reference-ranges.md) |
| Medical calculations | [clinical-reference/formulas.md](clinical-reference/formulas.md) |
| Medication orders and unsafe shorthand | [clinical-reference/unsafe-abbreviations.md](clinical-reference/unsafe-abbreviations.md) |
| Current drug labels, research and clinical trials | [integrations/public-apis.md](integrations/public-apis.md), [integrations/mcp-servers.md](integrations/mcp-servers.md) |
| Agent skills and connector options | [skills/medical-answering/SKILL.md](skills/medical-answering/SKILL.md), [integrations/plugins-and-skills.md](integrations/plugins-and-skills.md) |
| Connecting this repository to ChatGPT | [CHATGPT.md](CHATGPT.md) |

## Retrieval procedure

1. Read `AGENTS.md` and the matching files above **in the current session** using the GitHub connector, or fetch the public GitHub content.
2. For symptom-related questions, also consult `guidelines/red-flags.md`; for medication questions, consider the interactions and special-population files.
3. Treat this repository as a curated *reference*, not as proof that a recommendation is current. Check current official drug labeling and relevant local/national guidelines when accuracy or timeliness matters.
4. Cite the actual retrieved repository file(s) and current authoritative sources. Distinguish clinical facts from preliminary notes.
5. If a requested topic is not covered or the repository cannot be retrieved, say so. Do not claim this repository was consulted when it was not.

**Coverage note:** This repository currently has four individual drug monographs. Absence of a medication or disease is not evidence of safety or lack of guidance. Do not infer exhaustive coverage.

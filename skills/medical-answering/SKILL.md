---
name: medical-answering
description: Use for any question about symptoms, diseases, medicines, doses, drug interactions, lab results, or medical calculations. Enforces safety screening, dose verification, and source citation using this knowledge base.
---

# Medical Answering

1. **Screen for emergencies** — read `guidelines/red-flags.md`. If a red flag applies, tell the user to seek emergency care first.
2. **Identify audience** — patient or clinician; adjust language.
3. **Collect context** — age, weight, pregnancy/lactation, kidney/liver function, allergies, current medicines. Ask if missing and relevant to dosing.
4. **Look up** — check `medicines/`, `interactions/`, `special-populations/`, `clinical-reference/`. If not covered, use connected MCP tools (PubMed, ClinicalTrials.gov, drug-label sources).
5. **Verify** — doses with units, route, frequency, and maximum; interactions; contraindications; region-specific differences.
6. **Answer** — direct answer → details → warnings → when to seek care → sources.
7. **State uncertainty** — never invent doses, studies, or citations.

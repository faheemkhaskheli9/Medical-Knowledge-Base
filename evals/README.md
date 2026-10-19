# Evaluation Set

Questions with expected key points, used to check that an assistant using this knowledge base answers accurately and safely.

## How to run
1. Ask the assistant each `question` from [medical-qa.yaml](medical-qa.yaml) in a fresh session with this repository loaded.
2. Mark **pass** only if every `must_include` point is present and no `must_not` item appears.
3. Track pass rate over time; add a case whenever a mistake is found.

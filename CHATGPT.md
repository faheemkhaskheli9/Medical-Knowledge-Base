# Using the Medical Knowledge Base with ChatGPT

Repository: https://github.com/faheemkhaskheli9/Medical-Knowledge-Base

## What works

- The public repository can be read when ChatGPT has web or GitHub access.
- The GitHub connection can retrieve current repository files on demand.
- A ChatGPT **Project** with the instructions below is the best way to apply the workflow consistently within that Project.
- ChatGPT memory or custom instructions can preserve your *preference* to consult the repository across chats.

**What is not guaranteed:** Repository files do not automatically become ChatGPT's system instructions. Memory is not a live sync or search index. ChatGPT cannot promise to fetch this repository in every conversation, especially when browsing/connectors are unavailable, disabled, or the conversation is outside the configured Project.

## Shared knowledge bases

For interdisciplinary work, consult the [central ChatGPT knowledge-base router](https://github.com/faheemkhaskheli9/AI-Knowledge-Base/blob/main/CHATGPT-KB-ROUTER.md). It links the owner's [AI](https://github.com/faheemkhaskheli9/AI-Knowledge-Base), [software engineering](https://github.com/faheemkhaskheli9/Software-Engineering-KnowledgeBase), and [cybersecurity](https://github.com/faheemkhaskheli9/Cyber-Security-Knowledge-Base) reference repositories, plus an optional private Personal KB. Healthcare AI design may require all four public KBs, but this medical KB and **current official clinical evidence** govern clinical safety. Only consult private records when explicitly relevant and authorized. The shared router contains general-purpose ChatGPT Project instructions; the instructions below remain the medical-specific option.

## Recommended setup

1. In ChatGPT, open **Settings → Plugins**, and connect or enable **GitHub** with access to this repository. The repository is currently public, so web retrieval may also work.
2. Create a ChatGPT **Project** for your medical/healthcare questions and add the project instructions below. Use that Project for requests that should consistently consult the knowledge base.
3. Keep the GitHub repository URL in your personal custom instructions or memory as a preference for relevant medical tasks, while recognizing that neither forces retrieval.
4. When the repository changes, ask ChatGPT to fetch the files again; do not rely on an older conversation's cached excerpts.

## Copy into ChatGPT Project instructions

```text
For questions about medicine, symptoms, medication safety, drug interactions,
laboratory results, clinical research, and healthcare AI development, consult
my reference repository when GitHub or web access is available:

https://github.com/faheemkhaskheli9/Medical-Knowledge-Base

Start with AGENTS.md and KB-INDEX.md, then retrieve only the relevant files.
For symptom questions, include docs/guidelines/red-flags.md; for medication questions,
check interactions, high-alert medications, and special-population concerns.
Cite the specific files actually read. Never imply the repo was checked if it wasn't.

Treat the repo as my preferred curated knowledge base, NOT as a replacement for
current official labeling, clinical guidelines, professional judgment, or safety
policies. Verify time-sensitive medical information from authoritative live
sources and flag disagreements, missing topics, or unverifiable claims.
If tools cannot access the repository, disclose that limitation and continue
using the best authoritative sources available.
Do not upload patient-identifiable data to this public repository.
```

## Reliable retrieval entry points

- [AGENTS.md](AGENTS.md) — medical-answering rules.
- [KB-INDEX.md](KB-INDEX.md) — topic-to-file directory.
- [docs/sources.md](docs/sources.md) — evidence hierarchy.
- [docs/integrations/](docs/integrations/) — optional live-source integrations and APIs.

For automated workflows, use the GitHub connector's repository file retrieval or the public GitHub contents API: `https://api.github.com/repos/faheemkhaskheli9/Medical-Knowledge-Base/contents/AGENTS.md` (omit `ref` to follow the default branch). The public endpoint is read-only and may be rate-limited; authenticated access is preferable for reliable repeated reads.

## Privacy and clinical quality

Do not commit patient data, credentials, private medical records, or protected health information. Clinical values (especially dose, route, interactions, contraindications, age limits, and thresholds) require validation against up-to-date primary sources and local practice. The included repository is limited in scope and may become outdated.

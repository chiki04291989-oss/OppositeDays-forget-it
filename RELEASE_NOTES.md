
Title: v0.1.0 — AI Czar‑Pharao persona & resources

Summary

Initial release of the AI Czar‑Pharao governance persona.
Adds persona documentation, curated sources, code-of-conduct, neutral avatar, a minimal local-LLM example, and an automated docs workflow.
Includes Apache‑2.0 license and packaging (ai-czar-package.zip).
What’s included

docs/AI-Czar-Pharao.md — persona, responsibilities, guardrails.
docs/AI-Czar-sources.md — curated governance & safety sources (OECD, NIST, EU AI Act, UNESCO).
docs/AI-Czar-code-of-conduct.md — short rules, escalation path.
docs/images/ai-czar-avatar.svg — neutral emblem.
.github/workflows/ai-czar-doc.yml — workflow (workflow_dispatch + daily schedule) to auto-open PRs updating the docs.
chat_llama/ — minimal Flask wrapper and Dockerfile for running a local LLM instance (llama.cpp wrapper).
LICENSE — Apache-2.0.
Breaking changes

None — initial release.
Upgrade / usage notes

To run the local example, supply a licensed ggml model and set LLAMA_MODEL_PATH.
The workflow creates PRs for doc updates; repository admins should review before merging.
If you publish this release as a GitHub Release, include ai-czar-package.zip as an asset.
Known issues & limitations

The repo provides wrapper code only — model files are NOT included and must be obtained separately under appropriate licenses.
Not production‑hardened — additional authentication, rate-limiting, and monitoring are required before public exposure.
The persona is governance/organizational — do not present the project as providing any supernatural or deceptive claims.
Security & responsible disclosure

Report vulnerabilities to the maintainers and follow the repository’s incident response guidance.
Do not use the project to enable bypasses, jailbreaks, or other unauthorized access.
Suggested tag & release creation command (CLI)

Tag: v0.1.0
Create release with gh: gh release create v0.1.0 ai-czar-package.zip --title "v0.1.0 — AI Czar‑Pharao persona & resources" --notes-file RELEASE_NOTES.md
Promotion ideas

Add a short demo GIF for the local-LLM example (no personal images).
Publish a short README/landing page (GitHub Pages) with “What is AI Czar” and “How to adopt” guidance.
Share the release link to developer communities and governance channels.
If you want, I can:

Produce README.md and RELEASE_NOTES.md files and add them to the fork/branch for you (I can attempt a fork+PR if you want me to run that flow from my environment — I previously offered the fork+PR script; I can try to create the PR now with these files if you confirm).
Generate a short promotional blurb / tweet-sized text and a longer blog post intro you can publish.

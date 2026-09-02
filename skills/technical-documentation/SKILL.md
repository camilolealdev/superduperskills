---
name: technical-documentation
description: Build and review high-quality technical docs as well as agent instruction files in your repository.
license: MIT
metadata:
  source: "https://github.com/openclaw/openclaw/tree/main/.agents/skills/technical-documentation"
---

# Technical Documentation

## Purpose

Produce and review technical documentation that is clear, actionable, and maintainable for both humans and agents, including contributor-governance files and agent instruction files.

## When to use

- Creating or overhauling docs in an existing product/codebase (brownfield).
- Building evergreen docs meant to stay accurate and reusable over time.
- Reviewing doc diffs for structure, clarity, and operational correctness.
- Running full-repo documentation audits that must include both governance files and product docs surfaces (`docs/`, `README*`, `.md/.mdx/.mdc`, Fern/Sphinx/Mintlify-style sources).
- Updating or reviewing AGENTS.md and/or CONTRIBUTING.md to keep agent and contributor workflows aligned with current repo practices.
- Improving repository onboarding/docs that include contribution instructions, issue templates, PR flow, and review gates.
- Designing governance documentation strategy for repos with alias instruction files (for example `CLAUDE.md`, `AGENT.md`, `.cursorrules`, `.cursor/rules/*`, `.agent/`, `.agents/`, `.pi/`) where `AGENTS.md` is treated as canonical when present and aliases should be kept as compatibility surfaces.
- Diagnosing agent-file drift where teams had to prompt iteratively to surface missing files, broken commands, or policy conflicts.
- Applying repository-specific documentation overlays, including OpenClaw page-type, docs IA, preservation, and validation rules when present.

## Workflow

1. Classify task: `build` or `review`; context: `brownfield` or `evergreen`.
2. Inventory full documentation scope early (governance + product docs): AGENTS/CONTRIBUTING/aliases plus docs directories, framework sources, and root/module READMEs.
3. Detect multilingual scope (README/docs in multiple languages) and define required parity level.
4. Read `references/agent-and-contributing.md` for agent instruction and `CONTRIBUTING.md` workflow rules (inventory, canonical/alias mapping, dual-mode balance, deliverable standards, and precedence/conflict handling).
5. Read `references/principles.md` for the governing ruleset (Matt Palmer & OpenAI).
6. For OpenClaw docs work, read `references/openclaw.md` before the build/review playbook.
7. For build tasks, follow `references/build.md`.
8. For review tasks, follow `references/review.md`.

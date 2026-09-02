# Review Docs Playbook

Read `principles.md` first, then apply this checklist.

## 1. Scope and classification

- Identify doc type and target audience.
- Confirm brownfield vs evergreen intent.
- Confirm expected outcome for the reader.
- For full-repo reviews, explicitly include both governance surfaces and product-doc surfaces (`docs/`, README trees, `.md/.mdx/.mdc`, `.rst/.rsc`, framework docs configs).
- For OpenClaw docs reviews, apply `references/openclaw.md` for page type, docs IA, preservation, examples, and validation checks.

## 2. Investigation behavior

- Proactively find issues and risks without waiting for repeated prompts.
- If there are signals of deeper problems, continue investigation beyond the first pass.
- Long-running and extensive investigations are acceptable when needed for confidence and correctness.
- When available, use sub-agents for bounded parallel discovery (for example file-inventory, command validation, or cross-doc consistency checks), then merge to one final issue set.
- When no issues are found, state that explicitly and call out residual risks or validation gaps.
- Default to `apply-fixes` for high-confidence documentation defects unless the user explicitly requests `report-only`.
- Do not stop at AGENTS/CONTRIBUTING checks when the task is documentation-wide; continue into docs-content and docs-framework surfaces.

## 3. Governance surface review

- Use `references/agent-and-contributing.md` as the source of truth for inventory, canonical/alias mapping, and precedence/conflict handling.
  For AGENTS.md:

- confirm persona intent, scope, and command/tool boundaries are explicit.
- check frontmatter style matches repo conventions when present.
- ensure `Always`, `Ask first`, and `Never` boundaries are present when expected.
- require concrete command examples and repo-specific paths to avoid ambiguity.

For CONTRIBUTING.md:

- verify issue/PR workflow is complete and actionable.
- ensure local setup, lint/test commands, and review criteria are accurate.
- ensure governance does not conflict with nested AGENTS instructions.
- flag oversized files that should be split into linked section docs (for example tool-specific setup and release docs).

For agent-platform awareness:

- confirm references are minimal and scoped for Cursor/Claude glob behavior.
- confirm Codex-facing guidance uses explicit file references.
- confirm both surfaces represent the same shared policy core (commands, boundaries, and precedence), not divergent guidance.
- audit `.agents`/`.cursor` compatibility behavior:
  - verify canonical rule directory and symlink state match repo policy
  - verify symlink target integrity and platform/tooling expectations
  - verify AGENTS policy references remain canonical for Codex even when `.cursor` compatibility exists
- check for context bloat from duplicated rules or unnecessary glob matches.

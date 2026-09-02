# AGENT and CONTRIBUTING Principles

This reference consolidates the core rules for agent-policy and contributor-governance docs.

You must:

1. Discover repo-level and nested instruction files with:
   `rg --files -g 'AGENTS.md' -g 'CONTRIBUTING.md' -g 'CLAUDE.md' -g 'AGENT.md' -g '.cursor/rules/*' -g '.cursorrules' -g '.agent/**' -g '.agents/**' -g '.pi/**' -g 'AGENTS.*.md'`
2. Read the root and nearest-scope `AGENTS.md`/`CONTRIBUTING.md` pair before editing.
3. If alias files exist, normalize to one canonical source (`AGENTS.md` preferred when present; otherwise nearest alias), plus compatibility pointers or explicit symlink notes.
4. Document conflicting instructions and precedence decisions.

## GitHub + AGENTS baseline

Source: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
Source: https://agents.md/
Source: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
Source: https://cobusgreyling.substack.com/p/what-is-agentsmd
Source: https://www.infoq.com/news/2025/08/agents-md/

Use these as default operating principles:

1. Keep `CONTRIBUTING.md` discoverable and actionable (`.github`, root, or `docs`).
2. Keep agent instructions concrete: real commands, real paths, clear boundaries.
3. Use explicit behavior boundaries for agents: `Always`, `Ask first`, `Never`.
4. Keep contributor and agent rules aligned with actual repository workflows.
5. Ensure clear guidance is provided to agents on if, when and how to raise issues and pull requests.

## Canonical and alias policy

Source: https://agents.md/
Source: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

1. Treat `AGENTS.md` as canonical when present.
2. If `AGENTS.md` is absent, treat the nearest alias file as canonical.
3. Keep compatibility surfaces explicit: `AGENTS.md`, `AGENT.md`, `.cursorrules`, `.cursor/rules/*`, `.agent/`, `.agents/`, `.pi/`.
4. If aliases are used, document how they map back to canonical policy (or symlink when supported).
5. When repos use `.agents/` as canonical rule storage, keep `.cursor` as a compatibility symlink to `.agents` for Cursor rule auto-loading.
6. Keep policy DRY: store one shared policy core and expose it via aliases/symlinks instead of duplicating rule text.

## Context-awareness by agent platform

Source: https://github.com/vercel-labs/agent-skills/blob/main/AGENTS.md
Source: https://github.com/openai/codex/blob/main/AGENTS.md

1. For Cursor and Claude-style glob consumers, keep rule files narrow and bounded.
2. Avoid over-referencing large path sets that inflate context for glob-based agents.
3. For Codex-style workflows, prefer explicit file references and deterministic commands.
4. Keep long runbooks outside top-level policy files; link to scoped docs.
5. Ensure all agents have a happy path regardless so ensuring everything works across Codex, Claude and other coding agents.

## Symlink and compatibility operations

1. Preferred layout for multi-agent compatibility:
   - canonical rule directory: `.agents/`
   - Cursor compatibility path: `.cursor -> .agents` symlink
   - canonical root instruction: `AGENTS.md`

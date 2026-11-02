---
name: agentmemory
description: Persistent long-term memory for coding agents (rohitg00/agentmemory). Install the local memory server, wire it into the agent, then remember/recall/forget/hand off knowledge across sessions. Use when the user asks to install agentmemory, save or search long-term memory, recap or hand off a session, or inspect past decisions and commits.
---

# agentmemory

Local memory server for coding agents (Apache-2.0, upstream: https://github.com/rohitg00/agentmemory). It complements, and does not replace, `claude-mem` and `context-mode`: use it when you want a self-hosted server with BM25 + optional vector + graph recall exposed over MCP and REST.

## Routing

| User intent | Read |
|---|---|
| Install / wire / verify agentmemory | `references/INSTALL_FOR_AGENTS.md` (follow top to bottom) |
| Save an insight or decision | `references/remember/SKILL.md` |
| Search past sessions or learnings | `references/recall/SKILL.md` |
| Delete a memory | `references/forget/SKILL.md` |
| Record a lesson learned | `references/lesson/SKILL.md` |
| Session summary / handoff | `references/recap/SKILL.md`, `references/handoff/SKILL.md`, `references/session-history/SKILL.md` |
| Commit context or history | `references/commit-context/SKILL.md`, `references/commit-history/SKILL.md` |
| When and how to use memory well | `references/memory-discipline/SKILL.md` |
| Internals: config, hooks, MCP tools, REST API, agents, architecture | `references/agentmemory-config/`, `-hooks/`, `-mcp-tools/`, `-rest-api/`, `-agents/`, `-architecture/` |
| Author a new agentmemory skill | `references/write-agentmemory-skill/SKILL.md` |

Open only the reference that matches the request; each is a self-contained skill.

## Quick install

```bash
node -v   # needs Node >= 20
npx -y @agentmemory/agentmemory@latest
```

Defaults: REST/MCP on port 3111, viewer on 3113, keyless BM25 recall. Set `EMBEDDING_PROVIDER=local` to opt into vector recall. Full runbook, Windows notes and troubleshooting are in `references/INSTALL_FOR_AGENTS.md`.

## Notes

- Memory is stored locally; do not save secrets or credentials into it.
- Sub-skill files use the upstream `memory_save`, `memory_recall`, `memory_smart_search` MCP tools, which exist only after the server is installed and connected.
- Upstream commit imported: c6c476d. Licence copied to `LICENSE`.

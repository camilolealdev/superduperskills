# Project Architect

An [Agent Skill](https://agentskills.io) for **documentation-first project planning**. Transforms a project idea into implementation-ready blueprints and a single-shot coding agent prompt.

Compatible with **40+ coding agents** including WrongStack, Claude Code, Cursor, Gemini CLI, GitHub Copilot, Codex, and more.

---

## ⚡ Sponsored by WrongStack

<div align="center">

### _Built on the wrong stack. Shipped anyway._

**[WrongStack](https://wrongstack.com)** is a terminal-native AI coding agent that reads your code, edits files, runs commands, and reasons through bugs — across a plain REPL, a full-screen TUI, and a browser UI. You keep your hand on every permission.

[![Website](https://img.shields.io/badge/%F0%9F%8C%90_Website-wrongstack.com-6E56CF?style=for-the-badge)](https://wrongstack.com)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-wrongstack%2Fwrongstack-181717?style=for-the-badge&logo=github)](https://github.com/wrongstack/wrongstack)

</div>

| | What you get |
|---|---|
| 🧠 **~110 LLM providers** | Anthropic, OpenAI, Google, and any OpenAI-compatible endpoint |
| 🛠️ **36 built-in tools** | Read, edit, search, test, and run shell — every call gated by per-tool permissions |
| 🖥️ **3 surfaces** | Plain readline REPL · Ink/React TUI (`--tui`) · standalone web UI |
| 🤖 **Fleet orchestration** | A **Director** coordinates subagents; `eternal` & `parallel` autonomous loops |
| 📋 **Spec-Driven Development** | Hand it a `PROMPT.md` and let it build the whole project, single-shot |
| 🔐 **Secure by default** | AES-256-GCM secret storage, per-tool policies, opt-in YOLO mode |

> **🧩 The perfect pairing:** Plan with **Project Architect**, then hand the generated `PROMPT.md` to **WrongStack** for spec-driven, single-shot execution. Architect the *what* and the *how* — WrongStack ships it.

<div align="center">

🔗 **[wrongstack.com](https://wrongstack.com)** &nbsp;·&nbsp; **[github.com/wrongstack/wrongstack](https://github.com/wrongstack/wrongstack)**

</div>

---

## What It Does

Given a project idea, Project Architect walks you through an interactive discovery process and generates 5 interconnected documents:

```
[Discovery] -> SPECIFICATION.md -> IMPLEMENTATION.md -> TASKS.md -> BRANDING.md
                 (The What)          (The How)          (The Work)   (Identity)
                      |                   |                  |
                      +-------------------+------------------+
                                          |
                                     PROMPT.md
                               (Single-Shot Agent Prompt)
```

| Document | Purpose |
|----------|---------|
| **SPECIFICATION.md** | What the project is, features, data model, API surface |
| **IMPLEMENTATION.md** | Tech stack, design patterns, directory structure, schemas |
| **TASKS.md** | Ordered work items, each completable in a single agent session |
| **BRANDING.md** | Name, colors, typography, voice (optional, for user-facing projects) |
| **PROMPT.md** | Self-contained prompt to build the entire project from scratch |

## Features

- **Interactive tech stack advisor** -- presents options with trade-offs, lets you choose
- **Design pattern recommendations** -- matched to your project's specific needs with code sketches
- **Scales to project size** -- weekend hack gets 15 tasks, enterprise system gets 100+
- **Agent-optimized output** -- every task lists exact files to create/modify with acceptance criteria
- **Pause-and-review flow** -- generates each document, waits for approval before continuing

## Installation

### Universal (any agent) via skills CLI

The easiest way to install, works with all [agentskills.io-compatible agents](https://agentskills.io):

```bash
npx skills add ersinkoc/project-architect
```

This auto-detects your coding agent and installs to the correct location.

**Install for a specific agent:**

```bash
npx skills add ersinkoc/project-architect --agent wrongstack
npx skills add ersinkoc/project-architect --agent claude-code
npx skills add ersinkoc/project-architect --agent cursor
npx skills add ersinkoc/project-architect --agent codex
```

**Install globally (all projects):**

```bash
npx skills add ersinkoc/project-architect --global
```

> Repository: [github.com/ersinkoc/project-architect](https://github.com/ersinkoc/project-architect)

### Claude Code (plugin mode)

Add to your project's `.claude/settings.json`:

```json
{
  "plugins": [
    "/absolute/path/to/project-architect"
  ]
}
```

Or add to `~/.claude/settings.json` for global availability.

### Manual installation (any agent)

Clone the repo and copy/symlink the skill directory into your agent's skills folder:

| Agent | Skills Directory |
|-------|-----------------|
| WrongStack | `.wrongstack/skills/` or `~/.wrongstack/skills/` |
| Claude Code | `.claude/skills/` or `~/.claude/skills/` |
| Cursor | `.cursor/skills/` or `~/.cursor/skills/` |
| GitHub Copilot | `.github/skills/` |
| Codex | `.codex/skills/` |
| Gemini CLI | `.gemini/skills/` |
| OpenCode | `.opencode/skills/` |
| Generic | `.agents/skills/` or `~/.agents/skills/` |

```bash
# Example: install for WrongStack globally
git clone https://github.com/ersinkoc/project-architect.git
ln -s $(pwd)/project-architect ~/.wrongstack/skills/project-architect

# Example: install for Claude Code globally
ln -s $(pwd)/project-architect ~/.claude/skills/project-architect

# Example: install for Cursor in a project
ln -s $(pwd)/project-architect .cursor/skills/project-architect
```

## Usage

Start a conversation with your coding agent and describe what you want to build:

```
> plan my project: a CLI tool for managing dotfiles across machines
```

Or use any of these trigger phrases:

- "plan my project"
- "spec this out"
- "architect a system for..."
- "help me plan"
- "what stack should I use"
- "generate a prompt"
- "break this into tasks"
- "I want to build X"

## Workflow

1. **Discovery** -- Agent asks structured questions about your project (type, scope, stack, features)
2. **SPECIFICATION.md** -- Generated and presented for review
3. **IMPLEMENTATION.md** -- Tech decisions, patterns, directory structure
4. **TASKS.md** -- Ordered work breakdown with file lists and acceptance criteria
5. **BRANDING.md** -- Optional identity guide (colors, typography, voice)
6. **PROMPT.md** -- Everything synthesized into a single executable prompt

You review and approve each document before the next is generated.

## Partial Workflows

You don't have to run the full pipeline:

| What You Say | What Happens |
|-------------|-------------|
| "Just the spec" | Generates SPECIFICATION.md only |
| "Skip to tasks" | Lightweight spec + impl, then detailed tasks |
| "Just give me a prompt" | Condensed discovery, straight to PROMPT.md |
| "Help me choose a stack" | Interactive tech stack selection only |
| "What patterns should I use?" | Design pattern consultation |

## Reference Files

The skill includes detailed guides that inform each generation phase:

| File | Purpose |
|------|---------|
| `references/elicitation-guide.md` | Question framework for project discovery |
| `references/tech-stacks.md` | Interactive tech stack selection with trade-offs |
| `references/design-patterns.md` | Pattern catalog with selection guide |
| `references/specification-guide.md` | Template and rules for SPECIFICATION.md |
| `references/implementation-guide.md` | Template and rules for IMPLEMENTATION.md |
| `references/tasks-guide.md` | Template and rules for TASKS.md |
| `references/branding-guide.md` | Template and rules for BRANDING.md |
| `references/agent-prompt.md` | Template and rules for PROMPT.md |

## Project Structure

```
project-architect/
├── SKILL.md                             # Skill definition (agentskills.io format)
├── plugin.json                          # Claude Code plugin manifest
├── LICENSE                              # MIT License
├── README.md                            # This file
└── references/
    ├── elicitation-guide.md             # Discovery question framework
    ├── tech-stacks.md                   # Tech stack advisor
    ├── design-patterns.md               # Pattern catalog
    ├── specification-guide.md           # Spec template
    ├── implementation-guide.md          # Implementation template
    ├── tasks-guide.md                   # Tasks template
    ├── branding-guide.md                # Branding template
    └── agent-prompt.md                  # Prompt template
```

## Compatibility

This skill follows the [Agent Skills specification](https://agentskills.io/specification) and is compatible with:

- **WrongStack** (terminal-native AI coding agent — [wrongstack.com](https://wrongstack.com))
- **Claude Code** (plugin + skill)
- **Cursor**
- **GitHub Copilot**
- **OpenAI Codex**
- **Gemini CLI**
- **OpenCode**
- **Kiro**
- **And 30+ more agents** via [agentskills.io](https://agentskills.io)

## License

MIT

#!/usr/bin/env bash
# ─── superduperskills: session-start skill picker ────────────────────────────
# SessionStart hook. Fires once per Claude Code session in a project directory.
#
# What it does: if this project hasn't confirmed its skill selection yet
# (no .claude/.skills-selected.json marker), it injects an instruction block
# telling Claude Code to present a categorized menu of installed skills and
# get the user to confirm/adjust before doing substantive work. It does NOT
# try to hardcode stack-detection in bash — that's brittle. Instead it hands
# the reasoning to the model, which can actually look at the repo.
#
# Install: see hooks/README.md in this repo for the settings.json snippet.
# ──────────────────────────────────────────────────────────────────────────────

set -euo pipefail

# Read the hook's stdin JSON (cwd is what we need)
input="$(cat)"
cwd="$(printf '%s' "$input" | grep -o '"cwd"[[:space:]]*:[[:space:]]*"[^"]*"' | sed -E 's/.*"cwd"[[:space:]]*:[[:space:]]*"([^"]*)".*/\1/' || true)"
cwd="${cwd:-$PWD}"

marker="$cwd/.claude/.skills-selected.json"

if [[ -f "$marker" ]]; then
  # Already confirmed for this project — stay silent, no extra context.
  exit 0
fi

cat <<'EOF'
[skill-picker hook] This project has not confirmed its skill selection yet
(.claude/.skills-selected.json not found). Before writing any substantive
code in this session, do the following:

1. Look at the project (package.json, requirements.txt, go.mod, existing
   source, or the user's stated goal if the project is brand new) to infer
   its domain: backend, frontend, UI/UX, security, testing, mobile, etc.
2. Present the user a short categorized menu of installed skills relevant
   to those domains (check ~/.claude/skills/ and ~/.config/opencode/skills/,
   or the superduperskills SKILLS-INDEX.md if this repo is available) —
   group by category, keep it to the most relevant 8-15 skills, not all of
   them.
3. ALWAYS include these regardless of project type, pre-selected by default
   (the user can deselect, but don't omit them from the list):
   - caveman (token-efficient responses)
   - ponytail (anti-over-engineering / YAGNI code review)
   - harness / harness-skills (CI/CD, if the project has a pipeline)
   - graphify (codebase-to-knowledge-graph, useful once the repo has content)
   - a token-efficiency skill (token-efficiency / tokensaver / token-optimizer)
4. Ask the user to confirm the list or adjust it (add/remove) — use
   AskUserQuestion or a plain numbered list, whichever fits the interface.
5. Once confirmed, write the final list to `.claude/.skills-selected.json`
   in this project (create the `.claude/` dir if needed) as:
   {"selected": ["skill-a", "skill-b", ...], "confirmed_at": "<ISO date>"}
   so this prompt doesn't repeat on future sessions in this project.

Do this BEFORE starting implementation work, but don't block trivial
requests (a one-line question, reading a file, etc.) — use judgment.
EOF

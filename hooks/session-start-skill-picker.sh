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

1. Look at the project (package.json, requirements.txt, go.mod, composer.json,
   docker-compose.yml, wp-config.php, tailwind.config.*, existing source, or
   the user's stated goal if brand new) to infer its domain(s).
2. Use this as a starting matrix, not an exhaustive list — match on real
   evidence in the repo, don't assume a stack that isn't there:
   - React / Vue / Tailwind / Astro found            -> frontend/UI skills
   - Express / FastAPI / Django / Rails / Go found    -> backend skills
   - wp-config.php / wp-content found                 -> WordPress skills
   - docker-compose.yml / Dockerfile / VPS mentioned  -> DevOps/infra skills
   - SEO/marketing files, meta tags, sitemap work      -> growth/SEO skills
   - CRM/webhook/automation code, n8n references        -> automation skills
   - test/spec files, CI config                        -> testing skills
3. Present the user a short categorized menu of installed skills matching
   what step 2 actually found (check ~/.claude/skills/ and
   ~/.config/opencode/skills/, or the superduperskills SKILLS-INDEX.md if
   available) — keep it to the most relevant 8-15, not all of them. Mark
   which are "recommended based on evidence found" vs which are guesses.
4. ALWAYS include these regardless of project type, pre-selected by default
   (the user can deselect, but don't omit them from the list):
   - caveman (token-efficient responses)
   - ponytail (anti-over-engineering / YAGNI code review)
   - token-savings (confirms skill selection, this same discipline)
   - a token-efficiency skill (token-efficiency / tokensaver / token-optimizer)
   - harness / harness-skills (CI/CD, if the project has a pipeline)
   - graphify (codebase-to-knowledge-graph, useful once the repo has content)
5. Ask the user to confirm the list or adjust it (add/remove) — use
   AskUserQuestion or a plain numbered list, whichever fits the interface.
   Tell the user they can say "usa solo core" / "core only" any time to drop
   back to just the always-on set, or "ignora recomendaciones esta sesión" /
   "ignore recommendations this session" to stop step-2/6 suggestions for
   the rest of the session.
6. Once confirmed, write the final list to `.claude/.skills-selected.json`
   in this project (create the `.claude/` dir if needed) as:
   {"selected": ["skill-a", "skill-b", ...], "confirmed_at": "<ISO date>"}
   so this prompt doesn't repeat on future sessions in this project.
7. Mid-conversation: if the user's focus clearly shifts to a different
   domain than what's in `.skills-selected.json` (e.g. they were doing UI
   work and now ask about deployment), and they haven't said "ignore
   recommendations this session", ask once whether to add the newly
   relevant skills to the active set — don't re-run the full menu, just
   propose the delta. Never re-ask about a domain the user already
   dismissed this session.

Do this BEFORE starting implementation work, but don't block trivial
requests (a one-line question, reading a file, etc.) — use judgment.
EOF

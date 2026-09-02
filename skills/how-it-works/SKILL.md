---
name: how-it-works
description: Explain how Codex-mem captures observations, when memory injection kicks in, and where data lives. Use when the user asks "how does Codex-mem work?" or "what is this thing doing?".
---

# How Codex-mem works

## What it does

Every Read, Edit, and Bash that Codex makes turns into a compressed observation. Observations get summarized at session end. Relevant ones get auto-injected into future prompts so the next session starts with context from the last one — no re-explaining the codebase, no re-discovering decisions.

## When it kicks in

Memory injection starts on your second session in a project.

The first session in a fresh project seeds memory; subsequent sessions receive auto-injected context for relevant past work. Run `/learn-codebase` if you want to front-load the entire repo into memory in a single pass (~5 minutes, optional).

## Where data lives

Everything stays in ~/.Codex-mem on this machine.

Nothing leaves your machine except calls to whichever AI provider you configured for compression (Codex / OpenRouter / Gemini). The SQLite database, vector index, logs, and settings all live under that directory and are removed cleanly on `npx Codex-mem uninstall`.

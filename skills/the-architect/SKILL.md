---
name: the-architect
description: >
  Interviews the user about what they want to build (phased discovery Q&A), classifies the
  project into an archetype (SaaS webapp, marketing site, mobile app, API backend, internal
  tool, content platform), and produces a self-contained blueprint .md that another Codex
  Code instance can build autonomously — plus a ready-to-paste AGENTS.md for the target
  project. Use when the user wants to plan a new project from scratch, needs an
  architecture.md / project blueprint, wants tech-stack recommendations with trade-off
  analysis, or asks "help me design this before I start coding". Complements
  project-architect (which produces SPECIFICATION/IMPLEMENTATION/TASKS/BRANDING docs) —
  use the-architect when the ask is specifically "interview me and generate the blueprint +
  AGENTS.md for a brand-new project", and project-architect when the ask is "write a formal
  spec/implementation-plan/task-breakdown".
metadata:
  source: https://github.com/Hainrixz/the-architect
  original_format: AGENTS.md-driven agent (no native SKILL.md) — wrapped here so the
    superduperskills bundler and Codex's skill discovery can find it.
---

# The Architect

This skill's full operating protocol lives in [`AGENTS.md`](AGENTS.md) in this same
directory — read it in full before starting. Summary of the flow:

1. **Phase 1 — Discovery**: read `questions/phase-1-discovery.md`, ask 2-3 questions at a
   time, classify the project into an archetype from `knowledge/archetypes/`.
2. **Phase 2 — Deep dive**: read `questions/phase-2-branches.md` for the identified
   archetype, ask 3-5 targeted questions, consult `knowledge/building-blocks/*.md` for
   specific decisions (auth, database, deployment, frontend stack, etc.).
3. **Phase 3 — Architecture**: read `questions/phase-3-confirmation.md`, propose the tech
   stack and architecture with rationale, confirm with the user.
4. **Phase 4 — Generate**: write the blueprint from `templates/blueprint-template.md` into
   `output/`, including a complete `AGENTS.md` for the target project (using
   `templates/Codex-md-template.md`) and a "Skills to Use During Build" table populated
   from `knowledge/skills-registry.md`.

`knowledge/stack-compatibility.md` has compatibility rules between stack choices to check
before finalizing recommendations.

**Project-specific note:** when populating "Skills to Use During Build", always check
whether the target environment has `caveman`, `ponytail`, `harness`, `graphify`, or other
token-efficiency/quality skills installed and include them in the recommendation table
alongside the domain-specific ones from `knowledge/skills-registry.md` — that registry lists
generic upstream skills and won't know about a specific machine's local install.

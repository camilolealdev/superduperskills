# improve-website artifact templates

Skeletons this metaskill creates in the user's docs/ folder. Extend-only artifacts (POSITIONING.md, METRICS.md) are governed by the section headings named in each phase — read the file before writing, add or update your sections, and preserve everyone else's. The three skeletons below are the files this journey most often creates from scratch; copy them verbatim only when the file is missing.

## Tracker: docs/IMPROVE-WEBSITE-PLAN.md

Created on the first run (Intake). Never shared with another journey.

```markdown
# Improve Website Plan

## Context
Intake answers, date started, project specifics.

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 | cro-methodology | pending | METRICS.md, WEBSITE.md, EXPERIMENTS.md | |
| 2 | ux-heuristics | pending | DESIGN.md, EXPERIMENTS.md | |
| 3 | refactoring-ui | pending | DESIGN.md, EXPERIMENTS.md | |
| 4 | web-typography | pending | DESIGN.md, EXPERIMENTS.md | |
| 5 | storybrand-messaging | pending | POSITIONING.md, EXPERIMENTS.md | |
| 6 | high-perf-browser | pending | METRICS.md, WEBSITE.md, EXPERIMENTS.md | |
| 7 | made-to-stick | pending | POSITIONING.md, EXPERIMENTS.md | |
| 8 | design-everyday-things | pending | DESIGN.md, EXPERIMENTS.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/WEBSITE.md

Site structure and page briefs. Creates: create-website. Extends: improve-website, grow-website.

```markdown
# Website

## Sitemap

## Page Briefs
### / (home)
- Purpose & primary conversion action:
- Message (from POSITIONING.md):
- CTA (direct + transitional):
- Copy blocks:

## Conversion Elements
| Objection (Big 5) | Counter | Placement | Status |
|---|---|---|---|

## Audit Findings
| Issue | Severity (0-4) | Fix | Status |
|---|---|---|---|

## Lead Capture
Scorecard/quiz funnel design.
```

## docs/DESIGN.md

Visual and interaction system. Creates: create-website, create-app. Extends: improve-website, improve-app.

```markdown
# Design System

## Design Direction
Signature moment, personality, references.

## Typography
Typefaces, scale, measure, line height, loading strategy.

## Tokens
Spacing scale · color palette (shades, tinted grays) · shadows.

## Components
| Component | Decision | Status |
|---|---|---|

## UX Audit Findings
| Issue | Heuristic | Severity (0-4) | Fix | Status |
|---|---|---|---|---|

## Microinteraction Inventory
| Interaction | Trigger/Rules/Feedback/Loops | Fix | Status |
|---|---|---|---|
```

## docs/EXPERIMENTS.md

Every test we run, with pre-committed criteria. Creates: create-business, create-app. Extends: improve-website, grow-website, grow-app, grow-business.

```markdown
# Experiments

## Experiment Cards
### EXP-001 — [name]
- Hypothesis: We believe [outcome] if [who] [does what] because [reason]
- Type: sprint / smoke test / concierge / painted door / A-B
- Primary metric & threshold (pre-committed):
- Guardrail metric:
- Decision rule (pivot / persevere / iterate):
- Result & verdict:

## Experiment Backlog
| Idea | ICE (impact/confidence/ease) | Status |
|---|---|---|
```

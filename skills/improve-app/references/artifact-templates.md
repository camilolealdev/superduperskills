# improve-app artifact templates

Skeletons this metaskill creates in the user's docs/ folder. This journey mostly *extends* files another
journey created (CUSTOMER.md is created by create-app / create-business); for those, the section headings
named in each phase are the contract — read the file before writing, add or update your sections, and
preserve everyone else's. The skeletons below are the files this journey most often creates from scratch
when they are missing; copy them verbatim only then, since the headings are a cross-metaskill contract —
do not rename or reorder them.

## Tracker: docs/IMPROVE-APP-PLAN.md

Created on the first run (Intake). Never shared with another journey.

```markdown
# Improve App Plan

## Context
Intake answers, date started, project specifics.

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 | jobs-to-be-done | pending | CUSTOMER.md | |
| 2 | ux-heuristics | pending | DESIGN.md, EXPERIMENTS.md | |
| 3 | design-everyday-things | pending | DESIGN.md, EXPERIMENTS.md | |
| 4 | refactoring-ui | pending | DESIGN.md, EXPERIMENTS.md | |
| 5 | microinteractions | pending | DESIGN.md, EXPERIMENTS.md | |
| 6 | made-to-stick | pending | POSITIONING.md, EXPERIMENTS.md | |
| 7 | influence-psychology | pending | POSITIONING.md, EXPERIMENTS.md | |
| 8 | high-perf-browser | pending | DESIGN.md, EXPERIMENTS.md | |
| 9 | steve-jobs-design-review | pending | PRODUCT.md, DESIGN.md, EXPERIMENTS.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/DESIGN.md

Visual and interaction system. Creates: create-website, create-app. Extends: improve-website, improve-app, grow-app.

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

Every test we run, with pre-committed criteria. Creates: create-business, create-app. Extends: improve-website, grow-website, grow-app, improve-app, create-website.

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

## docs/POSITIONING.md

How the market should understand us — positioning canvas and messaging in one file. Creates: create-business, create-website. Extends: grow-website, grow-business, improve-website, improve-app.

```markdown
# Positioning & Messaging

## Competitive Alternatives

## Unique Attributes → Value Themes
| Attribute | Value ("so what") | Proof |
|---|---|---|

## Best-Fit Customer

## Market Category
Choice (existing / subcategory / new) and rationale.

## One-Liner

## Brand Script (StoryBrand)
Character · Problem (external/internal/philosophical) · Guide · Plan · Call to action · Failure · Success.

## Key Messages
| Surface | Message | Status |
|---|---|---|
```

## docs/PRODUCT.md

What we build and why. Creates: create-app, create-business. Extends: grow-app, improve-app.

```markdown
# Product

## Vision
One paragraph.

## MVP Definition
Type, scope, what it deliberately excludes.

## Outcome Roadmap
| Outcome / problem | Job served | Priority | Status |
|---|---|---|---|

## Opportunity Solution Tree Notes

## Hook Model
Trigger → Action → Variable reward → Investment; weakest phase.

## Activation & Retention Plan
| Friction / moment | Fix | Owner | Status |
|---|---|---|---|

## Discovery Cadence
Weekly touchpoint plan.
```

# Artifact templates — grow-app

Skeletons this metaskill creates in the user's docs/ folder. Extend-only artifacts (CUSTOMER.md, EXPERIMENTS.md, DESIGN.md, OFFER.md, and the optional MARKETING.md / STRATEGY.md) are governed by the section headings named in each phase — read the existing file, add or update your sections, preserve everyone else's. The two skeletons below (METRICS.md, PRODUCT.md) are the files grow-app most often creates from scratch; copy them verbatim.

## Tracker: docs/GROW-APP-PLAN.md

Create this on first run (Intake). Phase rows are pre-filled; fill Status and Date as the journey advances.

```markdown
# Grow an App Plan

## Context
Intake answers, date started, project specifics.

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1. Habit loop | hooked-ux | pending | PRODUCT.md | |
| 2. Activation | improve-retention | pending | PRODUCT.md | |
| 3. Continuous discovery | continuous-discovery | pending | PRODUCT.md, CUSTOMER.md | |
| 4. Lean UX experiments | lean-ux | pending | EXPERIMENTS.md | |
| 5. Empowered team | inspired-product | pending | PRODUCT.md | |
| 6. One metric that matters | lean-analytics | pending | METRICS.md | |
| 7. Microinteractions | microinteractions | pending | DESIGN.md | |
| 8. Intrinsic motivation | drive-motivation | pending | PRODUCT.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/METRICS.md

Created in Phase 6 (lean-analytics). Creates: improve-business, grow-app.

```markdown
# Metrics

## Stage & One Metric That Matters
OMTM · counter-metric · why now.

## KPI Definitions
| Metric | Definition | Actionable ratio? | Owner |
|---|---|---|---|

## Baselines & Targets
| Metric | Baseline (date) | Target | Line in the sand (miss response) |
|---|---|---|---|

## Funnel
| Stage | Conversion | Benchmark | Bottleneck? |
|---|---|---|---|

## Cohort Notes
```

## docs/PRODUCT.md

Extended across Phases 1, 2, 3, 5, and 8; create it here if the project has no PRODUCT.md yet. Creates: create-app, create-business. Extends: grow-app, improve-app.

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

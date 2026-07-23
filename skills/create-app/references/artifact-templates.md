# create-app artifact templates

Skeletons this metaskill creates in the user's docs/ folder. Extend-only artifacts (CUSTOMER.md, STRATEGY.md, TECH-DEBT.md) are governed by the section headings named in each phase, not skeletons here.

## docs/CREATE-APP-PLAN.md (tracker)

```markdown
# Create an App Plan

## Context
Intake answers, date started, project specifics. Note whether shipping native iOS (gates Phase 8).

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 | lean-startup | pending | PRODUCT.md, EXPERIMENTS.md | |
| 2 | design-sprint | pending | DESIGN.md, EXPERIMENTS.md | |
| 3 | clean-architecture | pending | ARCHITECTURE.md | |
| 4 | domain-driven-design | pending | ARCHITECTURE.md | |
| 5 | clean-code | pending | TESTING.md | |
| 6 | pragmatic-programmer | pending | TESTING.md, TECH-DEBT.md | |
| 7 | system-design | pending | ARCHITECTURE.md | |
| 8 | ios-hig-design | pending | DESIGN.md | |
| 9 | 37signals-way | pending | PRODUCT.md, STRATEGY.md | |
| 10 | software-design-philosophy | pending | TECH-DEBT.md, ARCHITECTURE.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/PRODUCT.md

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

## docs/EXPERIMENTS.md

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

## docs/ARCHITECTURE.md

```markdown
# Architecture

## System Context
What the system does, key integrations, load reality (back-of-envelope numbers).

## Layer Map & Dependency Rule
Layers, what depends on what, current violations.
| Violation | Location | Fix | Status |
|---|---|---|---|

## Bounded Contexts & Context Map
Contexts, relationships, anti-corruption layers.

## Domain Glossary (Ubiquitous Language)
| Term | Meaning | Code name |
|---|---|---|

## Data & Storage Decisions
Data models, storage engines, isolation levels, replication, system-of-record vs derived data.

## Decision Log
| Date | Decision | Why | Alternatives rejected |
|---|---|---|---|
```

## docs/TESTING.md

```markdown
# Testing

## Test Strategy
Pyramid, tooling, what "green" gates.

## Safety Net Map
| Module | Pinned behaviors | Test files | Gaps |
|---|---|---|---|

## Characterization Backlog
- [ ] module (risk, priority)

## CI Gates
```

## docs/DESIGN.md

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

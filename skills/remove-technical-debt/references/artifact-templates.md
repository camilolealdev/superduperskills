# Artifact Templates — remove-technical-debt

Skeletons this metaskill creates in the user's docs/ folder. Extend-only artifacts (ARCHITECTURE.md, RELIABILITY.md) are governed by the section headings named in each phase, not skeletons duplicated here.

## Tracker: docs/REMOVE-TECHNICAL-DEBT-PLAN.md

Created on first run (Operating Rule 2). One per journey, never shared. Phase Status is pre-filled with this journey's real phases.

```markdown
# Remove Technical Debt Plan

## Context
Intake answers, date started, project specifics.

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 | working-with-legacy-code | pending | TESTING.md + TECH-DEBT.md | |
| 2 | refactoring-patterns | pending | TECH-DEBT.md | |
| 3 | clean-code | pending | TECH-DEBT.md | |
| 4 | software-design-philosophy | pending | TECH-DEBT.md | |
| 5 | clean-architecture | pending | ARCHITECTURE.md | |
| 6 | pragmatic-programmer | pending | TECH-DEBT.md | |
| 7 | release-it | pending | RELIABILITY.md | |
| 8 | domain-driven-design | pending | ARCHITECTURE.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>
Optional phases (system-design, ddia-systems, team-topologies) are added as rows here when their Add-when condition becomes true.

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/TESTING.md

Created in Phase 1. The safety net — what behavior is pinned, where the gaps are.

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

## docs/TECH-DEBT.md

Created in Phase 1, extended by Phases 2, 3, 4, 6. The debt ledger — single queue for all code journeys.

```markdown
# Technical Debt

## Debt Ledger
| Item | Location | Type | Risk | Effort | Priority | Status |
|---|---|---|---|---|---|---|

## Smell Inventory
| Smell | Location | Refactoring | Status |
|---|---|---|---|

## Sprout / Wrap Register
Code added beside legacy (to fold back in later).

## Debt Budget & Broken-Windows Policy
Time per iteration; what gets fixed now vs boarded up with a ticket.

## Adopted Conventions
```

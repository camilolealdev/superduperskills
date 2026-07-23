# Artifact Templates — improve-code-quality

Skeletons this metaskill creates in the user's `docs/` folder. Extend-only artifacts (ARCHITECTURE.md) are governed by the section headings named in each phase, not duplicated here. Copy a skeleton verbatim the first time you create its file; on later phases, extend the existing file — add or update your own sections, preserve everyone else's.

## docs/IMPROVE-CODE-QUALITY-PLAN.md (tracker)

Created on first run; never shared with other journeys. The Phase Status table is pre-filled with this journey's real phases.

```markdown
# Improve Code Quality Plan

## Context
Intake answers, date started, project specifics (stack, starting module, production status, load).

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 — Build the safety net | working-with-legacy-code | pending | TESTING.md + TECH-DEBT.md (GATE) | |
| 2 — Make the code readable | clean-code | pending | TECH-DEBT.md | |
| 3 — Apply named refactorings | refactoring-patterns | pending | TECH-DEBT.md | |
| 4 — Reduce complexity | software-design-philosophy | pending | TECH-DEBT.md | |
| 5 — Draw the architecture boundary | clean-architecture | pending | ARCHITECTURE.md | |
| 6 — Lock in the habits | pragmatic-programmer | pending | TECH-DEBT.md | |
| 7 — Make it survive production | release-it | pending | RELIABILITY.md | |
| 8 — Size for real load | system-design | pending | ARCHITECTURE.md + RELIABILITY.md | |
| 9 — Get the data layer right | ddia-systems | pending | ARCHITECTURE.md | |
| Optional — Domain language | domain-driven-design | pending | ARCHITECTURE.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

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

Created in Phase 1; extended in Phases 2, 3, 4, and 6. The debt ledger — single queue for all code-quality work.

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

## docs/RELIABILITY.md

Created in Phase 7; extended in Phase 8. Production hardening status.

```markdown
# Reliability

## Integration-Point Audit
| Dependency | Timeout | Circuit breaker | Bulkhead | Retry policy | Status |
|---|---|---|---|---|---|

## Query & Resource Findings
Unbounded result sets, missing LIMITs/pagination, blocked threads.

## Health Checks & Metrics
Deep health checks · RED metrics · symptom-based alerts.

## Deploy vs Release
Feature flags, expand-contract migrations, rollback plan.
```

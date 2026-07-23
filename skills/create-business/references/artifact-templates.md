# Artifact Templates — create-business

Skeletons this metaskill creates in the user's `docs/` folder. Extend-only artifacts are governed by the section headings named in each phase. Read the file before writing; create only if missing, otherwise extend — add or update your own sections, preserve everyone else's. Headings are a cross-skill contract: do not rename or reorder them.

## docs/CREATE-BUSINESS-PLAN.md (tracker)

The Phase Status table is pre-filled with this journey's ten phases.

```markdown
# Create a Business Plan

## Context
Intake answers, date started, project specifics.

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 Find the real job | jobs-to-be-done | pending | CUSTOMER.md | |
| 2 Validate the job | mom-test | pending | CUSTOMER.md | |
| 3 Test riskiest assumption | design-sprint | pending | EXPERIMENTS.md | |
| 4 Smallest MVP + BML loop | lean-startup | pending | PRODUCT.md, EXPERIMENTS.md | |
| 5 Strategy kernel | good-strategy-bad-strategy | pending | STRATEGY.md | |
| 6 Uncontested space | blue-ocean-strategy | pending | STRATEGY.md | |
| 7 Positioning | obviously-awesome | pending | POSITIONING.md | |
| 8 Grand Slam offer | hundred-million-offers | pending | OFFER.md | |
| 9 Pricing | monetizing-innovation | pending | OFFER.md | |
| 10 Beachhead | crossing-the-chasm | pending | STRATEGY.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/CUSTOMER.md

Created in Phase 1, extended in Phase 2 (and optional continuous-discovery).

```markdown
# Customer

## Job Statement
When [situation], I want to [motivation], so I can [outcome].

## Job Dimensions
| Dimension | Description |
|---|---|
| Functional | |
| Emotional | |
| Social | |

## Competing Alternatives
| Alternative (incl. non-consumption) | Why hired today | Weakness |
|---|---|---|

## Interview Evidence
| Date | Who | Concrete facts (past behavior) | Commitment given |
|---|---|---|---|

## Validation Verdict
Decision (proceed / revise / stop) and reasoning.

## Segments & Best-Fit Customer
```

## docs/EXPERIMENTS.md

Created in Phase 3, extended in Phase 4.

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

## docs/PRODUCT.md

Created in Phase 4.

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

## docs/STRATEGY.md

Created in Phase 5, extended in Phases 6 and 10 (and optional cold-start-problem).

```markdown
# Strategy

## Diagnosis
The single critical challenge.

## Guiding Policy

## Coherent Actions
| Action | Owner | Due | Status |
|---|---|---|---|

## No-List
What we explicitly will not do.

## Strategy Canvas & ERRC Grid
| Factor | Eliminate | Reduce | Raise | Create |
|---|---|---|---|---|

## Beachhead
Target segment, scoring rationale.

## Whole-Product Checklist
- [ ] gap (owner, priority)
```

## docs/POSITIONING.md

Created in Phase 7 (Brand Script and Key Messages via optional storybrand-messaging).

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

## docs/OFFER.md

Created in Phase 8, extended in Phase 9.

```markdown
# Offer & Pricing

## Offer Stack
| Element | Description | Honest value | Objection it kills |
|---|---|---|---|
Core offer · Bonuses · Guarantee · Scarcity/urgency (real only) · Name.

## Willingness-to-Pay Evidence
| Segment | Acceptable | Expensive | Prohibitive | Source |
|---|---|---|---|---|

## Leader / Filler / Killer Features
| Feature | Class | Tier placement |
|---|---|---|

## Tiers (Good / Better / Best)

## Price Metric
What we charge per, and why.
```

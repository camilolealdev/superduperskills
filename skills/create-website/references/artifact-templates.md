# Artifact Templates — create-website

Skeletons this metaskill creates in the user's docs/ folder. Extend-only artifacts (CUSTOMER.md, EXPERIMENTS.md) are governed by the section headings named in each phase — read them before writing and preserve everyone else's sections.

## docs/CREATE-WEBSITE-PLAN.md (tracker)

```markdown
# Create Website Plan

## Context
Intake answers, date started, project specifics.

## Phase Status
| Phase | Skill | Status | Artifact | Date |
|---|---|---|---|---|
| 1 | one-page-marketing | pending | MARKETING.md, CUSTOMER.md | |
| 2 | storybrand-messaging | pending | POSITIONING.md, WEBSITE.md | |
| 3 | made-to-stick | pending | POSITIONING.md, WEBSITE.md | |
| 4 | top-design | pending | DESIGN.md | |
| 5 | web-typography | pending | DESIGN.md | |
| 6 | refactoring-ui | pending | DESIGN.md | |
| 7 | ux-heuristics | pending | DESIGN.md | |
| 8 | cro-methodology | pending | WEBSITE.md, EXPERIMENTS.md | |
| 9 | scorecard-marketing | pending | WEBSITE.md, MARKETING.md | |
| 10 | steve-jobs-design-review | pending | WEBSITE.md | |
Statuses: pending · in-progress · awaiting-evidence · done · deferred: <reason> · skipped: <reason>

## Key Decisions
| Date | Phase | Decision | Rationale |
|---|---|---|---|

## Next Actions
- [ ] action (owner, due)
```

## docs/MARKETING.md

Created in Phase 1; `## Nurture Sequences` extended in Phase 9.

```markdown
# Marketing

## Target Market & Avatar
PVP niche choice · one-paragraph avatar.

## Before / During / After Grid
| Phase | Square | Current state | Plan |
|---|---|---|---|

## Channels
| Channel | Approach | Owner | Status |
|---|---|---|---|

## Word-of-Mouth (STEPPS)
| Lever | Idea | Status |
|---|---|---|

## Outbound Process
Roles, sequences, qualification, handoff.

## Referral & Invite Mechanics

## Nurture Sequences
```

## docs/POSITIONING.md

Created in Phase 2 (Brand Script, One-Liner, Key Messages). If the optional obviously-awesome phase runs first, it creates the file with the canvas sections above the messaging ones.

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

## docs/WEBSITE.md

Created in Phase 2 (Sitemap, Page Briefs); Conversion Elements added in Phase 8, Lead Capture in Phase 9, Audit Findings in Phases 7 and 10.

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

Created in Phase 4 (Design Direction); Typography added in Phase 5, Tokens + Components in Phase 6, UX Audit Findings in Phase 7.

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

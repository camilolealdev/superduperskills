---
name: spec-kit
description: >
  Spec-Driven Development (SDD) framework based on GitHub's official spec-kit
  (https://github.com/github/spec-kit). Enforces a specification-first approach
  where agents create executable specs, constitutions, technical architecture
  plans, and task breakdowns before writing code. Use whenever starting non-trivial
  features, architecture changes, new projects, or when user mentions "spec-kit",
  "spec driven", "speckit", "sdd", "/speckit.init", "/speckit.spec", or "write spec first".
argument-hint: "[init|constitution|spec|clarify|plan|tasks|implement|verify]"
license: MIT
---

# Spec Kit — Spec-Driven Development (SDD) for AI Agents

Based on GitHub's official [spec-kit](https://github.com/github/spec-kit), this skill enforces a **Spec-Driven Development** workflow. Code is an implementation detail of the specification; non-trivial features must always have a validated spec before execution starts.

## Core Philosophy

> "Never write code against ambiguous assumptions. Specify intent, constrain decisions in a constitution, break down verifiable tasks, then implement."

1. **Constitution First**: Define non-negotiables, technology stack constraints, and quality rules.
2. **Specification (PRD)**: Document user requirements, user stories, acceptance criteria, and edge cases.
3. **Clarification**: Interactively resolve underspecified constraints *before* architectural decisions are locked.
4. **Technical Implementation Plan (TRD)**: Map out system design, schema changes, API contracts, and component boundaries.
5. **Task Breakdown**: Partition implementation into isolated, verifiable work units with clear completion checks.
6. **Task-by-Task Implementation**: Execute sequentially following the spec.
7. **Verification**: Validate implementation against acceptance criteria.

---

## Slash Commands & Workflows

### 1. `/speckit.init`
Initializes SDD structure in the target project workspace:
- Creates `.speckit/` directory with `constitution.md`, `specs/`, and `plans/`.
- Registers project defaults and architecture constraints.

### 2. `/speckit.constitution`
Defines non-negotiable project principles:
- Code style, framework versions, state management rules.
- Performance ceilings, accessibility requirements, testing standards.
- Token & simplicity rules (pairing with `ponytail` and `caveman`).

### 3. `/speckit.spec [feature-name]`
Generates a Feature Requirement Specification (`.speckit/specs/[feature-name].md`):
- **Goal & Overview**: Why this feature exists and what value it delivers.
- **User Scenarios & Stories**: Concrete user interactions and expected behavior.
- **Acceptance Criteria**: Gherkin-style `Given-When-Then` assertions.
- **Edge Cases & Out-of-Scope**: Explicit boundaries to prevent scope creep.

### 4. `/speckit.clarify [feature-name]`
Audits the specification for ambiguities, missing data types, or conflicting requirements:
- Prompts key questions if requirements are incomplete.
- Updates the specification with clarified answers.

### 5. `/speckit.plan [feature-name]`
Generates Technical Implementation Plan (`.speckit/plans/[feature-name]-plan.md`):
- Data models & schemas (TypeScript types, DB tables, API payloads).
- Component hierarchy & module responsibilities.
- Security & error handling boundaries.
- Verification strategy (automated unit/integration test commands).

### 6. `/speckit.tasks [feature-name]`
Break down the plan into granular, ordered execution tasks:
```markdown
- [ ] Task 1: Data models & types (`src/types/feature.ts`)
- [ ] Task 2: Core business logic / backend handler (`src/services/feature.ts`)
- [ ] Task 3: Component UI layer (`src/components/FeatureView.tsx`)
- [ ] Task 4: Automated tests & manual verification
```

### 7. `/speckit.implement [task-id]`
Executes code changes for a single task:
- Consults `ponytail` for minimal working code (no unrequested abstractions).
- Writes unit self-check / test for non-trivial logic.
- Verifies task completion before proceeding to the next task.

### 8. `/speckit.verify [feature-name]`
Runs final verification against acceptance criteria:
- Executes test suite.
- Checks UI rendering / API responses.
- Generates completion summary.

---

## Integration with Core Agent Suite

- **Pair with `ponytail`**: When drafting specs and technical plans, use `ponytail` to choose the simplest architectural path (stdlib > native > existing deps > custom code).
- **Pair with `caveman`**: When rendering slash command outputs and spec summaries, keep prose terse and action-oriented.
- **Pair with `token-savings`**: Store specs in `.speckit/` files so session context stays lean rather than resending huge conversations.
- **Pair with `harness`**: Reference automated verification scripts in every technical plan.

---

## Quick Reference Table

| Stage | Command | Key Deliverable |
|-------|---------|-----------------|
| **0. Setup** | `/speckit.init` | `.speckit/constitution.md` |
| **1. Requirements** | `/speckit.spec [name]` | `.speckit/specs/[name].md` |
| **2. Clarify** | `/speckit.clarify [name]` | Resolved edge cases in spec |
| **3. Architecture** | `/speckit.plan [name]` | Technical Plan & Schemas |
| **4. Tasks** | `/speckit.tasks [name]` | Checklist of work items |
| **5. Build** | `/speckit.implement` | Clean, verifiable code edits |
| **6. Quality** | `/speckit.verify` | Test results & PR readiness |

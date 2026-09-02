---
name: angular-developer
description: >
  Generates Angular 18+ code and architectural guidance using Signals, Standalone Components, inject(), defer blocks,
  and RxJS interoperability. Use when building Angular apps, refactoring Angular components, or when user mentions
  "angular-developer", "angular signals", "standalone components", or "angular 18".
argument-hint: "[signals|standalone|defer|inject|rxjs]"
license: MIT
---

# Angular Developer — Modern Angular 18+ Guidance

Based on [affaan-m/angular-developer](https://skillrepo.dev/skills/affaan-m/angular-developer) (v1.1A), this skill guides modern Angular development.

## Core Patterns

- **Signals First**: Use `signal()`, `computed()`, and `effect()` for reactive state instead of raw RxJS Subjects where appropriate.
- **Standalone Architecture**: Prefer standalone components, directives, and pipes (`standalone: true`).
- **Deferred Loading**: Use `@defer (on viewport)` for automatic lazy loading of heavy UI components.

---
name: architecture-blueprint-generator
description: >
  Generates comprehensive architectural blueprints by scanning codebase dependencies, module boundaries, data flows,
  and deployment targets. Use when creating system architecture diagrams, onboarding docs, or when user mentions
  "architecture-blueprint-generator", "generate architecture blueprint", or "architecture overview".
argument-hint: "[scan|generate|mermaid|diagram]"
license: MIT
---

# Architecture Blueprint Generator — Automated System Blueprinting

Based on [github/architecture-blueprint-generator](https://skillrepo.dev/skills/github/architecture-blueprint-generator) (v1.0B), this skill scans a project to produce detailed technical blueprints and Mermaid diagrams.

## Output Components

- **Component Relationship Diagram**: Visualizes modules, HTTP endpoints, and database interactions using Mermaid.
- **Data Flow Mapping**: Traces request processing paths from ingress to storage.
- **Technology Matrix**: Summarizes languages, frameworks, ORMs, message queues, and cloud targets.

---
name: contract-first
description: >
  Contract-first API and event schema development pattern. Prevents field drift and breaking changes between frontend/backend
  or service providers by defining OpenAPI/TypeSpec/Protobuf contracts before coding. Use when designing API schemas,
  or when user mentions "contract-first", "contract first api", "typespec", or "openapi schema first".
argument-hint: "[openapi|typespec|protobuf|schema|drift]"
license: MIT
---

# Contract-First — Schema-Driven Development Workflow

Based on [affaan-m/contract-first](https://skillrepo.dev/skills/affaan-m/contract-first) (v1.0A), this skill enforces contract-first API development.

## Core Rules

- **Source of Truth**: The OpenAPI/TypeSpec document is the single authoritative contract (`api/spec.yaml`).
- **Code Generation**: Frontend SDKs and backend router interfaces are generated automatically from the spec (`npx @openapitools/openapi-generator-cli`).
- **Breaking Change Gate**: CI verifies schema diffs to block breaking parameter renames or type changes.

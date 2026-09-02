---
name: bun-runtime
description: >
  Guidance for using Bun as a runtime, package manager, bundler, and test runner. Explains Bun vs Node.js tradeoffs,
  native SQLite, Workspaces, and deployment. Use when working with Bun projects, configuring bun.lock, or when user
  mentions "bun-runtime", "bun test", "bun install", or "bun build".
argument-hint: "[runtime|package-manager|test|sqlite|bun.lock]"
license: MIT
---

# Bun Runtime — Fast JavaScript/TypeScript Runtime & Toolkit

Based on [affaan-m/bun-runtime](https://skillrepo.dev/skills/affaan-m/bun-runtime) (v1.2B), this skill guides performance-first JavaScript development using Bun.

## Performance Conventions

- **Fast Package Management**: Use `bun install` with frozen lockfile (`bun install --frozen-lockfile`) for CI.
- **Built-in Test Runner**: Replace Vitest/Jest with `bun test` for instant execution.
- **Native Modules**: Use `import { Database } from "bun:sqlite"` for local file-backed storage without native rebuilds.

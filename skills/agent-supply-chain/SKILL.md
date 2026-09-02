---
name: agent-supply-chain
description: >
  Verifies supply chain integrity for AI agent plugins, tools, and dependencies. Generates SHA-256 integrity manifests
  and audits third-party agent packages before installation. Use when verifying security of agent extensions, plugin safety,
  or when user mentions "agent-supply-chain", "supply chain integrity", "sha256 manifest", or "plugin audit".
argument-hint: "[verify|manifest|hash|audit]"
license: MIT
---

# Agent Supply Chain — Plugin Integrity & Security Audit

Based on [github/agent-supply-chain](https://skillrepo.dev/skills/github/agent-supply-chain) (v1.0A), this skill audits the supply chain of AI agent plugins, MCP servers, and skill packages.

## Integrity Verification

- **SHA-256 Manifest Generation**: Creates cryptographic hashes for all skill files and scripts.
- **Dependency Audit**: Verifies third-party npm/pip packages pulled by agent scripts.
- **Tamper Detection**: Compares installed skill files against published repository hashes.

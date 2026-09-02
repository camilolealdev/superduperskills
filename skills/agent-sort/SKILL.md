---
name: agent-sort
description: >
  Builds an evidence-backed ECC install plan for a repo by sorting skills, commands, rules, hooks, and extras into
  DAILY (frequent use) vs LIBRARY (on-demand) buckets. Use when organizing agent configurations, setting up new repos,
  or when user mentions "agent-sort", "sort skills", "ecc install plan", or "daily vs library".
argument-hint: "[sort|plan|daily|library]"
license: MIT
---

# Agent Sort — ECC Install Plan & Categorizer

Based on [affaan-m/agent-sort](https://skillrepo.dev/skills/affaan-m/agent-sort) (v1.2A), this skill categorizes tools, skills, rules, and hooks into **DAILY** (always loaded) vs **LIBRARY** (loaded on-demand) tiers.

## Categorization Strategy

- **DAILY Bucket**: High-frequency core skills (`caveman`, `ponytail`, `spec-kit`, `token-savings`, `harness`, `mem`, `rtk`, `graphify`).
- **LIBRARY Bucket**: Specialized, domain-specific skills (e.g. `dbsnp-database`, `openmontage`, `resemble-detect`).

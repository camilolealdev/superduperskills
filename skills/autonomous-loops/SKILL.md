---
name: autonomous-loops
description: >
  Patterns and architectures for autonomous Claude Code execution loops — from simple sequential pipelines to RFC-driven
  multi-agent DAG systems. Use when designing long-running agent workflows, setting up autonomous task loops, or when user
  mentions "autonomous-loops", "agent DAG loop", or "sequential execution loop".
argument-hint: "[dag|pipeline|rfc|loop]"
license: MIT
---

# Autonomous Loops — Task Loop Architectures for Agents

Based on [affaan-m/autonomous-loops](https://skillrepo.dev/skills/affaan-m/autonomous-loops) (v1.3A), this skill details execution loop topologies for AI agents.

## Loop Topologies

- **Sequential Pipeline**: Linear execution with state passed via JSON artifacts.
- **DAG Workflow**: Directed Acyclic Graph for parallel task execution with barrier sync points.
- **RFC-Driven Multi-Agent Loop**: RFC proposal step -> critique step -> implementation step -> verification step.

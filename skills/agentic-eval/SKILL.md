---
name: agentic-eval
description: >
  Patterns and techniques for evaluating and improving AI agent outputs. Implements self-critique, reflection loops,
  and quantitative evaluation suites. Use when building eval benchmarks, testing prompt changes, or when user mentions
  "agentic-eval", "eval suite", "self-critique", or "agent output evaluation".
argument-hint: "[benchmark|critique|reflection|eval]"
license: MIT
---

# Agentic Eval — Agent Evaluation & Reflection Framework

Based on [github/agentic-eval](https://skillrepo.dev/skills/github/agentic-eval) (v1.0A), this skill provides evaluation suites to measure accuracy, regression, and token efficiency of AI agent runs.

## Evaluation Workflows

- **Reflection Loops**: Agent re-reads output against specification requirements to score completeness.
- **Regression Benchmarking**: Runs standardized test suites across code changes to detect regressions.
- **Scorecards**: Generates quantitative reports rating code quality, test coverage, and token consumption.

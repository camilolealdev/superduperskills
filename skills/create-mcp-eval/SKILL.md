---
name: create-mcp-eval
description: >
  Generates comprehensive evaluation suites for any Model Context Protocol (MCP) server using @mcpjam/sdk.
  Supports Vitest/Jest integration, deterministic tool assertions, and LLM-as-a-judge test cases.
  Use when building eval tests for MCP servers, or when user mentions "create-mcp-eval", "mcp eval", or "mcpjam".
argument-hint: "[vitest|jest|assertions|mcp-server]"
license: MIT
---

# Create MCP Eval — MCP Server Test & Evaluation Framework

Based on [fauziyasin-s2m4qw/create-mcp-eval](https://skillrepo.dev/skills/fauziyasin-s2m4qw/create-mcp-eval) (v1.0A), this skill creates test suites for Model Context Protocol servers using `@mcpjam/sdk`.

## Eval Testing Workflow

1. **Tool Inventory**: Scans target MCP server definitions via `list_tools()`.
2. **Assertion Suite**: Generates input schema validation tests and error handling assertions.
3. **Execution Harness**: Runs Vitest/Jest against the MCP server in a subprocess sandbox.

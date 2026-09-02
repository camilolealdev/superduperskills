---
name: codebase-memory-mcp
description: >
  Indexes a codebase into a persistent knowledge graph so agents can query callers, callees,
  type hierarchies, and module relationships instead of re-reading dozens of files each session.
  Save tokens and accelerate context loading. Use when working on medium-to-large codebases,
  architectural refactoring, or when user mentions "codebase memory", "codebase-memory-mcp",
  "knowledge graph", "what calls what", or "graph indexing".
argument-hint: "[index|query|callers|dependencies|graph]"
license: MIT
---

# Codebase Memory MCP — Knowledge Graph Repo Indexer

Based on [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) (40k+ ★), this skill indexes repositories into a graph structure of symbols, imports, function calls, and type definitions.

## Key Benefits

- **Token Economy**: Instead of loading 40+ raw files into context to understand call flows, the agent queries the knowledge graph ("Who imports X?", "What functions depend on DB schema Y?").
- **Persistent Memory**: The index is maintained across sessions, preserving structural understanding of the repo.
- **Fast Navigation**: Provides structural traversal queries for complex multi-package codebases.

---

## Operating Commands

- **`index`**: Parses AST & imports to build/refresh the knowledge graph.
- **`query [symbol]`**: Returns symbol definition, file location, callers, and dependencies.
- **`callers [function]`**: Lists all functions and modules invoking the target function.
- **`graph-stats`**: Displays graph node count, edge density, and entrypoints.

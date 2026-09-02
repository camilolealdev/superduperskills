---
name: alloydb-basics
description: >
  Manages clusters, instances, and backups for Google Cloud AlloyDB for PostgreSQL, and integrates with AlloyDB MCP tools
  for automated database operations and vector search. Use when configuring AlloyDB, running PostgreSQL on GCP, or when user
  mentions "alloydb-basics", "alloydb", or "gcp postgresql".
argument-hint: "[cluster|instance|backup|vector|mcp]"
license: MIT
---

# AlloyDB Basics — GCP AlloyDB PostgreSQL Management

Based on [google/alloydb-basics](https://skillrepo.dev/skills/google/alloydb-basics) (v1.1C), this skill manages GCP AlloyDB clusters and PostgreSQL workloads.

## Core Operations

- **Cluster Provisioning**: Setup high-availability primary and read-pool instances.
- **pgvector Integration**: Configure vector index extensions (`pgvector`) for RAG embeddings.
- **Backup & Recovery**: Automate point-in-time recovery (PITR) policies and manual snapshots.

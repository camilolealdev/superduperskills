---
name: database-migrations
description: >
  Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments
  across PostgreSQL, MySQL, Prisma, Drizzle, and Flyway. Use when writing schema migrations, planning zero-downtime DB changes,
  or when user mentions "database-migrations", "zero downtime migration", "drizzle migration", or "prisma migrate".
argument-hint: "[zero-downtime|rollback|schema|drizzle|prisma]"
license: MIT
---

# Database Migrations — Zero-Downtime Schema Evolution

Based on [affaan-m/database-migrations](https://skillrepo.dev/skills/affaan-m/database-migrations) (v2.2A), this skill guides safe database migrations in production.

## Zero-Downtime Rule (Expand-Contract Pattern)

1. **Step 1 (Expand)**: Add new column as nullable or with default value (`ALTER TABLE users ADD COLUMN new_name text;`).
2. **Step 2 (Backfill & Dual Write)**: Deploy app code writing to both old and new columns.
3. **Step 3 (Contract)**: Drop old column after verifying all read traffic uses the new column.

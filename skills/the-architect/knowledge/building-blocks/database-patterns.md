# Building Block: Database Patterns

## Decision Matrix

| Database | Best For | Pros | Cons |
|----------|----------|------|------|
| **PostgreSQL (Supabase)** | SaaS, content, most apps | Full-featured, RLS, real-time, storage, auth included | Heavier than needed for simple apps |
| **PostgreSQL (Neon)** | Serverless, branching | Serverless scaling, DB branching for previews, generous free tier | Less integrated than Supabase |
| **MySQL (PlanetScale)** | High-scale, branching | Vitess-based, schema branching, no FK constraints (by design) | No foreign keys can be limiting |
| **SQLite (Turso)** | Edge, embedded, simple | Ultra-fast reads, edge replication, zero config | Not great for concurrent writes |
| **MongoDB** | Document-heavy, flexible schema | Schema flexibility, easy to start, Atlas free tier | Joins are painful, schema chaos at scale |
| **Redis (Upstash)** | Caching, sessions, queues | Serverless, fast, versatile | Not a primary database |

## ORM Decision Matrix

| ORM | Best For | Pros | Cons |
|-----|----------|------|------|
| **Prisma** | DX-focused, most projects | Best DX, great types, visual studio, migrations | Slower queries, large client bundle |
| **Drizzle** | Performance, SQL-like | SQL-like syntax, lightweight, fast | Less polished DX, newer ecosystem |
| **Kysely** | Type-safe raw SQL | Minimal abstraction, great types | More boilerplate, no migrations built-in |
| **Raw SQL** | Simple APIs, full control | No abstraction overhead | No type safety, manual everything |

## Schema Design Principles

### Naming Conventions
- Tables: plural, snake_case (`users`, `blog_posts`)
- Columns: snake_case (`created_at`, `user_id`)
- Foreign keys: `{table_singular}_id` (`user_id`, `post_id`)
- Indexes: `idx_{table}_{columns}` (`idx_posts_user_id`)

### Required Fields on Every Table
```sql
id          UUID PRIMARY KEY DEFAULT gen_random_uuid()
created_at  TIMESTAMPTZ DEFAULT now()
updated_at  TIMESTAMPTZ DEFAULT now()
```

### Soft Deletes (when appropriate)
```sql
deleted_at  TIMESTAMPTZ DEFAULT NULL
```
Use for: user data, billing records, audit-sensitive data
Don't use for: logs, temp data, high-volume tables

### Common Relationships
- **User → Resources**: One-to-many, FK `user_id` on resource table
- **Tags/Categories**: Many-to-many via junction table (`post_tags`)
- **Hierarchy**: Self-referential FK (`parent_id` on same table)
- **Polymorphic**: Avoid. Use separate tables or a type column + nullable FKs.

## Migration Strategy

### With Prisma
```bash
npx prisma migrate dev --name init    # Create migration
npx prisma generate                    # Generate client
npx prisma db push                     # Quick push (dev only)
npx prisma migrate deploy              # Production migration
```

### With Drizzle
```bash
npx drizzle-kit generate              # Generate SQL migration
npx drizzle-kit migrate               # Run migrations
npx drizzle-kit push                  # Quick push (dev only)
```

## Performance Patterns

- **Indexes**: Create indexes on all foreign keys and frequently filtered/sorted columns
- **Connection pooling**: Use connection pooler (Supabase has built-in, or use PgBouncer)
- **Query optimization**: Use `EXPLAIN ANALYZE` before shipping complex queries
- **Pagination**: Cursor-based for infinite scroll, offset-based for page numbers

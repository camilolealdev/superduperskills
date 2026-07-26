# Archetype: API / Backend Service

## Default Stack Recommendation

| Layer | Default | Alternative | When to Switch |
|-------|---------|-------------|----------------|
| Runtime | Node.js (Hono) | Python (FastAPI), Go | Python for ML/data, Go for high-performance |
| Language | TypeScript | Python, Go | Based on team/domain |
| Framework | Hono | Express, Fastify, NestJS | Express for simplicity, NestJS for enterprise |
| Database | PostgreSQL (Neon/Supabase) | MongoDB, SQLite | Mongo for document-heavy, SQLite for embedded |
| ORM | Drizzle | Prisma, TypeORM | Prisma for DX, TypeORM for NestJS |
| Validation | Zod | Joi, class-validator | class-validator with NestJS |
| Auth | JWT (jose library) | Passport.js, API keys only | Passport for OAuth, API keys for B2B |
| Queue | BullMQ + Redis | SQS, Inngest | SQS for AWS, Inngest for serverless |
| Caching | Redis (Upstash) | In-memory LRU | In-memory for single instance |
| Docs | OpenAPI/Swagger | — | Always generate API docs |
| Testing | Vitest | Jest | — |
| Hosting | Railway | Fly.io, AWS ECS, Vercel (Edge) | Fly for global, AWS for enterprise |
| Package Manager | pnpm | npm | — |

## Default Directory Structure

```
src/
  routes/
    auth/
      index.ts               # POST /auth/login, /auth/register, /auth/refresh
      middleware.ts           # Auth middleware
    users/
      index.ts               # GET/PATCH /users/:id
    [feature]/
      index.ts               # CRUD routes for feature
      schema.ts              # Zod validation schemas
      service.ts             # Business logic
    index.ts                 # Route aggregator
  middleware/
    auth.ts                  # JWT verification
    rateLimit.ts             # Rate limiting
    errorHandler.ts          # Global error handler
    logger.ts                # Request logging
  db/
    schema.ts                # Drizzle schema definitions
    migrations/              # SQL migrations
    index.ts                 # Database client
    seed.ts                  # Seed data
  services/
    email.ts                 # Email sending (Resend)
    queue.ts                 # Job queue (BullMQ)
    cache.ts                 # Cache layer (Redis)
  lib/
    env.ts                   # Environment variable validation (zod)
    errors.ts                # Custom error classes
    utils.ts                 # Shared utilities
  types/
    index.ts                 # Shared types
  index.ts                   # App entry point
tests/
  routes/                    # Route integration tests
  services/                  # Service unit tests
  helpers/                   # Test utilities
drizzle.config.ts            # Drizzle Kit config
```

## Common Patterns

### Route Structure (Hono)
```typescript
// Each route file exports a Hono app
const app = new Hono()
  .get('/', listHandler)
  .get('/:id', getHandler)
  .post('/', createHandler)
  .patch('/:id', updateHandler)
  .delete('/:id', deleteHandler)
export default app
```

### Error Handling
- Custom error classes: `NotFoundError`, `ValidationError`, `UnauthorizedError`
- Global error middleware catches all, returns consistent JSON shape:
  `{ success: false, error: { code, message, details? } }`

### API Response Shape
```json
{
  "success": true,
  "data": { ... },
  "meta": { "page": 1, "total": 100 }
}
```

### Auth
- Login returns access token (15min) + refresh token (7d)
- Access token in Authorization header: `Bearer <token>`
- Refresh token in httpOnly cookie
- Auth middleware decodes token, attaches `ctx.user`

## Build Order

1. **Scaffolding**: Init project, TypeScript config, install Hono + Drizzle + Zod
2. **Config**: Environment validation with Zod, logger setup
3. **Database**: Schema definition, migration setup, database client
4. **Error handling**: Custom error classes, global error middleware
5. **Auth routes**: Register, login, refresh, auth middleware
6. **Core feature routes**: CRUD for the primary entity
7. **Validation**: Zod schemas for all inputs, middleware integration
8. **Background jobs** (if needed): BullMQ setup, worker process
9. **Caching** (if needed): Redis cache layer for hot paths
10. **API docs**: OpenAPI spec generation, Swagger UI
11. **Testing**: Integration tests for routes, unit tests for services
12. **Deploy**: Railway/Fly config, health check endpoint, monitoring

## Common Pitfalls

- **Don't skip input validation.** Every route input must be validated with Zod. No exceptions.
- **Don't return raw database errors.** Map them to user-friendly messages.
- **Don't forget rate limiting.** Add it from day one on auth routes at minimum.
- **Don't hardcode secrets.** All config via environment variables, validated at startup.
- **Don't skip health checks.** `/health` endpoint for load balancers and monitoring.

## Skills for Build Phase

| Skill | When |
|-------|------|
| `/deep-research` | Comparing API frameworks or infra choices |

## See Also

- `knowledge/building-blocks/api-design-patterns.md` — REST conventions, response shapes, validation
- `knowledge/building-blocks/database-patterns.md` — Schema design, Drizzle setup, migrations
- `knowledge/building-blocks/auth-patterns.md` — JWT patterns, API key auth
- `knowledge/building-blocks/deployment-patterns.md` — Railway, Fly.io, Docker config
- `knowledge/building-blocks/testing-patterns.md` — Integration tests for every endpoint

# Building Block: API Design Patterns

## Decision Matrix

| Style | Best For | Pros | Cons |
|-------|----------|------|------|
| **REST** | Public APIs, simple CRUD | Universal, cacheable, tooling | Over/under-fetching, versioning pain |
| **tRPC** | Full-stack TypeScript (same repo) | End-to-end type safety, no code generation | TypeScript only, same repo required |
| **GraphQL** | Complex data, multiple clients | Flexible queries, one endpoint | Complexity, N+1 problems, over-engineering for most apps |
| **Server Actions** | Next.js forms/mutations | Zero API boilerplate, progressive enhancement | Next.js only, not for external consumers |

## Recommendation by Project Type

| Project | Recommended |
|---------|-------------|
| SaaS (Next.js monorepo) | **Server Actions** for mutations + **tRPC** for complex queries |
| SaaS (separate frontend/backend) | **REST** |
| Public API / B2B | **REST** with OpenAPI docs |
| Mobile + Web consuming same API | **REST** |
| Internal tool | **Server Actions** (simplest) |
| Complex data relationships | **GraphQL** (only if genuinely needed) |

## REST Conventions

### URL Structure
```
GET    /api/resources              # List (with pagination, filters)
POST   /api/resources              # Create
GET    /api/resources/:id          # Get one
PATCH  /api/resources/:id          # Update (partial)
DELETE /api/resources/:id          # Delete

GET    /api/resources/:id/children # Nested resources
POST   /api/resources/:id/actions  # Custom actions
```

### Response Shape (Consistent Across All Endpoints)
```json
// Success
{
  "success": true,
  "data": { ... },
  "meta": { "page": 1, "pageSize": 20, "total": 142 }
}

// Error
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": [{ "field": "email", "message": "Required" }]
  }
}
```

### HTTP Status Codes
| Code | When |
|------|------|
| 200 | Success (GET, PATCH) |
| 201 | Created (POST) |
| 204 | No content (DELETE) |
| 400 | Validation error |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Not found |
| 409 | Conflict (duplicate) |
| 429 | Rate limited |
| 500 | Server error |

### Pagination
```
GET /api/resources?page=1&pageSize=20        # Offset-based
GET /api/resources?cursor=abc123&limit=20     # Cursor-based (preferred for infinite scroll)
```

### Filtering & Sorting
```
GET /api/resources?status=active&sort=-created_at&search=keyword
```

## tRPC Patterns (Next.js)
```
- server/trpc.ts: create tRPC instance + context
- server/routers/: one router per domain
- server/routers/_app.ts: merge all routers
- app/api/trpc/[trpc]/route.ts: HTTP handler
- lib/trpc/client.ts: client-side hooks
- lib/trpc/server.ts: server-side caller
```

## Input Validation

Always validate ALL inputs with Zod:
```typescript
const createSchema = z.object({
  name: z.string().min(1).max(255),
  email: z.string().email(),
  role: z.enum(['admin', 'member', 'viewer']).default('member'),
})
```

Apply validation at the API boundary, not deep in business logic.

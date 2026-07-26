# Building Block: Authentication Patterns

## Decision Matrix

| Solution | Best For | Pros | Cons | Cost |
|----------|----------|------|------|------|
| **Clerk** | SaaS, fast MVP | Beautiful UI, social logins, orgs, webhooks, Expo SDK | Vendor lock-in, costs at scale | Free to 10k MAU |
| **NextAuth v5** | Full control | Open source, any provider, self-hosted | More setup, DIY UI, no org support | Free |
| **Supabase Auth** | Already using Supabase | Integrated with DB, Row Level Security, magic links | Less polished UI, fewer social providers | Free with Supabase |
| **Firebase Auth** | Mobile-first, Google ecosystem | Great mobile SDKs, phone auth, anonymous auth | Google lock-in, Firestore coupling | Free to 50k MAU |
| **Lucia** | Custom, lightweight | Full control, any DB, no vendor | DIY everything, discontinued (use Auth.js) | Free |
| **API Keys** | B2B APIs | Simple, stateless | No user management, no sessions | Free |
| **JWT (custom)** | Microservices, APIs | Stateless, cross-service | Must handle refresh, revocation, storage | Free |

## Implementation Patterns

### Clerk (Recommended for SaaS)
```
Install: @clerk/nextjs
- ClerkProvider wraps app in root layout
- middleware.ts: clerkMiddleware() protects routes
- Server: auth() returns userId, session
- Client: useAuth(), useUser(), SignIn/SignUp components
- Webhooks: /api/webhooks/clerk for user sync to database
```

### NextAuth v5 (Recommended for full control)
```
Install: next-auth@beta
- auth.ts: configure providers (Google, GitHub, credentials)
- middleware.ts: auth middleware from next-auth
- Server: auth() from auth.ts
- Client: SessionProvider + useSession()
- Database adapter: @auth/prisma-adapter or @auth/drizzle-adapter
```

### Supabase Auth (Recommended when using Supabase)
```
Install: @supabase/ssr
- lib/supabase/client.ts: browser client
- lib/supabase/server.ts: server client (cookies)
- middleware.ts: refresh session on every request
- RLS policies on tables for row-level authorization
- Auth UI: @supabase/auth-ui-react or custom
```

## Common Auth Requirements

### Protected Routes
- Next.js middleware for route protection (runs on edge, fast)
- Define public routes as allowlist, protect everything else
- Redirect to login with returnUrl parameter

### Roles & Permissions
- Store role in user metadata or separate roles table
- Middleware checks role for admin routes
- Component-level: `if (user.role !== 'admin') return null`
- API-level: validate role in route handler before processing

### Session Management
- **Cookie-based** (recommended for web): httpOnly, secure, SameSite
- **JWT** (for APIs): short-lived access token (15min) + longer refresh token (7d)
- **Refresh flow**: silent refresh before expiry, redirect to login on failure

### Social Login Providers
- Minimum: Google + GitHub (covers most developers)
- Consumer apps: Google + Apple (Apple required for iOS if offering social login)
- Enterprise: Google + Microsoft (covers corporate accounts)

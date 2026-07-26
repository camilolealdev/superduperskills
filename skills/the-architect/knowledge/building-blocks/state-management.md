# Building Block: State Management

## Decision Matrix

| Solution | Best For | Type | Complexity |
|----------|----------|------|-----------|
| **React Server Components** | Data display | Server state | None (built-in) |
| **Server Actions** | Form mutations | Server state | None (built-in) |
| **TanStack Query** | Client-side server state | Server cache | Low |
| **SWR** | Simple data fetching | Server cache | Low |
| **Zustand** | Client-only UI state | Client state | Low |
| **Jotai** | Atomic state, fine-grained | Client state | Low |
| **Redux Toolkit** | Large teams, complex state | Client state | Medium |
| **Supabase Realtime** | Live data | Real-time | Low |
| **Socket.io** | Custom real-time | Real-time | Medium |

## Recommendation: The Default Stack

For most Next.js projects, use this combination:

1. **Server Components** for data display (no state management needed)
2. **Server Actions** for mutations (forms, create/update/delete)
3. **TanStack Query** when client components need server data (polling, optimistic updates)
4. **Zustand** for UI-only state (sidebar open, modal state, theme, filters)

This covers 99% of use cases without over-engineering.

## When You DON'T Need State Management

- **Data that Server Components can fetch directly** → Just fetch in the component
- **Form state** → React Hook Form or native form elements
- **URL state** (filters, pagination) → `useSearchParams` + `nuqs` library
- **Theme** → CSS media query + `next-themes`
- **Auth state** → Clerk's `useAuth()` or NextAuth's `useSession()`

## Implementation Patterns

### Server Components (Default)
```typescript
// No state management — just fetch and render
async function Dashboard() {
  const stats = await db.query.stats.findFirst()
  const posts = await db.query.posts.findMany({ limit: 10 })
  return <DashboardView stats={stats} posts={posts} />
}
```

### Server Actions (Mutations)
```typescript
async function createPost(formData: FormData) {
  'use server'
  const data = schema.parse(Object.fromEntries(formData))
  await db.insert(posts).values(data)
  revalidatePath('/posts')
}
```

### TanStack Query (Client-Side Server State)
```typescript
'use client'
// Use when client needs to: poll, optimistically update, or cache across navigations
const { data, isLoading } = useQuery({
  queryKey: ['posts', filters],
  queryFn: () => fetch(`/api/posts?${params}`).then(r => r.json()),
  refetchInterval: 30000, // poll every 30s
})
```

### Zustand (Client UI State)
```typescript
// Small, focused stores — one per concern
const useSidebarStore = create<SidebarState>((set) => ({
  isOpen: true,
  toggle: () => set((s) => ({ isOpen: !s.isOpen })),
}))
```

## Real-Time Patterns

### When You Need Real-Time
- Chat / messaging
- Live collaboration (multiple users editing)
- Live dashboards (stock prices, monitoring)
- Notifications (in-app, not push)

### When You DON'T Need Real-Time
- Regular dashboards (poll every 30-60s instead)
- Social feeds (pull-to-refresh is fine)
- Admin panels (manual refresh button)

### Supabase Realtime (Recommended)
```typescript
const channel = supabase
  .channel('room1')
  .on('postgres_changes', { event: '*', schema: 'public', table: 'messages' },
    (payload) => addMessage(payload.new))
  .subscribe()
```

### Alternatives
- **Pusher / Ably**: Managed WebSocket service, easy setup
- **Socket.io**: Self-hosted, more control, more ops
- **Server-Sent Events**: One-way server→client, simpler than WebSocket

# Building Block: Testing Patterns

## Decision Matrix

| Type | Tool | What to Test | When |
|------|------|-------------|------|
| **Unit** | Vitest | Pure functions, utilities, hooks | Always |
| **Integration** | Vitest + Testing Library | Components with state, API routes | Production apps |
| **E2E** | Playwright | Critical user flows | Production apps |
| **API** | Vitest + supertest/fetch | API endpoints end-to-end | Backend projects |

## Recommendation by Project Type

| Project | Testing Approach |
|---------|-----------------|
| MVP / Prototype | Skip tests. Ship fast. Add later. |
| SaaS (production) | Unit + E2E for critical paths (auth, payments, core feature) |
| API / Backend | Integration tests for every endpoint, unit for business logic |
| Marketing Site | E2E smoke test (pages load, forms submit) |
| Internal Tool | E2E for core workflows |
| Mobile App | Unit + Detox/Maestro for critical flows |

## Vitest Setup (Recommended for all JS/TS projects)

```bash
pnpm add -D vitest @testing-library/react @testing-library/jest-dom jsdom
```

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    setupFiles: ['./tests/setup.ts'],
    globals: true,
  },
})
```

## Playwright Setup (E2E)

```bash
pnpm add -D @playwright/test
npx playwright install
```

### What to E2E Test (Priority Order)
1. **Auth flow**: Sign up → login → protected page → logout
2. **Core feature**: Create → view → edit → delete the main entity
3. **Payments** (if applicable): Pricing → checkout → subscription active
4. **Happy path**: The #1 thing users do, end to end

### What NOT to E2E Test
- Styling, layout, visual details (use visual regression if needed)
- Error states you can unit test
- Third-party service behavior
- Every permutation of filters/sorting

## Testing Principles

1. **Test behavior, not implementation.** Test what the user sees and does, not internal state.
2. **Prioritize by risk.** Test the paths where bugs cost the most (auth, payments, data loss).
3. **Fast tests > many tests.** A suite that takes 30 seconds gets run. One that takes 10 minutes doesn't.
4. **No mocking databases in integration tests.** Use a real test database. Docker Compose or test containers.
5. **E2E tests run in CI.** Never skip them before deploy.

## File Organization

```
tests/
  unit/                  # Pure function tests
    utils.test.ts
  integration/           # Component + API tests
    api/
      users.test.ts
    components/
      Dashboard.test.tsx
  e2e/                   # Playwright E2E
    auth.spec.ts
    core-feature.spec.ts
  fixtures/              # Test data factories
    users.ts
  setup.ts               # Global test setup
```

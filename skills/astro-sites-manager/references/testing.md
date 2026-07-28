# Testing Astro Projects

Complete guide for testing Astro projects — from unit/component tests to E2E, link checking, type safety, and CI pipelines.

---

## 1. Component Testing with Vitest

### Setup

```bash
npm install -D vitest @vitest/ui
```

### vitest.config.ts

```ts
/// <reference types="vitest" />
import { getViteConfig } from 'astro/config';

export default getViteConfig({
  test: {
    include: ['tests/**/*.{test,spec}.{js,ts}'],
  },
});
```

### AstroContainer API

The `AstroContainer` API renders Astro components in isolation without a full dev server.

```ts
import { experimental_AstroContainer as AstroContainer } from 'astro/container';
import { expect, test } from 'vitest';
import Greeting from '../src/components/Greeting.astro';

test('renders greeting with name prop', async () => {
  const container = await AstroContainer.create();
  const result = await container.renderToString(Greeting, {
    props: { name: 'World' },
  });

  expect(result).toContain('Hello, World');
});
```

### Testing Props

```ts
test('renders default when no name provided', async () => {
  const container = await AstroContainer.create();
  const result = await container.renderToString(Greeting, {
    props: {},
  });

  expect(result).toContain('Hello, stranger');
});
```

### Testing Slots

```ts
import Card from '../src/components/Card.astro';

test('renders slot content', async () => {
  const container = await AstroContainer.create();
  const result = await container.renderToString(Card, {
    slots: { default: '<p>Slot content here</p>' },
  });

  expect(result).toContain('Slot content here');
});
```

### Testing Conditional Rendering

```ts
import Alert from '../src/components/Alert.astro';

test('renders error variant', async () => {
  const container = await AstroContainer.create();
  const result = await container.renderToString(Alert, {
    props: { type: 'error', message: 'Something failed' },
  });

  expect(result).toContain('class="alert-error"');
  expect(result).toContain('Something failed');
});

test('does not render when hidden', async () => {
  const container = await AstroContainer.create();
  const result = await container.renderToString(Alert, {
    props: { type: 'info', message: 'Hidden', visible: false },
  });

  expect(result).not.toContain('Hidden');
});
```

### Run Tests

```bash
npx vitest
npx vitest --ui  # browser UI
```

---

## 2. E2E Testing with Playwright

### Setup

```bash
npm install -D @playwright/test
npx playwright install
```

### playwright.config.ts

```ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  webServer: {
    command: 'npm run preview',
    port: 4321,
    reuseExistingServer: !process.env.CI,
  },
  use: {
    baseURL: 'http://localhost:4321',
  },
});
```

> **Note:** Run `astro build` before E2E tests so `preview` has something to serve.

### Example: Page Load

```ts
import { test, expect } from '@playwright/test';

test('homepage loads correctly', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/My Site/);
  await expect(page.locator('h1')).toBeVisible();
});
```

### Example: Navigation

```ts
test('navigates to about page', async ({ page }) => {
  await page.goto('/');
  await page.click('a[href="/about"]');
  await expect(page).toHaveURL('/about');
  await expect(page.locator('h1')).toContainText('About');
});
```

### Example: Dynamic Routes

```ts
test('blog post renders from content collection', async ({ page }) => {
  await page.goto('/blog/first-post');
  await expect(page.locator('article h1')).toBeVisible();
  await expect(page.locator('article')).not.toBeEmpty();
});
```

### Testing View Transitions

```ts
test('view transitions work between pages', async ({ page }) => {
  await page.goto('/');
  const transitionPromise = page.waitForEvent('load');
  await page.click('a[href="/about"]');
  await transitionPromise;
  await expect(page).toHaveURL('/about');
});
```

### Run E2E Tests

```bash
npx astro build
npx playwright test
npx playwright test --ui  # interactive mode
```

---

## 3. Link Checking

### linkinator

Checks all links in the built output for broken references.

```bash
npx astro build
npx linkinator dist --recurse
```

Options:

```bash
npx linkinator dist --recurse --skip "^https://external-site.com"
```

### CI Integration (GitHub Actions)

```yaml
- name: Check links
  run: npx linkinator dist --recurse --retry --retry-errors
```

---

## 4. Type Checking

### Astro Template Validation

```bash
npx astro check
```

Validates `.astro` files for type errors in expressions, prop types, and component usage.

### TypeScript Checking

```bash
npx tsc --noEmit
```

Validates all `.ts` and `.tsx` files without emitting output.

### package.json Scripts

```json
{
  "scripts": {
    "check": "astro check && tsc --noEmit"
  }
}
```

---

## 5. Content Collection Validation

### Schema Enforcement

Content collections validate against Zod schemas at build time. Invalid content **fails the build automatically**:

```ts
// src/content.config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.date(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
```

A frontmatter error produces:

```
[ERROR] blog → "bad-post.md" frontmatter does not match schema.
  "title" is required.
```

### Draft Filtering

Filter drafts in production queries:

```astro
---
import { getCollection } from 'astro:content';

const posts = await getCollection('blog', ({ data }) => {
  return import.meta.env.PROD ? !data.draft : true;
});
---
```

Test that drafts are excluded by checking the built output does not contain draft post URLs.

---

## 6. Pre-Deploy Verification Script

Save as `scripts/verify.sh`:

```bash
#!/bin/bash
set -e

echo "→ Type checking..."
npx astro check

echo "→ Building..."
npx astro build

echo "→ Checking links..."
npx linkinator dist --recurse

echo "→ Running E2E tests..."
npx playwright test

echo "✓ All checks passed"
```

```bash
chmod +x scripts/verify.sh
./scripts/verify.sh
```

---

## 7. CI Pipeline (GitHub Actions)

Save as `.github/workflows/test.yml`:

```yaml
name: Test

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - run: npm ci

      - name: Type check
        run: npx astro check && npx tsc --noEmit

      - name: Build
        run: npx astro build

      - name: Component tests
        run: npx vitest run

      - name: Install Playwright
        run: npx playwright install --with-deps chromium

      - name: E2E tests
        run: npx playwright test

      - name: Link check
        run: npx linkinator dist --recurse --retry

      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Component tests | `npx vitest` |
| E2E tests | `npx playwright test` |
| Type check | `npx astro check && tsc --noEmit` |
| Link check | `npx linkinator dist --recurse` |
| Full verification | `./scripts/verify.sh` |

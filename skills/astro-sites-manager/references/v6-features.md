# Astro v6 Features (still current in v7)

These features were introduced or stabilized in Astro v6 and remain fully supported in v7.

---

## 1. Content Collections v2

Type-safe content management with Zod schemas and flexible data loaders.

```ts
// content.config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
```

**Loaders:**
- `file()` — single file (JSON, YAML)
- `glob()` — match files by pattern
- Custom loaders — fetch from CMS at build or request time (live collections)

**Querying:**
```ts
import { getCollection, getEntry } from 'astro:content';

const posts = await getCollection('blog', ({ data }) => !data.draft);
const post = await getEntry('blog', 'my-post');
```

---

## 2. Server Actions

Type-safe RPC endpoints with Zod validation.

```ts
// src/actions/index.ts
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';

export const server = {
  subscribe: defineAction({
    input: z.object({ email: z.string().email() }),
    handler: async ({ email }) => {
      // process subscription
      return { success: true };
    },
  }),
};
```

**Usage in components:**
```ts
import { actions } from 'astro:actions';

const result = await actions.subscribe({ email: 'user@example.com' });
```

**Form integration with progressive enhancement:**
```astro
<form method="POST" action={actions.subscribe}>
  <input type="email" name="email" />
  <button type="submit">Subscribe</button>
</form>
```

---

## 3. Sessions

Server-side session management with pluggable drivers.

**Config:**
```js
// astro.config.mjs
export default defineConfig({
  session: {
    driver: 'cookie', // also: node-fs, redis, etc.
  },
});
```

**Usage:**
```ts
// In pages/endpoints
const user = await Astro.session.get('user');
await Astro.session.set('user', { name: 'Alice' });

// In middleware
const user = await context.session.get('user');
```

---

## 4. Server Islands

Defer component rendering to request time while keeping the page static.

```astro
---
import UserGreeting from '../components/UserGreeting.astro';
---
<UserGreeting server:defer />
```

- Placeholder rendered at build time
- Component fetched and rendered at request time
- Perfect for personalized content in otherwise static pages

---

## 5. Environment Variables (astro:env)

Type-safe, validated environment variables.

```ts
import { MY_SECRET } from 'astro:env/server';
import { PUBLIC_API_URL } from 'astro:env/client';
```

**Schema definition:**
```js
// astro.config.mjs
export default defineConfig({
  env: {
    schema: {
      MY_SECRET: envField.string({ context: 'server', access: 'secret' }),
      PUBLIC_API_URL: envField.string({ context: 'client', access: 'public' }),
    },
  },
});
```

Variables are validated at build time — missing or invalid values cause build failures.

---

## 6. On-Demand Rendering

Hybrid static/SSR on a per-page basis.

```astro
---
// This page renders on every request
export const prerender = false;
---
```

**Adapters:**
- `@astrojs/node`
- `@astrojs/cloudflare`
- `@astrojs/netlify`
- `@astrojs/vercel`

**Hybrid mode:** static by default, opt individual pages into SSR with `prerender = false`.

---

## 7. View Transitions

Client-side navigation with animated transitions between pages.

```astro
---
import { ViewTransitions } from 'astro:transitions';
---
<head>
  <ViewTransitions />
</head>

<h1 transition:name="title" transition:animate="slide">Hello</h1>
<div transition:persist>
  <!-- State preserved across navigation -->
</div>
```

**Lifecycle events:**
- `astro:before-preparation`
- `astro:after-swap`
- `astro:page-load`

---

## 8. Middleware

Request/response pipeline with access to context.

```ts
// src/middleware.ts
import { defineMiddleware, sequence } from 'astro:middleware';

const auth = defineMiddleware(async (context, next) => {
  const token = context.cookies.get('token');
  context.locals.user = await validateToken(token?.value);
  return next();
});

const logging = defineMiddleware(async (context, next) => {
  console.log(context.url.pathname);
  return next();
});

export const onRequest = sequence(auth, logging);
```

Access to `context.locals`, `context.cookies`, `context.redirect()`.

---

## 9. Image Optimization

Built-in image processing with automatic optimization.

```astro
---
import { Image } from 'astro:assets';
import hero from '../assets/hero.png';
---
<Image src={hero} alt="Hero" width={800} />
```

- Automatic format conversion, lazy loading, responsive sizes
- Remote images configured via `image.domains` and `image.remotePatterns`:

```js
// astro.config.mjs
export default defineConfig({
  image: {
    domains: ['cdn.example.com'],
    remotePatterns: [{ protocol: 'https', hostname: '**.example.com' }],
  },
});
```

---

## 10. Internationalization (i18n)

Built-in i18n routing with locale-aware URL generation.

```js
// astro.config.mjs
export default defineConfig({
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'pt-br', 'es'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
```

**URL generation:**
```ts
import { getRelativeLocaleUrl } from 'astro:i18n';

getRelativeLocaleUrl('pt-br', '/about'); // → /pt-br/about
```

**Strategies:** pathname prefixes or domain-based routing.

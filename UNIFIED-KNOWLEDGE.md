# UNIFIED KNOWLEDGE — Multi-Taxonomy Skill Graph

> Fusión de todos los skills de todos los repositorios en un único sistema multi-conocimiento.
> Cada skill pertenece a una o más **áreas de conocimiento**, permitiendo búsqueda
> multidimensional. Skills duplicadas se marcan con `[dup:N]` y se listan sus fuentes.

> **Nota de vigencia:** esta taxonomía se curó a mano sobre una foto de **402** skills y
> referencia rutas de una máquina anterior (p. ej. `Documents/.opencode/skills/`). El repo
> ahora bundlea **1180** skills — usa [`SKILLS-INDEX.md`](SKILLS-INDEX.md) (auto-regenerado por
> `build_index.py`) como fuente de verdad actual para conteo, rutas y GitHub de origen.

---

## Mapa de Duplicados

Skills que aparecen en MÚLTIPLES repositorios:

| Skill | Repos | Nota |
|-------|-------|------|
| ui-ux-pro-max | `Documents/.opencode/skills/`, `Documents/.codex/skills/`, `edhorizonte/.opencode/skills/` | Copias idénticas en 3 lugares |
| nodejs-best-practices | `Documents/.agents/skills/`, `.continue/skills/`, `.codebuddy/skills/` | 3 copias |
| nodejs-backend-patterns | `Documents/.agents/skills/`, `.continue/skills/`, `.codebuddy/skills/` | 3 copias |
| design-system | `ui-ux-pro-max` (CKM), `frontend-jezweb` | Diferentes: uno es token architecture, otro es extractor |
| meta-optimizer | `seo-ccforseo`, `seo-geo` | Similar: títulos + meta descriptions |
| content-brief | `seo-ccforseo`, `seo-content-writer` (indirecto) | Brief vs writer |
| schema (gen) | `seo`, `seo-geo`, `seo-agrici`, `skills` | 4 fuentes para schema markup |
| internal-links | `seo-ccforseo`, `seo-geo (linking-optimizer)` | Mismo propósito, 2 implementaciones |
| keyword-research/cluster | `seo-geo`, `seo-ccforseo` | Complementarios |
| ai-seo / seo-geo / geo-content-optimizer / ai-visibility | 4 skills diferentes que tocan GEO | El más completo es `seo-geo` de seo-agrici |
| containers ln-731 vs docker skill | `backend-arch`, `skills (standalone)` | Docker skill es standalone helper |

---

## 1. FRONTEND — Conocimiento

### 1.1 React Ecosystem

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| react-expert | `backend-skills` | react, ssr, hooks, suspense | React 18+ components, Server Components |
| react-patterns | `frontend-jezweb` | react, perf, composition | React 19 perf, re-render prevention |
| nextjs-developer | `backend-skills` | nextjs, app-router, rsc, ssr | Next.js 14+ App Router, Server Actions |
| vercel-react-best-practices | `skills` | react, nextjs, vercel, perf | React/Next.js perf from Vercel Engineering |

### 1.2 UI Components & Styling

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| shadcn-ui | `frontend-jezweb` | radix, tailwind, components | shadcn/ui component install & config |
| tailwind-theme-builder | `frontend-jezweb` | tailwind, css, theme, shadcn | Tailwind v4 + shadcn/ui themed setup |
| ckm:ui-styling | `ui-ux-pro-max` | radix, tailwind, accessible | shadcn/ui + Radix accessible UIs |
| tailwind (HF) | `skills` | tailwind, hyperframes, runtime | Tailwind v4 browser-runtime in HyperFrames |

### 1.3 Design Systems & Tokens

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| design-system (CKM) | `ui-ux-pro-max` | tokens, architecture, specs | Token architecture, component specs |
| design-system (jezweb) | `frontend-jezweb` | extract, audit, reverse-engineer | Extract design system from website/screenshot |
| normalize | `impeccable` | alignment, tokens, consistency | Realign UI to design system standards |
| extract | `impeccable` | tokens, components, reuse | Extract components/tokens into design system |
| color-palette | `frontend-jezweb` | color, accessibility, tailwind | Accessible palettes from brand hex |
| icon-set-generator | `frontend-jezweb` | svg, icons, design | Cohesive SVG icon packs |
| favicon-gen | `frontend-jezweb` | favicon, branding, manifest | All favicon formats from logo/text/brand |

### 1.4 Design Enhancement (Impeccable Suite)

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| teach-impeccable | `impeccable` | setup, context | One-time design context setup |
| frontend-design | `impeccable` | design, production, creative | Production-grade interfaces, no generic AI |
| bolder | `impeccable` | amplify, impact, character | Amplify safe/boring designs |
| quieter | `impeccable` | tame, refine, calm | Tone down aggressive designs |
| distill | `impeccable` | simplify, reduce, essence | Strip to essence, remove complexity |
| colorize | `impeccable` | color, vibrancy, warmth | Add strategic color to monochrome UIs |
| typeset | `impeccable` | typography, hierarchy, fonts | Fix typography hierarchy & readability |
| arrange | `impeccable` | layout, spacing, rhythm | Fix layout, spacing, visual rhythm |
| animate | `impeccable` | motion, micro-interactions | Purposeful animations & micro-interactions |
| delight | `impeccable` | joy, personality, polish | Moments of joy, personality |
| polish | `impeccable` | finish, detail, ship-ready | Final quality pass before shipping |
| overdrive | `impeccable` | shaders, physics, 60fps | Technically ambitious animations |
| clarify | `impeccable` | ux-copy, labels, errors | Improve UX copy, error messages |
| harden | `impeccable` | i18n, errors, edge-cases | Error handling, i18n, edge cases |
| adapt | `impeccable` | responsive, breakpoints, mobile | Responsive design, fluid layouts |
| critique | `impeccable` | evaluate, score, feedback | UX evaluation with quantitative scoring |
| audit (impeccable) | `impeccable` | a11y, perf, anti-patterns | WCAG a11y, perf, theming audit |
| optimize (impeccable) | `impeccable` | perf, bundle, slow | UI perf: loading, rendering, animations |

### 1.5 Brand & Visual Identity

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| ckm:brand | `ui-ux-pro-max` | voice, identity, messaging | Brand voice, visual identity, guidelines |
| ckm:banner-design | `ui-ux-pro-max` | banners, social, ads, 22-styles | Social/ads/web/print banners |
| ckm:slides | `ui-ux-pro-max` | presentations, chartjs | HTML presentations with Chart.js |
| ui-ux-pro-max | `Documents/.opencode/skills/` [dup:3] | design, database, reference | UI/UX design intelligence database |

### 1.6 Mobile

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| react-native | `frontend-jezweb` | rn, expo, reanimated, navigation | RN/Expo perf, animations |
| react-native-expert | `backend-skills` | rn, expo, native, flatlist | RN/Expo, native modules, platform code |
| flutter-expert | `backend-skills` | flutter, dart, riverpod, bloc | Flutter 3+ cross-platform |

### 1.7 Vue / Angular / Alternative

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| vue-expert | `backend-skills` | vue3, nuxt, pinia, vite | Vue 3 Composition API, Nuxt 3 |
| vue-expert-js | `backend-skills` | vue3, js-only, jsdoc | Vue 3 with JavaScript (no TypeScript) |
| angular-architect | `backend-skills` | angular17, ngrx, rxjs | Angular 17+ standalone, NgRx state |

---

## 2. BACKEND — Conocimiento

### 2.1 Lenguajes & Runtimes

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| nodejs-backend-patterns | `agents` [dup:3] | node, express, fastify, rest | Express/Fastify servers, auth, DB |
| nodejs-best-practices | `agents` [dup:3] | node, async, security | Node.js principles, framework selection |
| nestjs-expert | `backend-skills` | nestjs, di, guards, typeorm | NestJS modules, GraphQL, TypeORM |
| fastapi-expert | `backend-skills` | fastapi, pydantic, async, sqlalchemy | FastAPI, Pydantic v2, JWT |
| django-expert | `backend-skills` | django, drf, orm, jwt | Django ORM, DRF, JWT auth |
| laravel-specialist | `backend-skills` | laravel, eloquent, sanctum, livewire | Laravel 10+, Eloquent, Horizon |
| rails-expert | `backend-skills` | rails, turbo, sidekiq, rspec | Rails 7+, Active Record, Hotwire |
| spring-boot-engineer | `backend-skills` | spring, jpa, security, webflux | Spring Boot 3.x, Security 6 |
| dotnet-core-expert | `backend-skills` | dotnet, ef-core, cqrs, aot | .NET 8 minimal APIs, Clean Architecture |
| csharp-developer | `backend-skills` | csharp, blazor, signalr, ef | C#, ASP.NET Core, Blazor, EF Core |
| golang-pro | `backend-skills` | go, goroutines, grpc, pprof | Go concurrency, gRPC, idiomatic Go |
| rust-engineer | `backend-skills` | rust, async, tokio, ffi | Rust ownership, async tokio, traits |
| python-pro | `backend-skills` | python, typing, pytest, mypy | Python 3.11+, type hints, pytest |
| typescript-pro | `backend-skills` | typescript, generics, trpc | Advanced generics, tRPC, type guards |
| javascript-pro | `backend-skills` | javascript, esm, async | ES2023+, async/await, ESM |
| kotlin-specialist | `backend-skills` | kotlin, coroutines, ktor, compose | Kotlin coroutines, KMP, Ktor |
| swift-expert | `backend-skills` | swift, swiftui, async, actors | SwiftUI, async/await, Vapor |
| php-pro | `backend-skills` | php8, laravel, symfony, phpstan | PHP 8.3+, Laravel, Symfony |
| java-architect | `backend-skills` | java, spring, jpa, webflux | Spring Boot 3.x, WebFlux |

### 2.2 Arquitectura & Diseño

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| architecture-designer | `backend-skills` | system-design, adr, tradeoffs | System diagrams, ADRs |
| microservices-architect | `backend-skills` | ddd, saga, cqrs, event-sourcing | Distributed systems, service boundaries |
| api-designer | `backend-skills` | rest, graphql, openapi, pagination | API design, OpenAPI specs |
| graphql-architect | `backend-skills` | graphql, apollo, federation, dataloader | GraphQL schema, Apollo Federation |
| websocket-engineer | `backend-skills` | websocket, socketio, redis, presence | Real-time bidirectional messaging |
| fullstack-guardian | `backend-skills` | fullstack, security, validation | Security-focused fullstack features |
| secure-code-guardian | `backend-skills` | owasp, jwt, bcrypt, csp | OWASP Top 10, input validation |
| spec-miner | `backend-skills` | reverse-engineer, legacy, docs | Reverse-engineer undocumented codebases |
| legacy-modernizer | `backend-skills` | strangler, monolith, migration | Incremental migration strategies |
| cli-developer | `backend-skills` | cli, argparse, cobra, completions | CLI tools, argument parsing |

### 2.3 Bases de Datos & Query

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| postgres-pro | `backend-skills` | postgres, explain, jsonb, vacuum | PostgreSQL optimization, replication |
| supabase-postgres-best-practices | `skills` | postgres, supabase, perf | Postgres perf from Supabase |
| supabase | `skills` | supabase, auth, realtime, storage | Full Supabase platform |
| database-optimizer | `backend-skills` | queries, indexes, partitioning | Query optimization, lock resolution |
| sql-pro | `backend-skills` | sql, cte, window-functions, explain | Complex queries, EXPLAIN plans |
| d1-migration | `frontend-jezweb` | d1, cloudflare, migration | Cloudflare D1 migration workflow |
| d1-drizzle-schema | `frontend-jezweb` | drizzle, d1, schema, orm | Drizzle ORM schemas for D1 |
| db-seed | `frontend-jezweb` | seed, fixtures, test-data | Realistic seed scripts |

---

## 3. INFRAESTRUCTURA & CLOUD — Conocimiento

### 3.1 Cloudflare

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| cloudflare-worker-builder | `frontend-jezweb` | workers, hono, vite, deploy | Hono + Vite Workers scaffold |
| cloudflare-api | `frontend-jezweb` | dns, cache, waf, r2, kv, d1 | REST API for CF operations |
| hono-api-scaffolder | `frontend-jezweb` | hono, routes, zod, validation | Hono route scaffolding |
| tanstack-start | `frontend-jezweb` | tanstack, cloudflare, ssr | Full-stack TanStack on CF Workers |
| vite-flare-starter | `frontend-jezweb` | react, hono, d1, shadcn | Clone + deploy full-stack CF app |

### 3.2 Docker & Containers

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| docker | `skills` | docker, container, dev | Container-based dev for npm, build |
| devops-engineer | `backend-skills` | docker, ci/cd, k8s, terraform | Dockerfiles, CI/CD pipelines |
| ln-731-docker-generator | `backend-arch` | docker, compose, generation | Dockerfile + docker-compose generation |
| ln-783-container-launcher | `backend-arch` | container, health, verify | Build + launch containers with health checks |

### 3.3 Kubernetes & Nube

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| kubernetes-specialist | `backend-skills` | k8s, helm, rbac, gitops | Deployments, RBAC, Helm charts |
| cloud-architect | `backend-skills` | aws, azure, gcp, migration | Cloud migrations, Well-Architected |
| terraform-engineer | `backend-skills` | terraform, iac, state, modules | IaC modules, state management |

### 3.4 Monitoreo & SRE

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| monitoring-expert | `backend-skills` | prometheus, grafana, tracing | Monitoring stacks, load testing |
| sre-engineer | `backend-skills` | slo, error-budget, incident | SLOs, error budgets, capacity |
| chaos-engineer | `backend-skills` | chaos, resilience, game-days | Chaos experiments, failure injection |

---

## 4. AGILE PIPELINE — Conocimiento (ln-* series)

### 4.1 Discovery & Planning

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-200-scope-decomposer | planning, scope, epics, stories | Scope → Epics + Stories + RICE |
| ln-201-opportunity-discoverer | growth, traffic, kde | Traffic-First KILL funnel for growth |
| ln-210-epic-coordinator | epics, planning, breakdown | Decompose scope into 3-7 Epics |
| ln-220-story-coordinator | stories, decomposition, planning | Create/replan 5-10 Stories per Epic |
| ln-221-story-creator | stories, invest, document | 9-section Story docs with INVEST validation |
| ln-222-story-replanner | stories, replan, update | Replan Stories when Epic changes |
| ln-230-story-prioritizer | rice, prioritization, sprint | RICE score Stories for sprint planning |
| ln-500-story-quality-gate | quality, gate, pass-fail | Quality gate with 4-level verdict |

### 4.2 Task Management

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-300-task-coordinator | tasks, planning, breakdown | Story → optimal task plan (1-8 tasks) |
| ln-301-task-creator | tasks, linear, template | Create tasks from templates in Linear |
| ln-302-task-replanner | tasks, replan, sync | KEEP/UPDATE/OBSOLETE/CREATE task sync |

### 4.3 Execution

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-400-story-executor | execution, priority, pipeline | Execute Story tasks by priority |
| ln-401-task-executor | implementation, coding | Implementation tasks (Todo→In Progress→To Review) |
| ln-402-task-reviewer | review, quality, done | Review tasks, set Done or To Rework |
| ln-403-task-rework | rework, fix, feedback | Fix rejected tasks from reviewer |
| ln-404-test-executor | tests, execution, risk | Execute test tasks with risk-based limits |

### 4.4 Quality

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-510-quality-coordinator | quality, aggregate, verdict | Aggregate quality checks |
| ln-511-code-quality-checker | dry, kiss, yagni, score | DRY/KISS/YAGNI, Code Quality Score |
| ln-512-tech-debt-cleaner | tech-debt, cleanup, auto-fix | Auto-fix low-risk debt (>=90% confidence) |
| ln-513-regression-checker | regression, tests, verify | Run test suite after implementation |
| ln-514-test-log-analyzer | logs, errors, stacktrace | Classify errors, map stack traces |

### 4.5 Testing Pipeline

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-520-test-planner | planning, research, manual | Research + manual + automated test planning |
| ln-521-test-researcher | research, competitors, bugs | Real-world problems, competitor solutions |
| ln-522-manual-tester | manual, scripts, verify | Execute manual test scripts |
| ln-523-auto-test-planner | automated, risk, priority | Risk-Based automated test planning |

### 4.6 Auditing Suite

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-610-docs-auditor | docs, quality, audit | Documentation quality audit |
| ln-611-docs-structure-auditor | hierarchy, links, ssot | Docs structure audit |
| ln-612-semantic-content-auditor | coverage, gaps, off-topic | Semantic doc content audit |
| ln-613-code-comments-auditor | comments, docstrings, why | WHY-not-WHAT docstring quality |
| ln-614-docs-fact-checker | facts, paths, versions | Verify claims in .md files |
| ln-620-codebase-auditor | full-audit, coordinator | Full codebase audit coordination |
| ln-621-security-auditor | security, sqli, xss, secrets | Hardcoded secrets, vulnerabilities |
| ln-622-build-auditor | build, lint, errors, warnings | Compiler/linter error audit |
| ln-623-code-principles-auditor | dry, kiss, di, error-handling | Code principles compliance |
| ln-624-code-quality-auditor | complexity, nesting, god-class | Cyclomatic complexity, long methods |
| ln-625-dependencies-auditor | deps, outdated, cve | Outdated packages, vulnerabilities |
| ln-626-dead-code-auditor | dead-code, unused, commented | Unreachable code, unused imports |
| ln-627-observability-auditor | logging, metrics, tracing | Health checks, request tracing |
| ln-628-concurrency-auditor | async, races, deadlocks | Thread safety, TOCTOU |
| ln-629-lifecycle-auditor | startup, shutdown, cleanup | Bootstrap, graceful shutdown |
| ln-630-test-auditor | tests, coordinator, suite | Complete test suite audit |
| ln-631-test-business-logic-auditor | framework, vs-code | Detects framework tests vs business logic |
| ln-632-test-e2e-priority-auditor | e2e, risk, coverage | Validates E2E for critical paths |
| ln-633-test-value-auditor | value, impact, probability | Scores each test, KEEP/REVIEW/REMOVE |
| ln-634-test-coverage-auditor | coverage, gaps, missing | Identifies missing test coverage |
| ln-635-test-isolation-auditor | isolation, flaky, determinism | Test anti-patterns, flaky detection |
| ln-636-manual-test-auditor | manual, scripts, harness | Manual test script quality |
| ln-637-test-structure-auditor | structure, organization, layout | Test file organization audit |
| ln-640-pattern-evolution-auditor | patterns, compliance, catalog | Architectural pattern compliance |
| ln-641-pattern-analyzer | single-pattern, score | Single pattern implementation analysis |
| ln-642-layer-boundary-auditor | layers, violations, boundaries | Layer boundary violations |
| ln-643-api-contract-auditor | api, dto, leakage | Layer leakage, error contracts |
| ln-644-dependency-graph-auditor | cycles, coupling, metrics | Dependency graph, coupling metrics |
| ln-645-open-source-replacer | oss, custom-code, migration | Custom modules → OSS candidates |
| ln-646-project-structure-auditor | structure, naming, hygiene | File hygiene, ignore files |
| ln-647-env-config-auditor | env, config, defaults | Env var sync, naming conventions |
| ln-650-persistence-performance-auditor | persistence, perf, coordinator | Data layer performance audit |
| ln-651-query-efficiency-auditor | n+1, fetch, bulk, cache | Redundant fetches, over-fetching |
| ln-652-transaction-correctness-auditor | transactions, rollback | Transaction scope, rollback handling |
| ln-653-runtime-performance-auditor | blocking-io, allocations | Blocking IO in async, string concat |
| ln-654-resource-lifecycle-auditor | resources, pools, leaks | Session scope, pool config, leaks |

### 4.7 Bootstrap & Scaffolding

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-700-project-bootstrap | scaffold, production, setup | Production-ready project scaffold |
| ln-720-structure-migrator | clean-arch, structure | Clean Architecture structure |
| ln-721-frontend-restructure | react, components, arch | React component architecture |
| ln-722-backend-generator | dotnet, clean-arch, entities | .NET Clean Architecture from entities |
| ln-723-seed-data-generator | seed, orm, entities | Seed data from ORM schemas |
| ln-724-artifact-cleaner | cleanup, replit, codesandbox | Remove platform-specific artifacts |

### 4.8 DevOps & Crosscutting

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-730-devops-setup | docker, cicd, env | Docker + CI/CD + env config |
| ln-732-cicd-generator | github-actions, ci | GitHub Actions CI configuration |
| ln-733-env-configurator | env, secrets, gitignore | Environment variables, secrets |
| ln-740-quality-setup | linters, pre-commit, tests | Code quality tooling setup |
| ln-741-linter-configurator | eslint, prettier, ruff | Linter configuration |
| ln-742-precommit-setup | husky, commitlint | Git hook automation |
| ln-743-test-infrastructure | vitest, xunit, pytest | Test framework setup |
| ln-760-security-setup | secrets, scanning, cve | Security scanning infrastructure |
| ln-761-secret-scanner | secrets, hardcoded, scan | Hardcoded secrets detection |
| ln-770-crosscutting-setup | logging, errors, cors | Logging + errors + CORS + health |
| ln-771-logging-configurator | serilog, structlog, json | Structured JSON logging |
| ln-772-error-handler-setup | middleware, exceptions | Global exception handling |
| ln-773-cors-configurator | cors, security, policy | CORS policy configuration |
| ln-774-healthcheck-setup | k8s, probes, readiness | Health check endpoints |
| ln-775-api-docs-generator | swagger, openapi, docs | Interactive API documentation |
| ln-780-bootstrap-verifier | verify, build, test | Post-bootstrap validation |
| ln-781-build-verifier | build, compile, success | Build compilation verification |
| ln-782-test-runner | tests, coverage, run | Test suite execution |
| ln-783-container-launcher | docker, health, launch | Container verification |

### 4.9 Documentation Pipeline

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-100-documents-pipeline | docs, coordinator, all | Complete project documentation system |
| ln-110-project-docs-coordinator | project, type, detection | Project docs with type detection |
| ln-111-root-docs-creator | claude-md, agents-md | AGENTS.md, CLAUDE.md creation |
| ln-112-project-core-creator | requirements, arch, tech-stack | Core project documentation |
| ln-113-backend-docs-creator | api-spec, db-schema | API + DB schema docs |
| ln-114-frontend-docs-creator | design-guidelines, wcag | Design guidelines + WCAG 2.1 |
| ln-115-devops-docs-creator | infrastructure, runbook | DevOps documentation |
| ln-120-reference-docs-creator | adr, guides, manuals | Architecture Decision Records |
| ln-130-tasks-docs-creator | kanban, workflow | Task management documentation |
| ln-140-test-docs-creator | strategy, risk-based | Testing strategy documentation |
| ln-160-docs-skill-extractor | docs, skills, extract | Docs → .claude/commands skills |
| ln-161-skill-creator | create, skills, procedural | Skill file creation |
| ln-162-skill-reviewer | review, quality, criteria | Skill quality review (D1-D11) |

### 4.10 Performance Optimization

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-810-performance-optimizer | perf, coordinator, cycles | Multi-cycle profiling + optimization |
| ln-811-performance-profiler | cpu, memory, io | Runtime performance metrics |
| ln-812-optimization-researcher | benchmarks, hypotheses | Research + optimization hypotheses |
| ln-813-optimization-plan-validator | validate, review | Multi-agent optimization validation |
| ln-814-optimization-executor | keep-discard, test | Optimization execution with testing |

### 4.11 Dependency Management

| Skill | Tags | Propósito |
|-------|------|-----------|
| ln-820-dependency-optimization-coordinator | deps, upgrade, coordinator | Project-wide dependency upgrades |
| ln-821-npm-upgrader | npm, upgrade, breaking | npm/yarn/pnpm dependency upgrades |
| ln-822-nuget-upgrader | nuget, upgrade, breaking | .NET NuGet package upgrades |
| ln-823-pip-upgrader | pip, upgrade, breaking | Python dependency upgrades |
| ln-830-code-modernization-coordinator | modernization, coordinator | OSS replacement + bundle optimization |
| ln-831-oss-replacer | oss, replace, keep-discard | Custom → OSS with atomic testing |
| ln-832-bundle-optimizer | bundle, tree-shaking, split | JS/TS bundle size reduction |

---

## 5. TESTING — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| test-master | `backend-skills` | testing, mocking, coverage | Multi-type test generation |
| vitest | `frontend-jezweb` | vitest, jest-migration, config | Vitest setup, config, migration |
| playwright-expert | `backend-skills` | e2e, page-objects, visual | E2E tests, visual regression |
| testcontainers-dotnet | `testcontainers` | dotnet, docker, integration | .NET integration tests |
| testcontainers-go | `testcontainers` | go, docker, integration | Go integration tests |
| debugging-wizard | `backend-skills` | debug, stacktrace, root-cause | Error parsing, root cause analysis |

---

## 6. DOCUMENTACIÓN — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| code-documenter | `backend-skills` | docstrings, openapi, jsdoc | Docstrings, API docs, portals |
| project-docs | `frontend-jezweb` | architecture, endpoints, schema | ARCHITECTURE.md, API docs |
| app-docs | `frontend-jezweb` | user-guide, screenshots, how-to | User docs with screenshots |

---

## 7. GIT & GITHUB — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| git-commit | `git-cicd` | conventional-commits, commit | Structured commits with type/scope |
| git-workflow | `frontend-jezweb` | pr, branches, merge, tags | PR prep, branch cleanup, conflict resolution |
| github-pr-creation | `git-cicd` | pr, conventional, validation | Create PRs with validation |
| github-pr-review | `git-cicd` | review, comments, fix | Resolve PR review comments |
| github-pr-merge | `git-cicd` | merge, validation, cleanup | Merge PRs with pre-merge checks |
| github-release | `frontend-jezweb` | release, tag, sanitize | Sanitize, tag, publish releases |
| fork-discipline | `frontend-jezweb` | multi-client, boundary, audit | Core/client boundary enforcement |

---

## 8. SEO — Conocimiento

### 8.1 Auditorías Completas

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| seo | `seo-agrici` | full-audit, orchestrator | Comprehensive SEO orchestrator |
| seo-audit | `seo-agrici` | crawl, health-score, 10-specialists | Full site audit (500 pages) |
| seo-technical | `seo-agrici` | crawlability, indexability, CWV | Technical SEO audit |
| seo-page | `seo-agrici` | single-page, deep, on-page | Deep single-page SEO analysis |
| seo-content | `seo-agrici` | eeat, quality, ai-readiness | E-E-A-T quality, AI citations |
| seo-images | `seo-agrici` | alt-text, sizes, webp | Image optimization audit |
| seo-local | `seo-agrici` | gbp, nap, citations, reviews | Local SEO with GBP audit |
| seo-maps | `seo-agrici` | geo-grid, rank-tracking, solv | Maps intelligence, local rank tracking |
| seo-backlinks | `seo-agrici` | links, toxic, gap (dataforseo) | Backlink profile analysis |
| seo-hreflang | `seo-agrici` | international, multi-language | Hreflang international SEO |
| seo-sitemap | `seo-agrici` | xml, sitemap, validation | XML sitemap analysis |
| seo-programmatic | `seo-agrici` | templates, scale, thin-content | Programmatic SEO planning |
| seo-google | `seo-agrici` | gsc, pagespeed, crux, analytics | Google SEO APIs (field data) |
| technical-seo-checker | `seo-geo` | CWV, crawl, speed | Core Web Vitals, mobile audit |
| on-page-seo-auditor | `seo-geo` | titles, headers, images | Scored on-page audit |
| domain-authority-auditor | `seo-geo` | CITE, trust, 40-items | 40-item domain authority audit |
| content-quality-auditor | `seo-geo` | CORE-EEAT, 80-items | Publish-readiness EEAT gate |

### 8.2 On-Page & Schema

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| meta-optimizer | `seo-ccforseo` | titles, ctr, serp | Title + meta CTR optimization |
| meta-tags-optimizer | `seo-geo` | og, twitter, ctr | Open Graph, Twitter card optimization |
| schema-gen | `seo` | json-ld, any-page | JSON-LD for any page type |
| schema-markup-generator | `seo-geo` | faq, howto, article, product | JSON-LD rich results generation |
| seo-schema | `seo-agrici` | detect, validate, generate | Schema.org detection & validation |

### 8.3 AI / GEO / Generative Search

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| seo-geo | `seo-agrici` | ai-overviews, GEO, llms-txt | AI Overviews, GEO optimization |
| geo-content-optimizer | `seo-geo` | chatgpt, perplexity, citations | AI citation-optimized content |
| ai-seo | `skills` | ai-search, llm, citations | AI search engine optimization |
| ai-visibility | `seo-ccforseo` | brand-mentions, 6-platforms | Brand presence in AI answers |
| entity-optimizer | `seo-geo` | knowledge-graph, wikidata | Entity presence in Knowledge Graph |

### 8.4 Content & Keywords

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| seo-content-writer | `seo-geo` | blog, landing, seo-writing | SEO content writing |
| content-brief | `seo-ccforseo` | brief, serp-analysis, aeo | Writer-ready SEO briefs |
| content-gap-analysis | `seo-geo` | gaps, competitors, topics | Competitor topic gaps |
| content-refresher | `seo-geo` | update, freshness, rankings | Refresh outdated posts |
| keyword-research | `seo-geo` | volume, difficulty, intent | Keyword discovery |
| keyword-cluster | `seo-ccforseo` | clustering, intent, topic | Intent + topic grouping |
| serp-analysis | `seo-geo` | serp, features, intent | Ranking factors analysis |
| competitor-analysis | `seo-geo` | gaps, backlinks, content | Competitor SEO comparison |
| cannibalization | `seo-ccforseo` | keywords, gsc, serp | Keyword cannibalization detection |
| internal-links | `seo-ccforseo` | orphand, anchor, hub-spoke | Internal linking analysis |
| internal-linking-optimizer | `seo-geo` | site-arch, authority | Internal link optimization |

### 8.5 Estrategia & Monitoreo

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| seo-plan | `seo-agrici` | strategy, roadmap, template | Strategic SEO planning |
| programmatic-seo | `skills` | templates, scale, pseo | Pages at scale from data |
| site-architecture | `skills` | hierarchy, navigation, url | Page structure planning |
| content-strategy | `skills` | topics, clusters, calendar | Editorial planning strategy |
| schema | `skills` | json-ld, structured-data | Structured data implementation |
| performance-reporter | `seo-geo` | dashboards, stakeholders | SEO/GEO performance reports |
| rank-tracker | `seo-geo` | rankings, serp, changes | Keyword ranking tracking |
| alert-manager | `seo-geo` | alerts, drops, notifications | Automated SEO alerts |
| backlink-analyzer | `seo-geo` | authority, toxic, building | Backlink opportunity analysis |
| memory-management | `seo-geo` | persist, campaign, sessions | Cross-session campaign memory |

### 8.6 Data APIs

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| seo-dataforseo | `seo-agrici` | serp, volume, backlinks, ai | Live search data API |
| seo-firecrawl | `seo-agrici` | crawl, scrape, map | Full-site crawling & scraping |
| seo-image-gen | `seo-agrici` | ai-image, og, blog | AI image generation for SEO |

---

## 9. CONTENIDO & COPYWRITING — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| copywriting | `skills` | copy, landing, homepage, cta | Marketing page copy |
| copy-editing | `skills` | edit, refresh, polish | Review and improve existing copy |
| lead-magnets | `skills` | ebooks, checklist, gated | Downloadable lead generation |
| cold-email | `skills` | b2b, outreach, sequence | Cold outreach campaigns |
| emails | `skills` | drip, lifecycle, automation | Automated email flows |
| social | `skills` | linkedin, twitter, tiktok | Social media content |
| social-media-posts | `frontend-jezweb` | platform-specific, hooks | Platform-specific posts |
| proposal-writer | `frontend-jezweb` | sow, scope, pricing | Client proposals, SOWs |
| strategy-document | `frontend-jezweb` | swot, okr, competitive | Strategic business documents |
| resume-cover-letter | `frontend-jezweb` | resume, ats, formats | Tailored resumes + cover letters |
| award-application | `frontend-jezweb` | awards, grants, submission | Award entry writing |

### Business English Variants

| Skill | Tags | Propósito |
|-------|------|-----------|
| us-business-english | en-us, direct, american | American English business writing |
| uk-business-english | en-gb, polished, british | British English business writing |
| aussie-business-english | en-au, warm, australian | Australian English business writing |
| nz-business-english | en-nz, inclusive, nz | New Zealand English business writing |

---

## 10. MARKETING & GROWTH — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| product-marketing | `skills` | context, icp, positioning | Marketing context document setup |
| marketing-ideas | `skills` | brainstorm, strategy, growth | Growth strategy ideation |
| marketing-psychology | `skills` | biases, persuasion, behavior | Psychological principles for marketing |
| competitors | `skills` | vs-pages, comparison, seo | Competitor comparison pages |
| competitor-profiling | `skills` | research, dossiers, profiles | Structured competitor research |
| co-marketing | `skills` | partnerships, joint-campaigns | Partnership ideation |
| referrals | `skills` | referral, affiliate, virality | Referral program design |
| community-marketing | `skills` | discord, slack, clg | Online community strategy |
| ads | `skills` | google-ads, meta, linkedin | Paid advertising strategy |
| ad-creative | `skills` | headlines, variations, bulk | Bulk ad copy generation |
| launch | `skills` | producthunt, gtm, waitlist | Product launch planning |
| directory-submissions | `skills` | directories, backlinks, listing | Directory submission campaigns |
| image | `skills` | ai-image, mockups, optimization | Marketing image creation |
| aso | `skills` | app-store, google-play | App Store optimization |
| analytics | `skills` | ga4, gtm, mixpanel | Analytics setup & measurement |
| ab-testing | `skills` | experiments, hypothesis, significance | A/B test design & analysis |
| cro | `skills` | conversion, optimization, pages | Conversion rate optimization |
| popups | `skills` | exit-intent, modals, banners | Popup/overlay optimization |
| signup | `skills` | registration, friction, trial | Registration flow optimization |
| paywalls | `skills` | upgrade, feature-gating, freemium | In-app upgrade conversion |
| pricing | `skills` | tiers, packaging, monetization | Pricing decision strategy |
| churn-prevention | `skills` | cancel, save, dunning, winback | Retention strategy |
| onboarding | `skills` | activation, ttv, first-run | Post-signup activation flows |
| free-tools | `skills` | calculators, graders, lead-gen | Engineering-as-marketing tools |
| sales-enablement | `skills` | decks, one-pagers, scripts | Sales collateral creation |
| revops | `skills` | lead-scoring, routing, handoff | Revenue operations processes |
| customer-research | `skills` | icp, interviews, synthesis | Customer research & analysis |

---

## 11. VIDEO, 3D & ANIMACIÓN — Conocimiento

### 11.1 HyperFrames

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| hyperframes | `skills` | video, compositions, captions, tts | Video composition in HTML |
| hyperframes-cli | `skills` | cli, init, render, preview | CLI: lint, preview, render |
| hyperframes-media | `skills` | tts, whisper, bg-remove | Asset preprocessing pipeline |
| hyperframes-registry | `skills` | registry, blocks, components | Install registry blocks |
| website-to-hyperframes | `skills` | url-to-video, capture | Website → video from URL |
| remotion-to-hyperframes | `skills` | migration, porting | Port Remotion to HyperFrames |

### 11.2 Animation Adapters

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| gsap | `skills` | timeline, easing, stagger | GSAP in HyperFrames |
| css-animations | `skills` | keyframes, fill-mode | CSS keyframes in HyperFrames |
| waapi | `skills` | element-animate, currentTime | Web Animations API in HyperFrames |
| animejs | `skills` | anime, timeline | Anime.js in HyperFrames |
| three | `skills` | webgl, canvas, shader | Three.js/WebGL in HyperFrames |
| lottie | `skills` | lottie, dotlottie, after-effects | Lottie in HyperFrames |

### 11.3 General Video

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| video | `skills` | ai-video, avatar, veo, runway | AI video production |
| walkthrough-video | `frontend-jezweb` | remotion, demo, screenshots | App demo video creation |

---

## 12. AGENT PLATFORMS — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| voltagent-best-practices | `skills` | voltagent, agents, workflows | VoltAgent architecture |
| voltagent-docs-bundle | `skills` | api-reference, versioned | Version-matched VoltAgent API docs |
| create-voltagent | `skills` | cli, setup, project | VoltAgent project initialization |
| composio | `skills` | integrations, 1000-apps | External app integration platform |
| elevenlabs-agents | `frontend-jezweb` | voice, ai-agent, phone | Conversational voice AI agents |
| nemoclaw-setup | `frontend-jezweb` | nvidia, sandbox, openclaw | NVIDIA NemoClaw installation |
| pinokio | `skills` | discover, launch, apps | App discovery & launching |
| gws-setup | `frontend-jezweb` | google-workspace, cli | Google Workspace CLI setup |
| gws-install | `frontend-jezweb` | fast-install, existing-oauth | Quick gws re-install |
| google-apps-script | `frontend-jezweb` | sheets, workspace, automation | Apps Script automation |
| google-chat-messages | `frontend-jezweb` | chat, webhook, cards | GChat message sending |
| mcp-builder | `frontend-jezweb` | mcp, fastmcp, python | MCP server building |
| mcp-developer | `backend-skills` | mcp, sdk, transport | MCP server/client development |
| stripe-payments | `frontend-jezweb` | checkout, subscriptions | Stripe payment integration |
| parcel-tracking | `frontend-jezweb` | tracking, courier, auspost | Australian parcel tracking |
| atlassian-mcp | `backend-skills` | jira, confluence, mcp | Jira + Confluence integration |

---

## 13. PROMPT ENGINEERING — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| prompt-engineer | `backend-skills` | templates, output, evaluation | LLM prompt design |
| prompt-architect | `backend-skills` | 27-frameworks, 7-intents | Research-backed prompt frameworks |
| prompt-improver | `token-optimizer` | vague, research, clarify | Enrich vague prompts |
| Prompt Coach | `skills` | session-logs, quality | Claude Code session analysis |
| brains-trust | `frontend-jezweb` | multi-model, consensus | Multi-model second opinions |
| the-fool | `backend-skills` | devil-advocate, red-team | Structured critical reasoning |

---

## 14. AGENT TOOLS & UTILITIES — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| agent-browser | `frontend-jezweb` | browser, automate, scrape | Browser automation |
| project-health | `frontend-jezweb` | setup, audit, permissions | Project health management |
| deep-research | `frontend-jezweb` | research, discovery, explore | Multi-depth research |
| team-update | `frontend-jezweb` | updates, feedback, standup | Team communication |
| ux-audit | `frontend-jezweb` | dogfood, friction, persona | UX walkthrough audit |
| responsiveness-check | `frontend-jezweb` | breakpoints, viewport, test | Responsive design testing |
| design-review | `frontend-jezweb` | visual, layout, audit | Visual design quality review |
| onboarding-ux | `frontend-jezweb` | guidance, empty-states, tours | In-app user guidance |
| product-showcase | `frontend-jezweb` | screenshots, gif, marketing | Marketing site generation |
| landing-page | `frontend-jezweb` | html, tailwind, responsive | Self-contained landing pages |
| design-loop | `frontend-jezweb` | autonomous, multi-page, builder | Multi-page site builder |
| roadmap | `frontend-jezweb` | plan, execute, phased | App build planning + execution |
| find-skills | `skills` | discover, install | Skill discovery |
| creating-skills | `git-cicd` | create, best-practices | Skill creation guide |
| skill-creator | `skills` | create, effective | Skill authoring guide |
| caveman | `skills` | compression, tokens, brief | Ultra-compressed communication |

---

## 15. CMS & E-COMMERCE — Conocimiento

### 15.1 Shopify

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| shopify-expert | `backend-skills` | liquid, hydrogen, storefront | Full Shopify development |
| shopify-setup | `frontend-jezweb` | cli, auth, admin-api | CLI + API access setup |
| shopify-products | `frontend-jezweb` | products, variants, inventory | Product management |
| shopify-content | `frontend-jezweb` | pages, blog, navigation | Store content management |

### 15.2 WordPress

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| wordpress-pro | `backend-skills` | themes, plugins, blocks, acf | Full WordPress development |
| wordpress-setup | `frontend-jezweb` | wp-cli, ssh, rest-api | WordPress connection setup |
| wordpress-elementor | `frontend-jezweb` | elementor, templates | Elementor page editing |
| wordpress-content | `frontend-jezweb` | posts, media, menus | Content management |

---

## 16. DATA, AI & ML — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| pandas-pro | `backend-skills` | dataframe, cleaning, aggregation | Data manipulation |
| spark-engineer | `backend-skills` | spark, dataframe, tuning | Big data processing |
| ml-pipeline | `backend-skills` | mlflow, kubeflow, feast | ML pipeline infrastructure |
| rag-architect | `backend-skills` | embeddings, vector-store, hybrid | RAG system design |
| fine-tuning-expert | `backend-skills` | lora, qlora, peft | LLM fine-tuning |
| ai-image-generator | `frontend-jezweb` | gemini, gpt, prompting | AI image generation |

---

## 17. EMBEDDED & SPECIALIZED — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| embedded-systems | `backend-skills` | stm32, esp32, freertos | Microcontroller firmware |
| game-developer | `backend-skills` | unity, unreal, ecs | Game development |
| salesforce-developer | `backend-skills` | apex, lwc, soql | Salesforce platform |
| image-processing | `frontend-jezweb` | resize, convert, pillow | Image processing pipeline |

---

## 18. DEV SETUP — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| ln-010-dev-environment-setup | `backend-arch` | setup, agents, mcp | Full dev environment setup |
| ln-011-agent-installer | `backend-arch` | install, claude, gemini, codex | CLI agent installation |
| ln-012-mcp-configurator | `backend-arch` | mcp, servers, config | MCP server registration |
| ln-013-config-syncer | `backend-arch` | sync, claude, gemini, codex | Cross-agent config sync |
| ln-014-agent-instructions-manager | `backend-arch` | claude-md, agents-md | Agent instruction files |
| ln-015-hex-line-uninstaller | `backend-arch` | uninstall, hex-line | Hex-line removal |
| ln-020-codegraph | `backend-arch` | code-graph, dependencies | Code knowledge graph |
| ln-002-session-analyzer | `backend-arch` | session, analysis, improve | Session quality analysis |
| ln-001-push-all | `backend-arch` | commit, push, all | Quick bulk push |

---

## 19. COMUNIDAD — Conocimiento

| Skill | Fuentes | Tags | Propósito |
|-------|---------|------|-----------|
| ln-910-community-engagement | `backend-arch` | health, delegation | Community health management |
| ln-911-github-triager | `backend-arch` | triage, issues, prs | Issue/PR backlog triage |
| ln-912-community-announcer | `backend-arch` | announcements, releases | Community announcements |
| ln-913-community-debater | `backend-arch` | rfc, debate, proposals | RFC discussion launch |
| ln-914-community-responder | `backend-arch` | respond, unanswered | Backlog answer responses |

---

## MAPA DE USO RÁPIDO

> "Necesito hacer X → qué skill uso?"

### Desarrollo
| Necesidad | Skill Recomendado |
|-----------|------------------|
| Arrancar un proyecto nuevo | `ln-700-project-bootstrap` |
| Crear una API REST | `fastapi-expert`, `nestjs-expert`, `hono-api-scaffolder` |
| Modelar base de datos | `d1-drizzle-schema`, `supabase` |
| UI con React | `react-expert`, `shadcn-ui`, `tailwind-theme-builder` |
| UI con Vue | `vue-expert` |
| UI con Angular | `angular-architect` |
| Landing page rápido | `landing-page` |
| Mobile app | `react-native` o `flutter-expert` |

### Calidad
| Necesidad | Skill Recomendado |
|-----------|------------------|
| Code review | `code-reviewer` |
| Full audit | `ln-620-codebase-auditor` |
| Security audit | `ln-621-security-auditor` |
| Performance audit | `ln-810-performance-optimizer` |
| Dependency audit | `ln-625-dependencies-auditor` |
| Test coverage | `ln-634-test-coverage-auditor` |
| A11y check | `audit` (impeccable) |
| Docs audit | `ln-610-docs-auditor` |

### SEO
| Necesidad | Skill Recomendado |
|-----------|------------------|
| Full SEO audit | `seo-audit` |
| Technical SEO | `seo-technical` |
| Optimizar meta tags | `meta-optimizer` |
| Schema markup | `schema-gen` |
| Content brief | `content-brief` |
| Keyword research | `keyword-research` |
| Investigar competidores | `competitor-analysis` |
| AI/GEO optimization | `seo-geo` o `geo-content-optimizer` |
| AI visibility check | `ai-visibility` |
| Content refresh | `content-refresher` |

### Marketing & Growth
| Necesidad | Skill Recomendado |
|-----------|------------------|
| Copywriting | `copywriting` |
| Cold email | `cold-email` |
| Emails lifecycle | `emails` |
| Social media | `social` o `social-media-posts` |
| CRO | `cro` |
| A/B test | `ab-testing` |
| Pricing | `pricing` |
| Product launch | `launch` |

### Diseño
| Necesidad | Skill Recomendado |
|-----------|------------------|
| UI production grade | `frontend-design` |
| Hacer UI más bold | `bolder` |
| Hacer UI más clean | `distill` |
| Extraer design system | `design-system` (jezweb) |
| Paleta de colores | `color-palette` |
| Iconos SVG | `icon-set-generator` |
| Favicon | `favicon-gen` |
| Animaciones UI | `animate` |
| UX audit | `ux-audit` |

### Video
| Necesidad | Skill Recomendado |
|-----------|------------------|
| Video composition | `hyperframes` |
| Website → video | `website-to-hyperframes` |
| TTS / voiceover | `hyperframes-media` |
| GSAP animación | `gsap` |
| Three.js 3D | `three` |
| Walkthrough video | `walkthrough-video` |

### DevOps
| Necesidad | Skill Recomendado |
|-----------|------------------|
| Dockerfile | `ln-731-docker-generator` o `devops-engineer` |
| CI/CD pipeline | `ln-732-cicd-generator` |
| K8s manifests | `kubernetes-specialist` |
| Terraform | `terraform-engineer` |
| Logging setup | `ln-771-logging-configurator` |
| Health checks | `ln-774-healthcheck-setup` |

### Infraestructura de Calidad
| Necesidad | Skill Recomendado |
|-----------|------------------|
| ESLint + Prettier | `ln-741-linter-configurator` |
| Pre-commit hooks | `ln-742-precommit-setup` |
| Test infra (Vitest) | `vitest` o `ln-743-test-infrastructure` |
| Integration tests | `testcontainers-dotnet` o `testcontainers-go` |
| E2E tests | `playwright-expert` |

---

## DUPLICADOS: Merge Map

| Grupo Duplicado | Fuentes | Acción Recomendada |
|-----------------|---------|-------------------|
| `ui-ux-pro-max` | 3 locations | Keep `Documents/.opencode/skills/`, symlink others |
| `nodejs-best-practices` | 3 locations | Keep `Documents/.agents/skills/`, symlink |
| `nodejs-backend-patterns` | 3 locations | Same |
| `schema` (markup) | `seo`, `seo-geo`, `seo-agrici`, `skills` | `seo-schema` de seo-agrici es el más completo |
| `meta-optimizer` vs `meta-tags-optimizer` | `seo-ccforseo` vs `seo-geo` | Complementarios, mantener ambos |
| `internal-links` vs `internal-linking-optimizer` | `seo-ccforseo` vs `seo-geo` | `seo-ccforseo` tiene más detalle técnico |
| `ai-seo` / `seo-geo` / `geo-content-optimizer` | 3 skills diferentes | `seo-geo` (seo-agrici) es el orquestador |
| `design-system` (CKM vs jezweb) | Son diferentes | CKM = token specs, jezweb = extractor |

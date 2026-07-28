# SuperDuperSkills

Inventario centralizado de skills multi-agente para Claude Code, Gemini CLI, Codex CLI y otros agentes de IA.

## Repositorios de Skills

| Repo | Ruta | Origen |
|------|------|--------|
| **agents** | `~/.agents/skills/` | Skills de productividad, marketing, video, HyperFrames |
| **opencode** | `~/.config/opencode/skills/` | SEO, frontend/backend, Cloudflare, diseño, testing, pipeline |
| **claude** | `~/.claude/skills/` | Lenguajes, frameworks, DevOps, infraestructura |

Estos 3 directorios contienen tanto skills individuales (marketplace/plugins) como ~26 skill-libraries clonadas explícitamente por los instaladores de este repo (mingrath, jeffallan, wondelai, taste-skill, mattpocock/skills, the-architect, etc.). El listado completo con conteo de estrellas y qué trae cada una vive en [`AGENTS.md`](AGENTS.md#directorios-donde-buscar-skills).

## Archivos del Repo

| Archivo | Descripción |
|---------|-------------|
| `SKILLS-INDEX.md` | Índice completo con todas las skills, descripciones y rutas |
| `UNIFIED-KNOWLEDGE.md` | Taxonomía multi-conocimiento unificada |
| `skills-inventory.md` | Inventario detallado por repositorio de origen |
| `skills-lock.json` | Snapshot congelado de una instalación antigua (fuentes ajenas a las de este repo) — no se regenera con `build_index.py`, es legado histórico, no una fuente de verdad actual |
| `AGENTS.md` | Instrucciones de recuperación para cualquier agente |
| `skills/` | Bundles de todos los SKILL.md listos para instalar |
| `install.sh` | Instalador para Linux/macOS/Git Bash |
| `install.ps1` | Instalador para Windows PowerShell |
| `build_index.py` | Script para regenerar el bundle desde las fuentes |
| `installers/install-claude-plugins.ps1` | Setup de maquina nueva para Claude Code: plugins (Superpowers, Caveman, token-optimizer), y clonado de skill-libraries de backend, frontend, UI/UX, seguridad, testing y debugging |
| `installers/install-opencode-plugins.ps1` | Equivalente para OpenCode: plugins npm + opencode.json de empresa + mismas skill-libraries |
| `hooks/session-start-skill-picker.sh` | Hook real de Claude Code — al iniciar sesión en un proyecto sin skills confirmados, obliga a presentar un menú y esperar confirmación antes de codear |
| `templates/skill-confirmation-block.md` | Bloque de texto para pegar en el `CLAUDE.md` de un proyecto — refuerzo escrito de la misma regla de confirmación de skills |

## Confirmación de skills al iniciar un proyecto

¿Quieres que Claude siempre pregunte qué skills usar antes de escribir código, en vez de improvisar? Ver [`hooks/README.md`](hooks/README.md) — trae un hook `SessionStart` real (instalable por proyecto o global) que obliga a presentar un menú categorizado y esperar tu confirmación, más un bloque de refuerzo para el `CLAUDE.md` del proyecto. Los defaults siempre propuestos: `caveman`, `ponytail`, `harness`, `graphify`, y un skill de token-efficiency.

## Total de Skills

**2552** skills únicos deduplicados entre los 3 repositorios (última regeneración via `build_index.py`).

| Categoría | Cantidad | Qué incluye |
|-----------|----------|-------------|
| DevOps & Cloud | 201 | Docker, Kubernetes, Terraform, CI/CD, Cloudflare, Wrangler, incidentes |
| Development & Backend | 185 | Lenguajes, frameworks backend, APIs, DB, `senior-*`, arquitectura |
| Project Management | 150 | Pipeline ágil (`ln-*`), planning, sprints, retros, roadmaps |
| Engineering Practices | 143 | `ring:*` (workflow de ingeniería), clean-code, DDD, code review, skill-creator |
| Testing & QA | 140 | `qe-*` (fleet de QA), TDD, coverage, mutation/contract/E2E testing |
| Marketing & Growth | 135 | Ads (12 plataformas), CRO, growth, ASO, positioning frameworks |
| Design & UX | 113 | Frontend-design, design systems, anti-slop (`ponytail`, `taste-*`), DESIGN.md library |
| Business & Strategy | 103 | C-level advisors, estrategia, finanzas, producto, competencia |
| AI & Agents | 100 | MCP servers, agentes, RAG, prompt engineering, LLM tooling |
| Writing & Content | 69 | Copywriting, copy-editing, inglés de negocios, comunicación interna |
| SEO & Content | 58 | Keyword research, schema markup, technical SEO, GEO/AI-visibility |
| Compliance & Legal | 33 | GDPR, SOC2, ISO, auditorías regulatorias |
| Productivity & People | 9 | Onboarding, hiring, coaching, cultura de equipo |
| Video & Animation | 16 | GSAP, Lottie, Three.js, producción de video |
| Sales & Comms | 7 | Cold email, propuestas comerciales, pitch decks |
| Other | 1090 | Skills muy específicos, más 2 colecciones agregadoras masivas (ComposioHQ y alirezarezvani, ~1600 skills combinadas) que cubren territorio propio y todavía no calzan en las categorías de arriba; ver `SKILLS-INDEX.md` |

El desglose completo (skill por skill, con GitHub y ruta) vive en [`SKILLS-INDEX.md`](SKILLS-INDEX.md) — se regenera automáticamente y es la fuente de verdad actual. `skills-inventory.md` y `UNIFIED-KNOWLEDGE.md` son una curaduría más profunda pero corresponden a una foto anterior (402 skills); úsalos para contexto narrativo, no para el conteo.

## Instalación

Clona el repo y ejecuta el instalador:

### Windows (PowerShell)
```powershell
.\install.ps1 -Target claude    # Solo Claude Code
.\install.ps1 -Target all       # Todos los agentes
.\install.ps1 -Mode symlink     # Usar symlinks en vez de copia
```

### Linux / macOS / Git Bash
```bash
./install.sh                    # Todos los agentes detectados
./install.sh --target claude    # Solo Claude Code
./install.sh --mode symlink     # Symlinks en vez de copia
./install.sh --dry-run          # Vista previa sin instalar
```

El instalador copia (o symlinkea) cada skill desde `skills/<nombre>/SKILL.md` al directorio del agente correspondiente (`~/.claude/skills/`, `~/.gemini/skills/`, `~/.codex/skills/`). Los skills existentes se saltan para no sobrescribir personalizaciones.

### Setup de maquina nueva (plugins + skill-libraries por categoria)

Si estas configurando una maquina desde cero y quieres tambien plugins de marketplace y las skill-libraries externas (no solo el bundle de este repo), usa:

```powershell
.\installers\install-claude-plugins.ps1     # Claude Code: Superpowers, Caveman, token-optimizer + clones
.\installers\install-opencode-plugins.ps1   # OpenCode: plugins npm + opencode.json de empresa + clones
```

Ambos clonan skill-libraries reales ya rastreadas por este repo, organizadas por categoria:

| Categoria | Fuentes clonadas |
|-----------|------------------|
| **Backend** | jeffallan/claude-skills, supabase/agent-skills, backend-arch (levnikolaevich/claude-code-skills) |
| **Frontend** | mingrath/awesome-claude-skills, jezweb/claude-skills |
| **UI/UX** | plugin87/ux-ui-agent-skills (★444), nextlevelbuilder/ui-ux-pro-max-skill, pbakaus/impeccable, wondelai/skills (★1.7k — refactoring-ui, hooked-ux, ux-heuristics, lean-ux, top-design), anthropics/skills oficial (★ canvas-design, theme-factory), Leonxlnx/taste-skill (★64.9k — anti-slop), coleam00/excalidraw-diagram-skill (★4.1k), blader/humanizer (★29.7k), ibelick/ui-skills (★6.6k — baseline-ui, fixing-motion-performance, fixing-accessibility), VoltAgent/awesome-design-md (★105k — 74 DESIGN.md de marcas conocidas), fabricioctelles/skills (★38 — design-md-validator) |
| **Seguridad** | agamm/claude-code-owasp (★277), BehiSecc/awesome-claude-skills (★9.7k), jeffallan-skills (secure-code-guardian), backend-arch (ln-621/ln-760) |
| **Testing** | proffesor-for-testing/agentic-qe (★408), testcontainers/claude-skills, backend-arch (ln-63x auditores de cobertura) |
| **Debugging** | LerianStudio/ring (★202, TDD + systematic-debugging), jeffallan-skills (debugging-wizard), backend-arch (ln-514 test-log-analyzer) |
| **Calidad / Simplicidad** | DietrichGebert/ponytail (★82.9k — anti-over-engineering, YAGNI, ponytail-review/audit/debt/gain) |
| **Planificacion / Arquitectura** | ersinkoc/project-architect (★251 — SPECIFICATION/IMPLEMENTATION/TASKS/BRANDING = PRD+TRD+dev-plan+UI), Hainrixz/the-architect (★374 — entrevista fases, genera blueprint + CLAUDE.md del proyecto objetivo), mattpocock/skills (★189k — to-spec, wayfinder, implement, domain-modeling, tdd, diagnosing-bugs, code-review) |
| **Anti-slop / Estandares de codigo** | multica-ai/andrej-karpathy-skills (★196k — karpathy-guidelines, anti-overengineering) |
| **Ads / Marketing pago** | AgriciDaniel/claude-ads (★7.5k — auditorias en 12 plataformas: Google, Meta, Amazon, Apple, TikTok, LinkedIn, etc.) |
| **Coleccion general** | mrgoonie/claudekit-skills (★2.2k), ComposioHQ/awesome-claude-skills (★71.2k), alirezarezvani/claude-skills (★23.4k), openai/skills (★24.3k, oficial) |
| **Memoria persistente** | thedotmack/claude-mem (★88.8k — contexto entre sesiones) |
| **SEO (fuente adicional)** | AgriciDaniel/claude-seo (★12.6k) |
| **Cloud oficial** | microsoft/skills (★2.8k, oficial), cloudflare/skills (★2.5k, oficial) |
| **CI/CD** | fvadicamo/dev-agent-skills, harness/harness-skills, antigravity-fullstack-hq |

Las fuentes con estrellas anotadas se eligieron verificando el conteo real via `gh api repos/<owner>/<repo>` (no solo ranking de busqueda) para priorizar mantenimiento activo y adopcion real sobre listados genericos.

Despues de clonar, corre `python build_index.py` para que estas skills entren al bundle de este repo (ver siguiente seccion).

## Actualizar el Bundle

```bash
python build_index.py
```

Escanea `~/.agents/skills/`, `~/.config/opencode/skills/` y `~/.claude/skills/`, deduplica por nombre, y regenera `skills/` y `SKILLS-INDEX.md`. Luego commit y push para actualizar el repo.

## Uso

Cada skill es un archivo `SKILL.md` dentro de su directorio. Los agentes cargan estos skills según la tarea. Consulta `SKILLS-INDEX.md` para buscar por nombre o categoría.

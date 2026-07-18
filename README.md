# SuperDuperSkills

Inventario centralizado de skills multi-agente para Claude Code, Gemini CLI, Codex CLI y otros agentes de IA.

## Repositorios de Skills

| Repo | Ruta | Origen |
|------|------|--------|
| **agents** | `~/.agents/skills/` | Skills de productividad, marketing, video, HyperFrames |
| **opencode** | `~/.config/opencode/skills/` | SEO, frontend/backend, Cloudflare, diseño, testing, pipeline |
| **claude** | `~/.claude/skills/` | Lenguajes, frameworks, DevOps, infraestructura |

## Archivos del Repo

| Archivo | Descripción |
|---------|-------------|
| `SKILLS-INDEX.md` | Índice completo con todas las skills, descripciones y rutas |
| `UNIFIED-KNOWLEDGE.md` | Taxonomía multi-conocimiento unificada |
| `skills-inventory.md` | Inventario detallado por repositorio de origen |
| `skills-lock.json` | Lock de skills instaladas |
| `AGENTS.md` | Instrucciones de recuperación para cualquier agente |
| `skills/` | Bundles de todos los SKILL.md listos para instalar |
| `install.sh` | Instalador para Linux/macOS/Git Bash |
| `install.ps1` | Instalador para Windows PowerShell |
| `build_index.py` | Script para regenerar el bundle desde las fuentes |
| `installers/install-claude-plugins.ps1` | Setup de maquina nueva para Claude Code: plugins (Superpowers, Caveman, token-optimizer), y clonado de skill-libraries de backend, frontend, UI/UX, seguridad, testing y debugging |
| `installers/install-opencode-plugins.ps1` | Equivalente para OpenCode: plugins npm + opencode.json de empresa + mismas skill-libraries |

## Total de Skills

**1256** skills únicos deduplicados entre los 3 repositorios (última regeneración via `build_index.py`).

| Categoría | Cantidad |
|-----------|----------|
| Project Management | 147 |
| Development & Backend | 121 |
| Writing & Content | 58 |
| Design & UX | 60 |
| Business & Strategy | 53 |
| Marketing & Growth | 51 |
| SEO & Content | 47 |
| DevOps & Cloud | 38 |
| AI & Agents | 29 |
| Compliance & Legal | 11 |
| Sales & Comms | 7 |
| Productivity & People | 7 |
| Video & Animation | 15 |
| Other | 612 |

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
| **UI/UX** | plugin87/ux-ui-agent-skills (★444), nextlevelbuilder/ui-ux-pro-max-skill, pbakaus/impeccable, wondelai/skills (★1.7k — refactoring-ui, hooked-ux, ux-heuristics, lean-ux, top-design), anthropics/skills oficial (★ canvas-design, theme-factory), Leonxlnx/taste-skill (★64.9k — anti-slop), coleam00/excalidraw-diagram-skill (★4.1k), blader/humanizer (★29.7k) |
| **Seguridad** | agamm/claude-code-owasp (★277), BehiSecc/awesome-claude-skills (★9.7k), jeffallan-skills (secure-code-guardian), backend-arch (ln-621/ln-760) |
| **Testing** | proffesor-for-testing/agentic-qe (★408), testcontainers/claude-skills, backend-arch (ln-63x auditores de cobertura) |
| **Debugging** | LerianStudio/ring (★202, TDD + systematic-debugging), jeffallan-skills (debugging-wizard), backend-arch (ln-514 test-log-analyzer) |
| **Calidad / Simplicidad** | DietrichGebert/ponytail (★82.9k — anti-over-engineering, YAGNI, ponytail-review/audit/debt/gain) |
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

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

## Total de Skills

**~400+** skills únicos deduplicados entre los 3 repositorios.

## Uso

Cada skill es un archivo `SKILL.md` dentro de su directorio. Los agentes cargan estos skills según la tarea. Consulta `SKILLS-INDEX.md` para buscar por nombre o categoría.

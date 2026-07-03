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

## Total de Skills

**402** skills únicos deduplicados entre los 3 repositorios.

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

## Actualizar el Bundle

```bash
python build_index.py
```

Escanea `~/.agents/skills/`, `~/.config/opencode/skills/` y `~/.claude/skills/`, deduplica por nombre, y regenera `skills/` y `SKILLS-INDEX.md`. Luego commit y push para actualizar el repo.

## Uso

Cada skill es un archivo `SKILL.md` dentro de su directorio. Los agentes cargan estos skills según la tarea. Consulta `SKILLS-INDEX.md` para buscar por nombre o categoría.

# Hooks — confirmar skills al empezar un proyecto

Este directorio trae un hook real de Claude Code (no solo una instrucción de
texto) que se dispara al iniciar sesión en un proyecto y le pide a Claude que
presente un menú de skills relevantes y espere tu confirmación antes de
empezar a escribir código.

## Cómo funciona

- `session-start-skill-picker.sh` — hook `SessionStart`. Si el proyecto no
  tiene todavía `.claude/.skills-selected.json`, inyecta instrucciones que
  obligan a Claude a: inferir el dominio del proyecto, armar un menú corto de
  skills relevantes (siempre incluyendo `caveman`, `ponytail`, `harness`,
  `graphify` y un skill de token-efficiency por defecto), preguntarte y
  confirmar, y guardar la selección para no volver a preguntar en la misma
  carpeta.
- Es determinístico en el disparo (el hook SIEMPRE corre al iniciar sesión),
  pero la construcción del menú la hace el modelo, no el script — un script
  bash no puede inferir de forma confiable el stack/dominio de un proyecto
  nuevo, así que esa parte se delega a Claude con instrucciones explícitas.

## Instalación en un proyecto

1. Copia el script a tu proyecto:
   ```bash
   mkdir -p .claude/hooks
   cp /ruta/a/superduperskills/hooks/session-start-skill-picker.sh .claude/hooks/
   chmod +x .claude/hooks/session-start-skill-picker.sh
   ```
2. Mergea `settings-snippet.json` dentro de tu `.claude/settings.json` (o
   `.claude/settings.local.json` si prefieres que no se comparta en git).
   Si ya tienes hooks configurados, agrega solo el bloque `SessionStart`
   dentro de tu `hooks` existente — no reemplaces el archivo entero.
3. Reinicia la sesión de Claude Code en ese proyecto. Al arrancar, deberías
   ver a Claude presentarte el menú de skills antes de tocar código.

## Instalación global (todos los proyectos)

En vez de instalarlo por proyecto, puedes ponerlo una vez en
`~/.claude/hooks/session-start-skill-picker.sh` y registrarlo en
`~/.claude/settings.json` (nivel usuario) — dispara en toda sesión, sin
importar el proyecto. La verificación de `.claude/.skills-selected.json`
sigue siendo por proyecto (carpeta actual), así que cada proyecto confirma
su propia selección una sola vez aunque el hook sea global. Si ya tienes
otros hooks en `SessionStart` (p. ej. de otro plugin), agrega esta entrada
dentro del mismo array de `hooks`, no reemplaces el bloque completo:

```json
"SessionStart": [
  {
    "matcher": "",
    "hooks": [
      { "type": "command", "command": "...tu hook existente..." },
      {
        "type": "command",
        "command": "bash \"C:\\Users\\<tu-usuario>\\.claude\\hooks\\session-start-skill-picker.sh\"",
        "timeout": 5
      }
    ]
  }
]
```

## Reiniciar la selección

Borra `.claude/.skills-selected.json` en el proyecto y la próxima sesión
volverá a preguntar.

## La otra mitad: refuerzo en CLAUDE.md

El hook cubre el arranque de sesión. Para que la confirmación de skills
también quede como regla escrita y visible en el propio `CLAUDE.md` del
proyecto (útil cuando `the-architect` o `project-architect` generan uno
nuevo), pega el bloque de [`templates/skill-confirmation-block.md`](../templates/skill-confirmation-block.md)
en la sección de reglas operativas del `CLAUDE.md` del proyecto.

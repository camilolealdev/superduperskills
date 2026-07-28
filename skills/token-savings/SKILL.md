---
name: token-savings
description: >
  Confirms which skills are actually relevant to a project BEFORE work
  starts, instead of the model guessing, loading, or invoking skills
  ad-hoc — the single biggest lever for cutting wasted tokens across a
  session (a project's skill listing metadata alone can be a meaningful
  fraction of context; picking wrong or invoking speculatively compounds
  that cost turn after turn). Use when the user says "/token-savings",
  "ahorra tokens", "optimiza tokens", "qué skills debería usar",
  "confirma los skills antes de empezar", or at the start of a new
  project before writing substantial code. Complements (does not
  replace) caveman/token-efficiency/tokensaver, which compress the
  model's own output — this skill instead reduces the input/context cost
  of loading and re-evaluating skills. Backed by a SessionStart hook
  (hooks/session-start-skill-picker.sh in superduperskills) that runs
  this automatically once per project; invoke this skill directly to
  re-run the check mid-project or on a machine without the hook installed.
---

# Token Savings — confirmar skills antes de trabajar

## Por qué existe

Cada skill instalado añade su nombre+descripción a la metadata que se
inyecta en cada turno. A esta escala (1300+ skills en `superduperskills`),
eso ya es un costo fijo — el desperdicio real viene de una segunda causa:
invocar o considerar skills que no aplican al proyecto actual, tarea por
tarea, sin una decisión explícita una sola vez al principio. Confirmar la
selección UNA vez por proyecto evita re-evaluar el catálogo completo en
cada turno y evita que el modelo "pruebe" skills irrelevantes.

## Cuándo correr esto

- Al empezar un proyecto nuevo (si el hook `session-start-skill-picker.sh`
  ya está instalado, esto ya corrió automáticamente — revisa si existe
  `.claude/.skills-selected.json` antes de repetir el trabajo).
- Cuando el usuario pide explícitamente ahorrar tokens u optimizar el uso
  de skills a mitad de proyecto.
- Cuando cambias de dominio dentro del mismo proyecto (ej. pasas de
  backend a diseño de UI) y la selección confirmada ya no cubre lo nuevo.

## Pasos

1. **Si existe `.claude/.skills-selected.json`**, léelo y muéstraselo al
   usuario como la selección vigente. Pregunta si quiere ajustarla antes
   de continuar — no repitas todo el proceso de cero si no es necesario.
2. **Si no existe**, infiere el dominio del proyecto (package.json,
   requirements.txt, go.mod, código existente, o el objetivo declarado del
   usuario si el proyecto es nuevo).
3. Arma un menú corto (8-15, no el catálogo completo) de skills instalados
   relevantes a ese dominio — revisa `~/.claude/skills/`,
   `~/.config/opencode/skills/`, o `SKILLS-INDEX.md` de `superduperskills`
   si el repo está disponible.
4. **Incluye siempre por defecto**, sin importar el dominio (el usuario
   puede quitarlos, no los omitas de la propuesta):
   - `caveman` — respuestas comprimidas
   - `ponytail` — anti-over-engineering / revisión YAGNI
   - `harness` / `harness-skills` — si el proyecto tiene pipeline CI/CD
   - `graphify` — grafo de conocimiento del codebase
   - un skill de compresión de output (`token-efficiency` / `tokensaver` /
     `token-optimizer`) — nota: esos comprimen lo que el modelo escribe;
     este skill reduce lo que el modelo carga/reconsidera. Son complementarios,
     no reemplazos entre sí.
5. Confirma con el usuario (`AskUserQuestion` o lista numerada).
6. Guarda la selección en `.claude/.skills-selected.json`:
   `{"selected": ["skill-a", "skill-b", ...], "confirmed_at": "<fecha ISO>"}`.
7. Reporta en una línea cuántos skills quedaron seleccionados vs. cuántos
   había disponibles para ese dominio, como evidencia del ahorro.

## Relación con el resto del sistema

- `hooks/session-start-skill-picker.sh` (en `superduperskills`) — versión
  automática de este mismo flujo, disparada por un hook `SessionStart` real.
- `templates/skill-confirmation-block.md` — la misma regla en texto, para
  pegar en el `CLAUDE.md` de un proyecto como respaldo si el hook no está
  instalado.
- Esta skill es la versión invocable a demanda de las dos anteriores —
  úsala cuando quieras re-confirmar sin depender de que el hook exista en
  esta máquina.

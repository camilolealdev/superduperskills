<!--
Pega este bloque en la sección de reglas operativas del CLAUDE.md de un
proyecto (o dentro del bloque "Skills to Use During Build" que generan
the-architect / project-architect). Refuerza en texto lo que el hook de
hooks/session-start-skill-picker.sh ya hace en código — sirve como respaldo
si el hook no está instalado, y como documentación legible para cualquiera
que abra el CLAUDE.md.
-->

## Invocación y confirmación de skills

Antes de escribir código sustancial en este proyecto (no aplica a preguntas
triviales, lectura de archivos, o cambios de una línea):

1. **Identifica el dominio** de la tarea (backend, frontend, UI/UX,
   seguridad, testing, debugging, documentación, etc.).
2. **Verifica qué skills hay instalados** para ese dominio (`~/.claude/skills/`,
   `~/.config/opencode/skills/`, o `SKILLS-INDEX.md` si el repo
   `superduperskills` está disponible) y arma una lista corta (8-15) de los
   más relevantes — no dumps de la lista completa.
3. **Siempre incluye estos por defecto**, sin importar el dominio de la
   tarea (el usuario puede quitarlos, pero no los omitas de la propuesta):
   - `caveman` — respuestas comprimidas, ahorro de tokens
   - `ponytail` — anti-over-engineering / revisión YAGNI
   - `harness` / `harness-skills` — CI/CD, si el proyecto tiene pipeline
   - `graphify` — grafo de conocimiento del codebase (útil una vez hay contenido)
   - un skill de token-efficiency (`token-efficiency` / `tokensaver` /
     `token-optimizer`)
4. **Pregunta y confirma** la lista con el usuario antes de proceder. No
   improvises con un skill genérico cuando hay uno especializado disponible
   para el dominio exacto de la tarea.
5. Si el proyecto ya tiene una selección confirmada (revisa si existe
   `.claude/.skills-selected.json`), no vuelvas a preguntar — respétala hasta
   que el usuario pida cambiarla.

**Regla de calidad:** el skill se invoca para elevar la calidad del output,
no como trámite. Si el skill de `frontend-design` dice "evitar Inter y
purple gradients", eso se aplica. Si `ponytail` marca algo como
over-engineered, se simplifica antes de continuar.

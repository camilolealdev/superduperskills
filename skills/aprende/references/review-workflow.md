# `/aprende --review` workflow / workflow de `/aprende --review`

`/aprende --review` is the aging and pruning mode. It surfaces existing
`lesson` files in the current project's memory folder, oldest first, and
asks whether each is still valid. Retired lessons stay on disk for audit
but are skipped by future `/aprende` runs.

`/aprende --review` es el modo de envejecimiento y poda. Saca a la luz los
archivos `lesson` existentes en la carpeta de memoria del proyecto actual,
los más viejos primero, y pregunta si cada uno sigue siendo válido. Las
lecciones retiradas quedan en disco para auditoría pero se ignoran en
corridas futuras de `/aprende`.

---

## When to run / Cuándo correr

- The user types `/aprende --review`.
- Suggested cadence: monthly per project, or whenever a lesson seems to be
  misfiring (the agent followed it and got a worse result).
- The user can also run it after a major refactor that may invalidate
  prior lessons.

Cadencia sugerida: mensual por proyecto, o cuando una lección parezca estar
fallando, o después de un refactor mayor.

---

## Flow / Flujo

1. **Find lessons.** `ls ~/.claude/projects/<slug>/memory/lesson_*.md`.
   If none exist, print `No lessons to review in this project.` and exit.

2. **Sort.** Read each file's frontmatter. Sort by `metadata.lastValidated`
   ascending (oldest first). If `lastValidated` is missing, treat as the
   epoch (sort first).

3. **For each lesson, present:**
   ```
   Lesson 1 of N — last validated YYYY-MM-DD (confidence: high)
   <title>
   <description>

   Still valid? [y/n/edit/skip]
   >
   ```

4. **Process response:**
   - `y` — bump `lastValidated` in the frontmatter to today's date. Keep
     `status: active`.
   - `n` — set `status: retired`. Bump `lastValidated`. **Do not delete
     the file.**
   - `edit` — print the full body of the lesson, prompt the user for a
     new version (free-text input until they type `END` on its own line).
     Overwrite the body (frontmatter is regenerated with bumped
     `lastValidated`).
   - `skip` — do not touch the file. Move on.
   - any other input — ask again (do not guess).

5. **At the end**, print summary:
   ```
   Reviewed N lessons:
     ✓ validated:  X
     ⊘ retired:    Y
     ✎ edited:     Z
     - skipped:    W
   ```

---

## Editing rules / Reglas de edición

When the user picks `edit`:
1. Read the file. Print the four-section body verbatim, in a fenced block.
2. Prompt: `Paste the new body (terminate with a line containing only END):`
3. Read input lines until `END` on its own line.
4. Validate: the new body **must** contain all four mandatory subheads
   (`**What happened`, `**Why it happened`, `**How to avoid`,
   `**Detection signal`). If missing, reject and ask again.
5. Write back: frontmatter with bumped `lastValidated`, new body, original
   frontmatter fields preserved (`createdAt`, `confidence`,
   `originSessionId`).

Cuando el usuario elige `edit`:
1. Lee el archivo. Imprime el cuerpo de cuatro secciones tal cual, en un
   fenced block.
2. Prompt: `Pega el cuerpo nuevo (termina con una línea que solo diga END):`
3. Lee líneas hasta `END` sola.
4. Valida: el cuerpo nuevo **debe** tener los cuatro subheads obligatorios.
   Si faltan, rechaza y vuelve a pedir.
5. Escribe de vuelta: frontmatter con `lastValidated` actualizado, cuerpo
   nuevo, campos originales preservados.

---

## Retire rules / Reglas de retiro

When the user picks `n`:
1. Set `metadata.status: retired` in the frontmatter.
2. Bump `metadata.lastValidated` to today's date (so it doesn't reappear
   on the next review).
3. Do **not** delete the file. Do **not** delete the MEMORY.md index entry.
   Audit trail matters more than disk space.

If you want to fully delete a retired lesson, the user does it manually
with `rm` and a manual edit of MEMORY.md. The skill never deletes.

Si el usuario quiere borrar completamente una lección retirada, lo hace
manualmente. El skill nunca borra.

---

## Supersede / Reemplazar

When a new lesson is written that explicitly replaces an old one, the
`/aprende` write flow (not `--review`) sets the old lesson's `status` to
`superseded-by-<new-name>`. The user can do this manually too.

Cuando se escribe una lección nueva que reemplaza explícitamente a una
vieja, el flujo de escritura de `/aprende` (no `--review`) marca la vieja
con `status: superseded-by-<nombre-nuevo>`. El usuario también puede
hacerlo manualmente.

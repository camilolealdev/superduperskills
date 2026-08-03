---
name: aprende
version: 0.1.0
license: MIT
description: |
  EN — Review the current conversation and surface reusable learnings across four
  categories (memory, lesson, skill, project-doc). Generate a numbered candidate
  list first; only write to disk after the user confirms. Trigger when the user
  types /aprende, /learn, "reflect on this", "save what we learned", "remember
  this for next time", or after correcting the agent on a recurring mistake.
  ES — Revisa la conversación actual y extrae aprendizajes reusables en cuatro
  categorías (memoria, lección, skill, project-doc). Genera primero una lista
  numerada de candidatos; solo escribe a disco después de la confirmación del
  usuario. Activa cuando el usuario escriba /aprende, /learn, "reflexiona sobre
  esto", "guarda lo que aprendimos", "recordar esto para la próxima", o después
  de corregir al agente sobre un error recurrente.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# `aprende` — Learn from this conversation / Aprende de esta conversación

> EN — A skill that turns finished conversations into durable, structured
> learnings: memories, anti-patterns (Reflexion-style), skill stubs, and
> project-doc updates. Confirmation-first. Never auto-writes.
>
> ES — Un skill que convierte conversaciones terminadas en aprendizajes
> durables y estructurados: memorias, anti-patrones (estilo Reflexion), stubs
> de skills, y actualizaciones a project-docs. Confirmación primero. Nunca
> escribe automáticamente.

---

## 1. Purpose / Propósito

**EN.** Coding agents repeat mistakes across sessions because the corrections a
user makes in one conversation evaporate when the session ends. `aprende`
fixes that. When invoked, it reviews the current conversation, identifies what
is worth preserving across four well-defined categories, and writes those
learnings to the right files — in the format the user's existing memory
system already reads — only after the user picks the items to keep.

Guiding principle: **a false positive locked into memory is worse than
repeating a correction three times.** Be liberal at surfacing candidates,
strict at confirming them, and conservative at writing them. Prefer false
negatives.

**ES.** Los agentes de código repiten errores entre sesiones porque las
correcciones que el usuario hace en una conversación se evaporan cuando esa
sesión termina. `aprende` arregla eso. Al activarse, revisa la conversación
actual, identifica qué vale la pena preservar a través de cuatro categorías
bien definidas, y escribe esos aprendizajes en los archivos correctos — en el
formato que ya usa el sistema de memoria del usuario — solo después de que el
usuario elija qué guardar.

Principio rector: **un falso positivo cristalizado en la memoria es peor que
repetir una corrección tres veces.** Sé liberal al proponer candidatos,
estricto al confirmarlos, y conservador al escribirlos. Prefiere los falsos
negativos.

---

## 2. When to invoke / Cuándo activarse

**EN — Trigger on any of:**
- The user types `/aprende` or `/learn` (the English alias).
- The user types phrases like: "reflect on this", "save what we learned",
  "remember this for next time", "let's capture that", "make a note of this",
  "don't forget X next session".
- The user has corrected the agent on the same thing **twice** in a session —
  proactively *suggest* running `/aprende` (one line, in the assistant turn);
  do not run it without permission.
- The session is wrapping up (the user says "we're done", "good, ship it",
  "commit and push") and signals have been captured by the optional
  PostToolUse hook (`.aprende-signals.md` exists with content).

**ES — Activa con cualquiera de estos:**
- El usuario escribe `/aprende` o `/learn` (alias en inglés).
- El usuario escribe frases como: "reflexiona sobre esto", "guarda lo que
  aprendimos", "recuérdalo para la próxima", "captura esto", "que no se nos
  olvide X".
- El usuario corrigió al agente sobre lo mismo **dos veces** en la sesión —
  proactivamente *sugiere* correr `/aprende` (una línea, en el turno del
  asistente); no lo ejecutes sin permiso.
- La sesión está cerrando ("ya terminamos", "listo, súbelo", "commit y push")
  y el hook PostToolUse capturó señales (existe `.aprende-signals.md` con
  contenido).

---

## 3. The four categories / Las cuatro categorías

| # | Category / Categoría | Lives at / Vive en | When / Cuándo |
|---|---------------------|--------------------|---------------|
| 1 | `memory` | `~/.claude/projects/<slug>/memory/<name>.md` (`metadata.type: user \| project \| reference \| feedback`) | Durable facts, preferences, project context, external references. *Hechos durables, preferencias, contexto del proyecto, referencias externas.* |
| 2 | `lesson` (anti-pattern) | Same folder, `metadata.type: lesson` | A mistake happened. We know what, why, and how to avoid. *Un error pasó. Sabemos qué, por qué, y cómo evitar.* |
| 3 | `skill` (stub) | `~/.claude/skills/<slug>/SKILL.md` or `./.claude/skills/<slug>/` | A reusable multi-step workflow surfaced. *Apareció un workflow multi-paso reutilizable.* |
| 4 | `project-doc` | `./CLAUDE.md` + `./AGENTS.md` (dual-write) — or `~/.claude/CLAUDE.md` + `~/.claude/AGENTS.md` for global | Build commands, repo conventions, gotchas worth telling every future agent. *Comandos de build, convenciones del repo, gotchas que vale la pena contarle a cada agente futuro.* |

**One example each / Un ejemplo de cada:**

- `memory` — "User prefers pnpm over npm in all JS projects." / "El usuario prefiere pnpm sobre npm en todos los proyectos JS."
- `lesson` — "Assumed `localStorage` works inside a WebView purchase flow; it does not — caused silent purchase failures. Use IndexedDB instead." / "Asumí que `localStorage` funciona dentro de un flujo de compra en WebView; no funciona — causó fallos de compra silenciosos. Usa IndexedDB."
- `skill` — `/verify-rls` — a 6-step Supabase RLS verification workflow that came up three times today. / un workflow de 6 pasos para verificar RLS en Supabase que apareció tres veces hoy.
- `project-doc` — "Run tests with `pnpm run test:unit`, not `npm test`. The latter triggers the e2e suite which needs a running DB." / "Corre tests con `pnpm run test:unit`, no `npm test`. El último dispara la suite e2e que necesita una DB activa."

---

## 4. Workflow (5 passes) / Workflow (5 pases)

Run these in order. Do not skip. Each pass has a hard output shape.

Ejecuta en orden. No saltes pasos. Cada pase tiene una forma de output estricta.

### Pass A — Scan / Escaneo

**EN.** Read the conversation transcript silently. Look for the patterns in
`references/signal-patterns.md` (multi-language). The high-signal classes:

1. **Explicit user corrections** (high confidence) — "no, do X instead",
   "actually that's wrong", "always do Y", "never do Z", "stop doing W",
   "the convention here is", and their Spanish counterparts in
   `references/signal-patterns.md`.
2. **Error → fix sequences** (high) — a tool call failed, a different call
   succeeded shortly after. The delta between them is the lesson.
3. **Repeated attempts** (medium) — three or more Edits to the same file in a
   row, three or more Bash retries of the same command with variations.
4. **User explanations of *why*** (high — Reflexion gold) — "the reason is",
   "because", "the gotcha is", "porque", "el detalle es", "la trampa es".
5. **Workflows the user described step-by-step** (medium, candidate for a
   `skill` stub) — four or more sequential tool calls that the user explicitly
   walked through.

If `~/.claude/projects/<current-project-slug>/.aprende-signals.md` exists and
is non-empty, prepend its contents to the scratch list — those are signals
captured by the PostToolUse hook earlier in this session.

**ES.** Lee la transcripción de la conversación en silencio. Busca los
patrones de `references/signal-patterns.md` (multi-idioma). Las clases de
alta señal:

1. **Correcciones explícitas del usuario** (high) — "no, mejor X", "eso está
   mal", "siempre Y", "nunca Z", "deja de hacer W", "la convención aquí es".
2. **Secuencias error → arreglo** (high) — una llamada falló, otra distinta
   funcionó después. El delta es la lección.
3. **Intentos repetidos** (medium) — tres o más Edits al mismo archivo en
   fila, tres o más reintentos de Bash con variaciones.
4. **Explicaciones de *por qué* del usuario** (high — oro de Reflexion) —
   "porque", "el detalle es", "la trampa es", "the reason is".
5. **Workflows que el usuario explicó paso a paso** (medium, candidato a
   `skill` stub) — cuatro o más llamadas secuenciales que el usuario detalló.

Si `~/.claude/projects/<slug-del-proyecto>/.aprende-signals.md` existe y no
está vacío, anteponé su contenido a la lista — son señales capturadas por el
hook PostToolUse antes en esta sesión.

### Pass B — Generate / Generar

For each signal, draft a candidate item with this internal shape:

Para cada señal, draftea un candidato con esta forma interna:

```
{
  "category": "memory" | "lesson" | "skill" | "project-doc",
  "title": "<short imperative title, ≤ 60 chars>",
  "rationale": "<one sentence; what this captures and why>",
  "confidence": "high" | "medium" | "low",
  "source_excerpt": "<short verbatim quote or tool-result line, optional>"
}
```

**Confidence derivation (mandatory):**
- `high` — explicit user feedback in the conversation, **OR** error→fix with a
  user explanation, **OR** the same correction repeated by the user.
- `medium` — inferred pattern, single user comment without elaboration,
  error→fix without explanation.
- `low` — guess, single observation the model thinks *might* matter.

**Be liberal at this pass.** It's cheaper to filter at confirmation than to
miss a real learning. Cap the candidate list at **15 items** per run; if you
find more, keep the 15 highest-confidence and tell the user to re-run.

**Sé liberal en este pase.** Es más barato filtrar en la confirmación que
perder un aprendizaje real. Limita la lista a **15 items** por corrida; si
encuentras más, conserva los 15 de mayor confidence y dile al usuario que
vuelva a correr.

### Pass C — Dedup / Deduplicar

Before showing the list, check overlaps **without dropping silently**:

Antes de mostrar la lista, chequea overlaps **sin dropear en silencio**:

1. Read `~/.claude/projects/<slug>/memory/MEMORY.md` if it exists. For each
   candidate, do a title + topic similarity check against existing bullets.
2. For `skill` candidates, `ls ~/.claude/skills/` and `ls ./.claude/skills/`
   (if the project-local folder exists).
3. For `project-doc` candidates, `grep -i <keyword>` against `./CLAUDE.md` and
   `./AGENTS.md` (if either exists).
4. If a candidate looks like a near-duplicate of an existing entry, **do not
   drop it**. Annotate it `[overlaps with: <existing-name-or-path>]` in the
   numbered list so the user can decide whether to skip, edit, or replace.

### Pass D — Confirm / Confirmar

Output **exactly** this template (substitute values, keep the structure):

Imprime **exactamente** esta plantilla (sustituye valores, mantén la estructura):

```
Found N candidate learnings from this conversation.
Encontré N aprendizajes candidatos en esta conversación.

Reply with: numbers (e.g. 1,3,5), ranges (1-4), "all", "none", or
"edit N: <new wording>" / "drop low" / "skip N".

Responde con: números (ej. 1,3,5), rangos (1-4), "all", "none", o
"edit N: <nueva descripción>" / "drop low" / "skip N".

 1. [memory]      <title> — <rationale>  (<confidence>)
 2. [lesson]      <title> — <rationale>  (<confidence>)  [overlaps with: <name>]
 3. [skill]       <title> — <rationale>  (<confidence>)
 4. [project-doc] <title> — <rationale>  (<confidence>)
 ...

>
```

Then **wait**. Do **not** call Write, Edit, or any file-mutating tool until
the user replies. This is the most important rule in this skill.

Después **espera**. **No** llames Write, Edit, ni ninguna herramienta que
modifique archivos hasta que el usuario responda. Esta es la regla más
importante del skill.

Accepted inputs / Inputs aceptados:
- Comma-separated numbers: `1,3,5`
- Ranges: `1-4` or `1-3,7,9-11`
- `all` — accept everything as shown
- `none` — accept nothing, exit cleanly
- `edit 5: <new wording>` — replace the candidate's rationale/title before saving
- `skip 3` — accept all except the listed numbers
- `drop low` — filter out everything below the named confidence band (`drop low`, `drop medium`)

If the input is ambiguous, ask once. Do not guess.

Si el input es ambiguo, pregunta una vez. No adivines.

### Pass E — Execute / Ejecutar

For each confirmed candidate, run the **category-specific write procedure**:

Para cada candidato confirmado, ejecuta el **procedimiento de escritura por
categoría**:

#### `memory`

1. Determine `<slug>` for the current project: read `pwd`, then convert
   `/Users/soyenrique/Desktop/aprende-skill` to `-Users-soyenrique-Desktop-aprende-skill`
   (replace `/` with `-`, drop leading dash, keep dashes). The folder is
   `~/.claude/projects/<slug>/memory/`. Create it if missing (`mkdir -p`).
2. Pick a filename: kebab-case slug from the title, prefixed by `metadata.type`
   (e.g. `feedback_pnpm-over-npm.md`, `project_supabase-rls-policy.md`).
   If a file with that name exists, append `-2`, `-3`, ... **Never overwrite.**
3. Write the file with the frontmatter and body spec from
   `references/memory-format.md`.
4. Append a one-line entry to `~/.claude/projects/<slug>/memory/MEMORY.md`:
   `- [<Title>](<filename>.md) — <one-sentence hook>`.

#### `lesson`

1. Same folder as `memory`. Filename starts with `lesson_` (e.g.
   `lesson_webview-assumed-localstorage.md`).
2. Use the strict frontmatter and four mandatory subheads from
   `references/lesson-format.md`:
   - `**What happened / Qué pasó:**`
   - `**Why it happened / Por qué pasó:**`
   - `**How to avoid / Cómo evitar:**`
   - `**Detection signal / Señal de detección:**`
3. Append to `MEMORY.md` under a `## Lessons / Lecciones` subsection (create
   the subsection if missing).

#### `skill` (stub)

1. Decide scope: user-global (`~/.claude/skills/<slug>/`) by default;
   project-local (`./.claude/skills/<slug>/`) only if the workflow references
   repo-specific paths or tools.
2. Create the folder. Write `SKILL.md` as a **stub**, not a full skill — use
   `references/skill-stub-template.md`. Fill in only what the conversation
   shows; mark the rest `[STUB — fill in: ...]`.
3. Print a one-line reminder: "Skill stub written at `<path>`. Run the
   skill-creator plugin (or edit manually) to flesh it out before publishing."

#### `project-doc`

1. Decide scope: project-level (`./CLAUDE.md` and `./AGENTS.md` — dual-write)
   by default; global (`~/.claude/CLAUDE.md` and `~/.claude/AGENTS.md`) only
   if the candidate is repo-agnostic.
2. **Extra confirmation** for global writes: prompt the user one more time
   before touching `~/.claude/CLAUDE.md` or `~/.claude/AGENTS.md`. Global
   docs affect every session on this machine.
3. Read the target file. Find the best existing section (e.g. `## Commands`,
   `## Conventions`). Append under it.
4. If no good section exists, create a `## Learnings (added by /aprende)`
   section at the end of the file.
5. Mark each appended line with an HTML comment for later audit:
   `<!-- /aprende YYYY-MM-DD -->`.
6. Dual-write to **both** `CLAUDE.md` and `AGENTS.md`. If one doesn't exist,
   create it with the entry alone. Content is identical between the two.

After all writes, emit one confirmation line per write:

Después de cada escritura, imprime una línea de confirmación:

```
✓ memory   → ~/.claude/projects/.../feedback_pnpm-over-npm.md  (+MEMORY.md)
✓ lesson   → ~/.claude/projects/.../lesson_webview-localstorage.md  (+MEMORY.md)
✓ skill    → ~/.claude/skills/verify-rls/SKILL.md  (stub — finish before use)
✓ project  → ./CLAUDE.md + ./AGENTS.md  (## Commands)
```

End with a one-paragraph summary of what was learned and a pointer to
`/aprende --review` for later pruning.

Termina con un párrafo resumen de lo aprendido y un puntero a
`/aprende --review` para podar después.

---

## 5. Output formats / Formatos de salida

The strict specs live in separate references so this file stays scannable:

Las especificaciones estrictas están en references separadas para que este
archivo siga siendo fácil de escanear:

- `references/memory-format.md` — frontmatter + body for `type: user|project|reference|feedback`.
- `references/lesson-format.md` — frontmatter + 4 mandatory subheads (Reflexion).
- `references/skill-stub-template.md` — bare SKILL.md scaffold.
- `references/signal-patterns.md` — multi-language correction phrases and detection heuristics.
- `references/review-workflow.md` — semantics of `/aprende --review`.

The `lesson` format is the most important; here it is inline as well:

El formato `lesson` es el más importante; aquí va inline también:

```markdown
---
name: lesson_<short-slug>
description: One-sentence summary of the mistake and its corrective rule.
metadata:
  type: lesson
  confidence: high | medium | low
  status: active   # active | retired | superseded-by-<name>
  createdAt: YYYY-MM-DD
  lastValidated: YYYY-MM-DD
  originSessionId: <session-id or omit>
---

**What happened / Qué pasó:** <factual paragraph, one to three sentences>

**Why it happened / Por qué pasó:** <root cause — not the symptom>

**How to avoid / Cómo evitar:** <concrete rule the next agent should follow>

**Detection signal / Señal de detección:** <how a future run knows it's about to repeat this>

Related: [[other-memory-name]]
```

---

## 6. `--review` mode / modo `--review`

When invoked as `/aprende --review`:

Cuando se invoca como `/aprende --review`:

1. Read every `metadata.type: lesson` file in the current project's memory
   folder, sorted by `lastValidated` ascending (oldest first).
2. For each, show: title, `confidence`, `status`, `lastValidated`, and the
   one-sentence `description`.
3. Prompt per-lesson: `Still valid? [y/n/edit/skip]`
   - `y` — bump `lastValidated` to today's date.
   - `n` — set `status: retired`. **Do not delete the file.**
   - `edit` — show the full body, let the user paste a new version inline, then
     overwrite (and bump `lastValidated`).
   - `skip` — leave untouched.
4. At the end, print a summary: `N validated, M retired, K edited, L skipped`.

Lessons with `status: retired` are skipped by future `/aprende` runs when
reading memory at session start.

Las lecciones con `status: retired` se ignoran en futuras corridas de
`/aprende` cuando lee memoria al inicio de la sesión.

Full procedure: `references/review-workflow.md`.

---

## 7. `--portable` mode / modo `--portable`

When invoked as `/aprende --portable`:

Cuando se invoca como `/aprende --portable`:

1. Run the standard 5-pass flow as usual.
2. After the normal writes for `lesson` candidates, **also** mirror each
   lesson file to `./.aprende/lessons/<filename>.md` in the project root.
3. Update `./.aprende/index.md` with a one-line entry per lesson — Codex and
   other tools can read this from `AGENTS.md` instructions.
4. The first time `--portable` is used in a project, append this line to
   `./AGENTS.md` (creating it if missing):
   ```
   Before any non-trivial change, read `.aprende/index.md` for prior lessons.
   Antes de cualquier cambio no trivial, lee `.aprende/index.md` para ver lecciones previas.
   ```

This is **off by default.** Plain `/aprende` does not write `./.aprende/`.

Esto está **apagado por defecto.** Un `/aprende` normal no escribe `./.aprende/`.

---

## 8. Examples / Ejemplos

### Example 1 — explicit correction / corrección explícita

User said earlier in the session: *"No, in this repo we use spaces, not tabs.
Always 2 spaces."*

User invokes: `/aprende`

Expected output:

```
Found 1 candidate learning from this conversation.

 1. [project-doc] Indent with 2 spaces, not tabs — user stated repo convention explicitly  (high)

>
```

User: `1`

Execution:
```
✓ project  → ./CLAUDE.md + ./AGENTS.md  (## Conventions)
```

`./CLAUDE.md` now contains, under `## Conventions`:
```
- Indent with 2 spaces, not tabs. <!-- /aprende 2026-05-11 -->
```
`./AGENTS.md` mirrors the same line.

### Example 2 — error→fix lesson / lección error→arreglo

Session contained: Bash call `npm test` failed with "no test command"; user
said *"oh, this project uses pnpm"*; Bash call `pnpm test` succeeded.

User invokes: `/aprende`

Expected output:

```
Found 2 candidate learnings from this conversation.

 1. [lesson]      Don't default to npm in this repo — pnpm is the package manager  (high)
 2. [project-doc] Test command is `pnpm test`, not `npm test`  (high)

>
```

User: `all`

Execution: writes lesson file + project-doc append, MEMORY.md updated.

---

## 9. Safety / Guardrails

**EN — Hard rules:**

1. **Never write before confirmation.** No Write, Edit, or destructive Bash
   call may run between Pass D's output and the user's reply. Repeat: never.
2. **Never overwrite an existing file.** Always append, or create with a
   unique name (`-2`, `-3` suffix).
3. **Never delete a lesson.** Use `metadata.status: retired`.
4. **Extra confirmation for global writes.** Touching `~/.claude/CLAUDE.md`
   or `~/.claude/AGENTS.md` requires a second user yes.
5. **Dedup annotates, does not drop.** Let the user decide on overlaps.
6. **Cap at 15 candidates per run.** Forces focus.
7. **Confidence labels are mandatory.** No item ships without `(high|medium|low)`.
8. **Hooks never write learnings.** `capture-signal.sh` only appends signal
   records; `stop-suggest.sh` only emits text. Learnings are written exclusively
   by the user-confirmed `/aprende` flow.
9. **If unsure, prefer the false-negative.** Tell the user "I'm not confident
   this is a learning — re-run `/aprende` later if it repeats."

**ES — Reglas duras:**

1. **Nunca escribas antes de la confirmación.** Ninguna llamada Write, Edit, o
   Bash destructiva puede correr entre el output del Pase D y la respuesta del
   usuario. Repito: nunca.
2. **Nunca sobrescribas un archivo existente.** Siempre appendea, o crea con
   un nombre único (`-2`, `-3`).
3. **Nunca elimines una lección.** Usa `metadata.status: retired`.
4. **Confirmación extra para escrituras globales.** Tocar
   `~/.claude/CLAUDE.md` o `~/.claude/AGENTS.md` requiere un segundo sí del
   usuario.
5. **El dedup anota, no dropea.** Que el usuario decida sobre los overlaps.
6. **Tope de 15 candidatos por corrida.** Fuerza foco.
7. **Las etiquetas de confidence son obligatorias.** Ningún item sale sin
   `(high|medium|low)`.
8. **Los hooks nunca escriben aprendizajes.** `capture-signal.sh` solo
   appendea registros de señales; `stop-suggest.sh` solo emite texto. Los
   aprendizajes se escriben exclusivamente por el flujo `/aprende` confirmado.
9. **Si tienes dudas, prefiere el falso negativo.** Dile al usuario "no estoy
   seguro de que esto sea un aprendizaje — vuelve a correr `/aprende` si se
   repite."

---

## 10. Project-slug derivation / Derivación del slug del proyecto

The memory folder is `~/.claude/projects/<slug>/memory/`. To get `<slug>`:

La carpeta de memoria es `~/.claude/projects/<slug>/memory/`. Para obtener `<slug>`:

1. Read `pwd` (the current working directory absolute path).
2. Replace every character that is **not** a letter or digit (`A–Z`, `a–z`,
   `0–9`) with `-`. This is Claude Code's own project-folder convention, so the
   slug matches for **every** path — including Windows paths like
   `D:/proyectos_python/...` and any path containing `_`, `.`, `:`, `\` etc.
   (Replacing only `/` would mis-slug and read from the wrong folder.)
3. If the result starts with `-`, that leading dash stays (matches the
   existing convention — `~/.claude/projects/-Users-soyenrique-Desktop-aprende-skill/`).

Example (macOS/Linux): `pwd` = `/Users/soyenrique/Desktop/myproject`
→ slug = `-Users-soyenrique-Desktop-myproject`
→ folder = `~/.claude/projects/-Users-soyenrique-Desktop-myproject/memory/`

Example (Windows): `pwd` = `D:/proyectos_python/myproject`
→ slug = `D--proyectos-python-myproject`
→ folder = `~/.claude/projects/D--proyectos-python-myproject/memory/`

If the folder does not exist, create it with `mkdir -p`. Also create
`MEMORY.md` with a single-line header (`# Memory Index`) if it's missing.

Si la carpeta no existe, créala con `mkdir -p`. También crea `MEMORY.md` con
un header de una línea (`# Memory Index`) si no existe.

---

## 11. Integration with the optional hooks / Integración con los hooks opcionales

If the plugin's hooks are enabled (they ship ON by default), this skill
benefits from them but **never depends on them**:

Si los hooks del plugin están activos (vienen ON por defecto), este skill se
beneficia de ellos pero **nunca depende de ellos**:

- **PostToolUse** writes per-session signal records to
  `~/.claude/projects/<slug>/.aprende-signals.md`. Pass A reads this file
  if it exists and prepends its content to the scratch list.
- **Stop** reads the same file at session end and emits an
  `additionalContext` reminder if signals exist and `/aprende` was not run.

After a successful `/aprende` run (one that produced at least one
confirmed write), delete `.aprende-signals.md` to mark the signals as
consumed.

Después de una corrida exitosa de `/aprende` (que produjo al menos una
escritura confirmada), borra `.aprende-signals.md` para marcar las señales
como consumidas.

---

## 12. Cross-tool note / Nota cross-tool

This skill is designed to work in both **Claude Code** and **Codex**:

Este skill está diseñado para funcionar tanto en **Claude Code** como **Codex**:

- `project-doc` writes always dual-write to `CLAUDE.md` and `AGENTS.md`.
  Codex reads `AGENTS.md`; Claude Code reads `CLAUDE.md`. Same content in
  both. No symlinks, no imports.
- For `memory` and `lesson`, use `/aprende --portable` to mirror to
  `./.aprende/` in the project root. Codex can then read
  `.aprende/index.md` per the line auto-added to `AGENTS.md`.
- The skill itself (`skills/aprende/SKILL.md`) is plain Markdown with YAML
  frontmatter — readable by any agent that supports the agentskills.io
  convention.

---

## 13. Quick reference / Referencia rápida

| Command | Effect |
|---------|--------|
| `/aprende` | Standard run — review conversation, prompt, write. |
| `/learn` | English alias for `/aprende`. |
| `/aprende --review` | Revisit existing lessons; mark retired or refresh. |
| `/aprende --portable` | Standard run + mirror lessons to `./.aprende/`. |
| `/aprende --dry-run` | Run passes A-D but skip the write pass. Preview only. |
| `/aprende-enable-hooks` | Install PostToolUse + Stop hooks into `~/.claude/settings.json`. |
| `/aprende-disable-hooks` | Remove those hooks. |

---

*Made with discipline against false positives. / Hecho con disciplina contra
los falsos positivos.*

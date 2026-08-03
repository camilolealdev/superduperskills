# `memory` file format / Formato de archivo `memory`

This is the **exact** frontmatter and body specification for files saved under
`~/.claude/projects/<slug>/memory/` when the category is `memory` (not
`lesson` — see `lesson-format.md`).

Esta es la especificación **exacta** del frontmatter y cuerpo para archivos
guardados en `~/.claude/projects/<slug>/memory/` cuando la categoría es
`memory` (no `lesson` — ver `lesson-format.md`).

---

## Frontmatter (required / obligatorio)

```yaml
---
name: <kebab-case-slug>            # matches the filename without .md
description: <one-line summary used to decide relevance at recall time>
metadata:
  type: user | feedback | project | reference
  createdAt: YYYY-MM-DD
  originSessionId: <session-id, if known; else omit>
---
```

### `metadata.type` semantics

- **`user`** — who the user is: role, expertise, stable preferences ("user
  always wants pnpm, not npm").
- **`feedback`** — guidance the user gave about how the agent should work
  (corrections, confirmed approaches). Body must include `**Why:**` and
  `**How to apply:**` lines.
- **`project`** — ongoing work, goals, constraints not derivable from code or
  git history. Convert relative dates to absolute. Body should include
  `**Why:**` and `**How to apply:**` lines.
- **`reference`** — pointers to external resources (URLs, dashboards, tickets).

Use **`lesson`** only via `lesson-format.md` — it has stricter body
requirements.

Usa **`lesson`** solo vía `lesson-format.md` — tiene requisitos de cuerpo
más estrictos.

---

## Body / Cuerpo

Free-form Markdown. Recommended structure for `feedback` and `project`:

Markdown libre. Estructura recomendada para `feedback` y `project`:

```markdown
<one paragraph: the fact, the rule, or the context>

**Why:** <one sentence — why this matters>

**How to apply:** <one sentence — what the next agent should do differently>

Related: [[other-memory-name]]   # link to another memory by its `name:` slug
```

For `user`-type memories, one paragraph is usually enough; no `Why/How`
required.

Para memorias `user`, suele bastar un párrafo; no se requiere `Why/How`.

For `reference`-type memories, link + one-line context is enough:

Para memorias `reference`, link + una línea de contexto es suficiente:

```markdown
<URL or pointer> — <what it is, why we'd want to find it later>
```

---

## Cross-linking / Enlazado

Use `[[<other-memory-name>]]` to link to another memory. The name is the
other memory's `name:` slug. Linking liberally is fine; a `[[name]]` that
doesn't match an existing memory yet is fine too — it marks something worth
writing later.

Usa `[[<otro-nombre-de-memoria>]]` para enlazar a otra memoria. El nombre es
el slug `name:` de la otra. Linkear con libertad está bien; un `[[name]]` que
todavía no apunta a una memoria existente está bien — marca algo que vale la
pena escribir después.

---

## Filename convention / Convención de nombre de archivo

`<type>_<short-slug>.md` — e.g.:

- `feedback_pnpm-over-npm.md`
- `user_prefers-vim-mode.md`
- `project_supabase-rls-strict-mode.md`
- `reference_company-style-guide.md`

If a file with the chosen name exists, append `-2`, `-3`, etc. **Never
overwrite.** The skill must error out before overwriting an existing memory
file.

Si un archivo con el nombre elegido existe, appendea `-2`, `-3`, etc. **Nunca
sobrescribas.** El skill debe fallar antes de sobrescribir un archivo de
memoria existente.

---

## MEMORY.md index entry / Entrada en MEMORY.md

After writing the file, append one line to
`~/.claude/projects/<slug>/memory/MEMORY.md`:

Después de escribir el archivo, appendea una línea a
`~/.claude/projects/<slug>/memory/MEMORY.md`:

```
- [<Human-readable title>](<filename>.md) — <one-sentence hook>
```

If `MEMORY.md` does not exist, create it with a single-line header
(`# Memory Index`) before appending.

Si `MEMORY.md` no existe, créalo con un header de una línea
(`# Memory Index`) antes de appendear.

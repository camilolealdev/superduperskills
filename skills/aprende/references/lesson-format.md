# `lesson` file format / Formato de archivo `lesson`

This is the **exact** frontmatter and body specification for `lesson` files
(anti-patterns / Reflexion-style mistake records) saved under
`~/.claude/projects/<slug>/memory/`. A `lesson` is structurally distinct
from a `memory` because every lesson must answer four questions: *what,
why, how-to-avoid, detection-signal*.

Esta es la especificación **exacta** del frontmatter y cuerpo para archivos
`lesson` (anti-patrones / registros de error estilo Reflexion) guardados en
`~/.claude/projects/<slug>/memory/`. Una `lesson` es estructuralmente
distinta de una `memory` porque cada lección debe responder cuatro
preguntas: *qué, por qué, cómo evitar, señal de detección*.

---

## Frontmatter (required / obligatorio)

```yaml
---
name: lesson_<short-slug>
description: <one sentence — the mistake and its corrective rule, together>
metadata:
  type: lesson
  confidence: high | medium | low
  status: active                   # active | retired | superseded-by-<name>
  createdAt: YYYY-MM-DD
  lastValidated: YYYY-MM-DD
  originSessionId: <session-id, if known; else omit>
---
```

### Field semantics

- **`type: lesson`** — distinguishes this from `user/feedback/project/reference`.
- **`confidence`** — required, must be present. Used by `/aprende --review`
  and by future runs deciding which lessons to surface.
- **`status`**:
  - `active` (default) — show this in future sessions.
  - `retired` — kept on disk for audit, but skipped by `/aprende` reading
    memory. Set by `/aprende --review` when the user marks the lesson no
    longer valid.
  - `superseded-by-<other-name>` — kept on disk; replaced by a newer lesson.
- **`lastValidated`** — bumped by `/aprende --review` on `y` (still valid)
  or `edit` (refreshed). Used to sort the review queue (oldest first).

---

## Body (mandatory four sections / cuatro secciones obligatorias)

These four subheads are **required**, in this order, with both languages:

Estos cuatro subheads son **obligatorios**, en este orden, con ambos idiomas:

```markdown
**What happened / Qué pasó:** <one to three sentences. Factual. The specific
mistake that occurred in the session, not a generalization.>

**Why it happened / Por qué pasó:** <root cause. Not the symptom. If the
user explained it, prefer their wording. Reflexion lift comes from this
field being accurate.>

**How to avoid / Cómo evitar:** <concrete, actionable rule for the next
agent. Imperative voice. "Use IndexedDB inside WebViews" beats "be careful
with storage".>

**Detection signal / Señal de detección:** <how a future run knows it is
about to repeat this. A code shape, a tool call pattern, a context keyword,
a file path, a stack trace fragment. The thing to grep for.>
```

After the four sections, optional `Related:` line linking to other memories
or lessons:

Después de las cuatro secciones, una línea `Related:` opcional enlazando a
otras memorias o lecciones:

```markdown
Related: [[other-lesson-name]] [[some-feedback-memory]]
```

---

## Filename convention / Convención de nombre de archivo

`lesson_<short-slug>.md` — e.g.:

- `lesson_webview-assumed-localstorage.md`
- `lesson_npm-default-wrong-on-pnpm-repo.md`
- `lesson_rls-policy-needs-using-and-with-check.md`

If a file with the chosen name exists, append `-2`, `-3`, etc. **Never
overwrite.**

Si un archivo con el nombre elegido existe, appendea `-2`, `-3`, etc.
**Nunca sobrescribas.**

---

## MEMORY.md index entry / Entrada en MEMORY.md

Append the lesson under a `## Lessons / Lecciones` subsection in
`MEMORY.md` (create the subsection if missing):

Appendea la lección bajo una subsección `## Lessons / Lecciones` en
`MEMORY.md` (crea la subsección si no existe):

```markdown
## Lessons / Lecciones

- [<Title>](<filename>.md) — <one-sentence hook>  *(high)*
```

The confidence label in italics at the end is optional but encouraged —
makes the index scannable for "what are the high-confidence rules?".

La etiqueta de confidence en cursiva al final es opcional pero recomendada —
hace que el índice sea fácil de escanear para "¿cuáles son las reglas de
alta confidence?".

---

## Worked example / Ejemplo trabajado

`lesson_webview-assumed-localstorage.md`:

```markdown
---
name: lesson_webview-assumed-localstorage
description: localStorage inside a purchase WebView fails silently — use IndexedDB.
metadata:
  type: lesson
  confidence: high
  status: active
  createdAt: 2026-05-11
  lastValidated: 2026-05-11
---

**What happened / Qué pasó:** A purchase flow stored a transaction token in
`localStorage` inside a WebView; the token vanished between page navigations
and purchases failed silently. *Un flujo de compra guardó un token en
`localStorage` dentro de un WebView; el token desapareció entre navegaciones
y las compras fallaron en silencio.*

**Why it happened / Por qué pasó:** WebViews in our build do not persist
`localStorage` across navigations under certain isolation modes. The
behavior is platform-specific and not documented in the framework's
README. *Los WebViews en nuestro build no persisten `localStorage` entre
navegaciones bajo ciertos modos de aislamiento. El comportamiento es
específico de plataforma y no está documentado en el README del framework.*

**How to avoid / Cómo evitar:** Use `IndexedDB` (or a server-side session)
for any state that must survive WebView navigations. Never trust
`localStorage` inside a purchase or auth WebView. *Usa `IndexedDB` (o una
sesión server-side) para cualquier estado que deba sobrevivir navegaciones
en WebView. Nunca confíes en `localStorage` dentro de un WebView de compra
o auth.*

**Detection signal / Señal de detección:** Code in `src/checkout/**` or
`src/purchase/**` that calls `localStorage.setItem` or
`localStorage.getItem` should be flagged. Also: any `window.location`
change followed by a `localStorage.getItem` that returns `null` in a
purchase context. *Código en `src/checkout/**` o `src/purchase/**` que llame
`localStorage.setItem` o `localStorage.getItem` debe ser marcado. También:
cualquier cambio de `window.location` seguido de un `localStorage.getItem`
que devuelve `null` en contexto de compra.*

Related: [[project_webview-state-management]]
```

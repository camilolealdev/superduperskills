# Confirmation prompt template / Plantilla del prompt de confirmación

This is the **literal output** the model must produce at the end of Pass D
(after scanning, generating, and dedup). It is the most-read part of the
skill — copy it exactly, substituting values.

Este es el **output literal** que el modelo debe producir al final del
Pase D. Copia exacta, sustituye valores.

---

## Template

```
Found N candidate learnings from this conversation.
Encontré N aprendizajes candidatos en esta conversación.

Reply with: numbers (e.g. 1,3,5), ranges (1-4), "all", "none", or
"edit N: <new wording>" / "drop low" / "skip N".

Responde con: números (ej. 1,3,5), rangos (1-4), "all", "none", o
"edit N: <nueva descripción>" / "drop low" / "skip N".

 1. [memory]      <title> — <one-sentence rationale>  (<confidence>)
 2. [lesson]      <title> — <one-sentence rationale>  (<confidence>)  [overlaps with: <name>]
 3. [skill]       <title> — <one-sentence rationale>  (<confidence>)
 4. [project-doc] <title> — <one-sentence rationale>  (<confidence>)
 ...

>
```

---

## Formatting rules / Reglas de formato

1. **Number column** — right-aligned in a 2-char field. The skill caps at
   15 candidates, so `15` is the widest. Use `%2d` formatting.
2. **Category column** — left-aligned in a 13-char field. The four
   categories are `memory`, `lesson`, `skill`, `project-doc`.
3. **Title and rationale** — one sentence each, joined by ` — `.
4. **Confidence** — in parentheses at the end, lowercased:
   `(high)`, `(medium)`, `(low)`.
5. **Overlap annotation** (optional) — square brackets after the confidence:
   `[overlaps with: <name>]`. Use this when Pass C found a similar existing
   entry. Never drop a candidate silently because of overlap.

---

## After printing, WAIT / Después de imprimir, ESPERA

Do not call any tool that modifies files (Write, Edit, destructive Bash)
until the user replies. Read the user's reply, then proceed to Pass E.

No llames ninguna herramienta que modifique archivos hasta que el usuario
responda. Lee la respuesta, luego pasa al Pase E.

---

## Accepted inputs / Inputs aceptados

| Input | Effect / Efecto |
|-------|-----------------|
| `1,3,5` | Save candidates 1, 3, 5. / Guarda candidatos 1, 3, 5. |
| `1-4` | Save 1 through 4 inclusive. / Guarda del 1 al 4 inclusive. |
| `1-3,7,9-11` | Combinations. / Combinaciones. |
| `all` | Save every candidate. / Guarda todos los candidatos. |
| `none` | Save nothing, exit. / No guarda nada, sale. |
| `edit 5: <text>` | Replace candidate 5's title/rationale with `<text>` before saving. / Reemplaza candidato 5 con `<text>`. |
| `skip 3` | Save all except 3. / Guarda todos menos 3. |
| `skip 2,5` | Save all except 2 and 5. / Guarda todos menos 2 y 5. |
| `drop low` | Discard all `(low)` candidates; save the rest. / Descarta los `(low)`; guarda el resto. |
| `drop medium` | Discard `(low)` AND `(medium)`; save only `(high)`. / Descarta `(low)` Y `(medium)`. |

If the input is ambiguous, ask once. Do not guess.

Si el input es ambiguo, pregunta una vez. No adivines.

---

## Worked example / Ejemplo trabajado

After a session where the user corrected the agent on package manager and
explained a WebView purchase bug, Pass D would print:

```
Found 3 candidate learnings from this conversation.
Encontré 3 aprendizajes candidatos en esta conversación.

Reply with: numbers (e.g. 1,3,5), ranges (1-4), "all", "none", or
"edit N: <new wording>" / "drop low" / "skip N".

Responde con: números (ej. 1,3,5), rangos (1-4), "all", "none", o
"edit N: <nueva descripción>" / "drop low" / "skip N".

 1. [project-doc] Use pnpm, not npm — user said "this repo uses pnpm"  (high)
 2. [lesson]      localStorage fails in purchase WebView — use IndexedDB  (high)
 3. [memory]      User prefers explicit error messages in tests  (medium)

>
```

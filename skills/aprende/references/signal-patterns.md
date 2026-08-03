# Signal patterns / Patrones de señal

Multi-language correction patterns and detection heuristics for Pass A of
`/aprende`. Liberal at this layer (false positives are filtered at
confirmation).

Patrones de corrección multi-idioma y heurísticas de detección para el
Pase A de `/aprende`. Liberal en esta capa (los falsos positivos se filtran
en la confirmación).

---

## 1. Explicit user correction phrases (HIGH confidence)

### English
- `no, do X instead`
- `actually, X` / `actually that's wrong`
- `not X, Y`
- `stop doing X`
- `always X` / `never X`
- `the convention here is X`
- `we use X (not Y) in this repo`
- `I told you (already) to`
- `don't (ever)`
- `correction:` / `fix:` (in chat)
- `the right way is`

### Español
- `no, mejor X` / `no, usa X`
- `en realidad, X` / `eso está mal`
- `no es X, es Y`
- `deja de hacer X` / `para de hacer X`
- `siempre X` / `nunca X`
- `la convención aquí es X`
- `aquí usamos X (no Y)` / `en este repo usamos X`
- `ya te dije`
- `nunca / jamás`
- `corrección:` / `arreglo:`
- `lo correcto es`

**Heuristic:** these phrases in a user turn that immediately follows or
soon follows an agent action are HIGH confidence. The same phrase in a
question or hypothetical is not a correction.

**Heurística:** estas frases en un turno del usuario inmediatamente o poco
después de una acción del agente son HIGH confidence. La misma frase en una
pregunta o hipotético no es una corrección.

---

## 2. Error → fix sequences

**Detection:** a tool call (Bash, Edit, Write) failed (non-zero exit code,
error in stderr, or test failure), followed within 3 turns by a different
tool call that succeeded at the same goal.

**Detección:** una llamada de herramienta (Bash, Edit, Write) falló (exit
code no-cero, error en stderr, o test fallido), seguida dentro de 3 turnos
por una llamada distinta que tuvo éxito en el mismo objetivo.

**Confidence:**
- HIGH if the user said *why* in between ("oh, this uses pnpm", "porque
  X").
- MEDIUM if the agent figured it out silently.

**The lesson is the delta** — what was different between the failed and
successful call. Save *that*, not the failure itself.

**La lección es el delta** — qué cambió entre la llamada fallida y la
exitosa. Guarda *eso*, no el fallo en sí.

---

## 3. Repeated attempts (MEDIUM)

**Detection:**
- 3+ Edits to the same file within a 5-turn window.
- 3+ Bash calls with the same command prefix and minor variations
  (`npm test` → `npm run test` → `npm run test:unit`).
- 2+ retries of the same tool with a slight argument change.

**Why it matters:** repetition is a signal the agent doesn't have the
right model of the task. Even if it eventually succeeds, the *converged*
form is the lesson.

**Por qué importa:** la repetición indica que el agente no tiene el modelo
correcto de la tarea. Aun si eventualmente funciona, la forma *convergida*
es la lección.

---

## 4. User explanations of *why* (HIGH — Reflexion gold)

### English
- `the reason is X`
- `because X`
- `the gotcha is X`
- `the catch is X`
- `the trick is`
- `what's happening is`

### Español
- `la razón es X`
- `porque X`
- `el detalle es X`
- `la trampa es X`
- `el truco es`
- `lo que pasa es`

**Capture rule:** when a user explains *why*, the explanation is the *Why
it happened* field of a `lesson`. Do not paraphrase aggressively — keep
the user's wording where it's compact and clear.

**Regla de captura:** cuando el usuario explica *por qué*, la explicación
es el campo *Why it happened* de una `lesson`. No parafrasees agresivamente
— mantén las palabras del usuario donde sean compactas y claras.

---

## 5. Workflows worth a `skill` stub (MEDIUM)

**Detection:** 4+ sequential tool calls forming a coherent workflow that:
- The user described step-by-step *before* the agent did them, OR
- Came up earlier in the same session in a similar form, OR
- The user explicitly named ("the deploy process", "the RLS check").

**Capture rule:** draft a SKILL.md stub. Do **not** fill it in completely
— a full skill from one observation is high false-positive territory.
Stub the trigger and the steps; flag the rest with `[STUB — fill in: ...]`.

**Regla de captura:** draftea un stub de SKILL.md. **No** lo completes — un
skill completo a partir de una sola observación tiene alto riesgo de falsos
positivos. Stub el trigger y los pasos; marca el resto con
`[STUB — completar: ...]`.

---

## 6. Project-doc candidates (HIGH if mentioned explicitly)

**Detection:**
- User mentioned a build/test/run command.
- User mentioned a repo convention ("we use 2-space indent").
- User mentioned a gotcha that applies to every agent on this repo, not
  just this session ("the test DB must be running before running e2e").

**Capture rule:** these go to `./CLAUDE.md` AND `./AGENTS.md`. Same content
both files.

**Regla de captura:** van a `./CLAUDE.md` Y `./AGENTS.md`. Mismo contenido
en ambos archivos.

---

## 7. False-positive traps / Trampas de falso positivo

Do NOT capture / NO captures:

- Conversational pleasantries ("thanks!", "great!", "gracias").
- One-off observations the agent made that the user didn't validate.
- Repository facts already in `git log`, the README, or `CLAUDE.md` —
  they're already discoverable.
- Speculations ("maybe X is the issue").
- Apologies, hedging, self-corrections by the agent.

**When unsure, MEDIUM confidence** and let the user filter at
confirmation. If still unsure, do not generate the candidate at all
(false negative > false positive).

**Cuando dudes, MEDIUM confidence** y deja que el usuario filtre en la
confirmación. Si sigues dudando, no generes el candidato (falso negativo >
falso positivo).

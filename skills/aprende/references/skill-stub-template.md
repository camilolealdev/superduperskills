# Skill stub template / Plantilla de stub de skill

When `/aprende` produces a `skill` candidate, it writes a **stub** SKILL.md
— not a complete skill. The user finishes it. A full skill drafted from one
observation is high false-positive territory.

Cuando `/aprende` produce un candidato `skill`, escribe un SKILL.md **stub**
— no un skill completo. El usuario lo termina. Un skill completo drafteado
de una sola observación tiene alto riesgo de falsos positivos.

---

## Where it goes / Dónde va

- **User-global** (default): `~/.claude/skills/<slug>/SKILL.md`
- **Project-local**: `./.claude/skills/<slug>/SKILL.md`

Choose project-local only if the workflow references repo-specific paths
or tools (e.g. mentions `src/checkout/**` or runs a script that only
exists in this repo). Otherwise default to user-global.

Elige project-local solo si el workflow referencia paths o herramientas
específicas del repo. Si no, default a user-global.

---

## Exact stub content / Contenido exacto del stub

```markdown
---
name: <slug>
version: 0.0.1
description: |
  [STUB drafted by /aprende on YYYY-MM-DD]
  <one-sentence purpose based on the conversation>
  Trigger keywords: <words observed in the session>
allowed-tools:
  - Read
  - Edit
  - Bash
---

# <Title>

## When to invoke / Cuándo activarse

[STUB — fill in trigger conditions. From /aprende observation on
YYYY-MM-DD, this workflow appeared when: <one-line context>.]

[STUB — completa las condiciones del trigger. Por la observación de
/aprende el YYYY-MM-DD, este workflow apareció cuando: <contexto>.]

## Workflow / Workflow

[STUB — observed sequence from the conversation:

 1. <step from the conversation>
 2. <step from the conversation>
 3. <step from the conversation>
 4. ...

Refine these into clear, reusable instructions before publishing this
skill. Decide what's repeatable and what was session-specific.]

[STUB — secuencia observada en la conversación:

 1. <paso>
 2. <paso>
 ...

Refina estos pasos antes de publicar.]

## Examples / Ejemplos

[STUB — paste a transcript snippet here, or write a worked example.]

## Safety / Guardrails

[STUB — anything destructive in this workflow? Add safety rules.]
```

---

## Filename / Nombre del archivo

The `<slug>` should be a short, kebab-case noun-phrase or verb-phrase that
makes the skill easy to find. Examples:

- `verify-rls`
- `deploy-staging`
- `audit-css`
- `migrate-supabase-policy`

Do not collide with an installed skill. If the chosen `<slug>` exists,
prompt the user before overwriting (this is the only case where the user
might *intentionally* overwrite a stub — but ask first).

No colisiones con un skill instalado. Si el `<slug>` existe, pregúntale al
usuario antes de sobrescribir (es el único caso donde el usuario podría
querer sobrescribir un stub intencionalmente — pero pregunta primero).

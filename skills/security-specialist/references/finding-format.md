# Finding Format Specification

Este documento define a estrutura canônica de um security finding. Todo finding produzido pelo security-specialist DEVE conformar a este schema.

---

## Formato Simples (SQLite — uso interno)

Para persistência no scan.db e workflows modulares (discovery, triage, diff-review):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | UUID v4 | yes | Identificador único |
| `scan_id` | UUID v4 | yes | FK para scan session parent |
| `title` | string | yes | Nome da vulnerabilidade (≤ 80 chars) |
| `severity` | enum | yes | `critical`, `high`, `medium`, `low`, `info` |
| `category` | enum | yes | `injection`, `xss`, `auth`, `crypto`, `exposure`, `config`, `dependency`, `logic`, `other` |
| `status` | enum | yes | `open`, `fixed`, `false-positive`, `accepted-risk`, `tracked` |
| `file_path` | string | yes | Repo-relative path |
| `line_number` | integer | yes | Line onde a vulnerabilidade origina |
| `description` | string | yes | 2–4 frases explicando o quê e por quê importa |
| `evidence` | string | yes | Código, data flow trace, ou PoC |
| `remediation` | string | no | Fix sugerido |
| `tracking_url` | string | no | URL do issue tracker externo |
| `notes` | string | no | Notas de triage |
| `created_at` | string | yes | ISO 8601 timestamp |

---

## Formato Estruturado (JSON — output de full-scan pipeline)

Para findings que passam pela pipeline completa de 6 fases (full-scan), use o formato rico definido em `report-schema.json`. Este formato é **obrigatório** para o output `findings.json` do full-scan.

### Campos do Formato Estruturado

| Field | Description |
|-------|-------------|
| `verdict` | `confirmed` ou `rejected` |
| `title` | Título conciso e padronizado |
| `description` | Explicação completa com detalhes de reprodução |
| `root_cause` | Template: `[function] em [file] não [ação], permitindo [consequência]` |
| `intended_behavior` | O que o dev tentou construir (lógica não-vulnerável) |
| `trace` | Array sequencial: `entrypoint` → `propagation`* → `sink` |
| `conditions` | Pré-requisitos factuais para exploração |
| `execution` | Perspectiva do atacante, payloads, instruções, resultado esperado |
| `remediation` | Estratégia + code_changes opcionais |
| `severity` | Likelihood × Impact, cada com score + reason |
| `confidence` | Score (low/medium/high) + reason |

### Trace

Cada step do trace contém:
```json
{
  "kind": "entrypoint|propagation|sink",
  "file": "src/routes/users.js",
  "line": 42,
  "scope": "searchUsers",
  "description": "User input from query param 'q' enters the handler"
}
```

**Regras:**
- Mínimo 2 steps (entrypoint + sink)
- Primeiro step DEVE ser `kind: "entrypoint"`
- Último step DEVE ser `kind: "sink"`
- File paths relativos à raiz do repositório
- Scope é function/method name sem parênteses

### Conditions

Pré-requisitos factuais. Array vazio = explorável por default.
```json
{
  "kind": "authentication_level",
  "description": "Requires authenticated session with any role"
}
```

Kinds válidos: `authentication_level`, `authorization_role`, `user_interaction`, `system_configuration`, `network_routing`, `environmental_dependency`, `data_state`, `timing_dependency`, `third_party_dependency`

### Execution

```json
{
  "attacker_perspective": "Authenticated user with basic role",
  "payloads": ["GET /api/search?q=' UNION SELECT password FROM users--"],
  "instructions": [
    "Login with any valid account",
    "Navigate to search endpoint",
    "Inject SQL via query parameter"
  ],
  "expected_result": "Response contains all user password hashes"
}
```

### Confidence

```json
{
  "score": "high",
  "reason": "Full trace verified against source. All steps readable and confirmed."
}
```

- **high**: Trace completo verificado, exploit testável
- **medium**: Trace parcialmente verificado, algumas assumptions
- **low**: Static analysis only, complex routing, missing files

---

## Quando Usar Qual Formato

| Workflow | Formato |
|----------|---------|
| `full-scan` (pipeline 6 fases) | **Estruturado** (findings.json validado contra schema) |
| `discovery`, `diff-review`, `triage` | **Simples** (SQLite) |
| `pentest` | **Simples** (SQLite) + evidence expandida |
| `reporting` (HTML final) | Ambos — HTML renderiza de qualquer fonte |

---

## Validação

Para o formato estruturado, valide com:
```bash
node scripts/validate-findings.cjs .security/scans/<timestamp>/findings.json
```

O validador checa: required fields, enum values, structural constraints, `additionalProperties`, e semantic rules (trace starts at entrypoint, ends at sink).

---

## Exemplo: Formato Estruturado Completo

```json
{
  "verdict": "confirmed",
  "title": "SQL Injection in user search endpoint",
  "description": "User-supplied search parameter is concatenated directly into SQL query. Authenticated user can extract arbitrary data including credentials.",
  "root_cause": "searchUsers in src/routes/users.js does not parameterize user input, allowing arbitrary SQL execution.",
  "intended_behavior": "Search should filter users by name using parameterized queries, returning only matching records the caller is authorized to see.",
  "trace": [
    {
      "kind": "entrypoint",
      "file": "src/routes/users.js",
      "line": 35,
      "scope": "searchUsers",
      "description": "User input from req.query.search enters handler"
    },
    {
      "kind": "propagation",
      "file": "src/routes/users.js",
      "line": 42,
      "scope": "searchUsers",
      "description": "Input concatenated into SQL string template without escaping"
    },
    {
      "kind": "sink",
      "file": "src/routes/users.js",
      "line": 43,
      "scope": "searchUsers",
      "description": "Concatenated string passed to db.raw() for execution"
    }
  ],
  "conditions": [
    {
      "kind": "authentication_level",
      "description": "Requires valid session (any role)"
    }
  ],
  "execution": {
    "attacker_perspective": "Authenticated user with basic role",
    "payloads": ["GET /api/users?search=' UNION SELECT password FROM users--"],
    "instructions": [
      "Login with any valid account",
      "Send GET request to /api/users with crafted search parameter",
      "Observe response containing all password hashes"
    ],
    "expected_result": "Response body contains password hashes for all users in database"
  },
  "remediation": {
    "strategy": "Use parameterized queries via the ORM's query builder instead of string concatenation.",
    "code_changes": [
      {
        "file_name": "src/routes/users.js",
        "fixed_code": "const results = await db('users').where('name', 'like', `%${search}%`);"
      }
    ]
  },
  "severity": {
    "likelihood": { "score": "high", "reason": "Any authenticated user can exploit. No special tools needed." },
    "impact": { "score": "critical", "reason": "Full database read access including credentials and PII." },
    "overall_severity": "critical"
  },
  "confidence": {
    "score": "high",
    "reason": "Full trace verified. db.raw() confirmed at line 43. No parameterization in path."
  }
}
```

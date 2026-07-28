# Steering: Validate a Finding

Determine se um finding reportado é real e explorável. Produza um verdict: `confirmed`, `rejected`, ou `needs-more-info`.

## Princípio: Validação Adversarial

O agente que valida NUNCA deve ser o agente que encontrou o finding. Hunting agents são biased para encontrar coisas; validation agents são biased para matar false positives. Este step adversarial é crítico.

---

## Step 1: Load Finding Details

```bash
python3 scripts/scan_db.py show --finding-id <id>
```

Extraia:
- Tipo de vulnerabilidade claimed (CWE)
- Location (file, line, function, ou endpoint)
- Source do report (qual scanner, ou manual)
- Evidência ou PoC existente
- Trace claimed (se disponível)

## Step 2: Read the Code at the Finding Location

Abra o file. Leia a function. Entenda o que faz. Não confie no snippet do scanner — scanners truncam contexto e perdem surrounding logic.

Perguntas:
- O pattern que o scanner flagged realmente existe aqui?
- É dead code? (unreachable, commented out, behind permanent feature flag)
- Foi refatorado desde o scan? (cheque git log)
- Se o código não bate com o report → provável **false positive** de resultados stale.

## Step 3: Testes de Validação (5 Gates)

Aplique **todos** os testes abaixo. O finding deve sobreviver cada um:

### 3a. Exploitation Test
Leia o código real em cada step do trace. O data flow funciona como claimed?
- Pode construir o exact input (HTTP request, CLI invocation, API call, crafted file) que triggera isto?
- O input realmente alcança o sink sem ser blocked/transformed/validated no caminho?

### 3b. Impact Test
O que o atacante **realmente ganha**?
- Se a resposta é "aprende field names" ou "causa um error" → LOW máximo
- Se não pode descrever dano concreto em 2 frases → severity provavelmente está inflada

### 3c. Baseline Test
O comparável identificado em Phase 1 tem o mesmo pattern?
- Se sim e já foi explorado → finding MAIS FORTE, não mais fraco
- Se sim e nunca explorado em anos de produção → entenda por quê antes de reportar
- Se não tem comparável ou comparável não tem o pattern → proceda normalmente

### 3d. Mitigation Test
Existe outra layer que previne exploitation?
- WAF rules
- Middleware de input validation upstream
- Framework defaults (auto-escape, parameterized queries, CSRF tokens)
- Database constraints
- Network isolation
- Rate limiting

Mitigações não tornam false positive — reduzem severity. Note mas ainda confirme o flaw subjacente.

### 3e. Parser/Runtime Behavior Test
Se o exploit depende de como parser/runtime handles input específico:
- Verifique contra a spec ou implementação REAL
- NÃO assuma behavior de intuição
- Cite a spec ou teste dinamicamente
- Os false positives mais convincentes vêm de reasoning "o parser vai interpretar isso como..." sem verificar

## Step 4: Trace the Data Flow

### Identify the Source
- HTTP request parameters (query, body, headers, cookies)
- File uploads
- Database records (se populated por user input elsewhere)
- Message queues / event payloads

### Trace Through Transformations
- Validado? (type check, regex, allowlist)
- Sanitizado? (HTML encoding, SQL escaping, shell quoting)
- Transformado em safe type? (parsed as integer, resolved as enum)
- Passa por framework-level protection? (ORM parameterization, template auto-escape)

### Document the Chain
```
Source: req.query.search (user-controlled, string, sem length limit)
  → passed to: buildQuery(search) em db/queries.js:45
  → buildQuery concatena em SQL string (SEM parameterization)
  → executed via: db.raw(query) em db/queries.js:52
Sink: raw SQL execution
Mitigations: nenhuma encontrada
Verdict: CONFIRMED — SQL injection clássica
```

## Step 5: Attempt Proof-of-Concept

Se pode demonstrar exploitation safety sem causar dano:

**Para injection flaws:** Construa payload que produz observable side effect.
**Para auth bypasses:** Mostre o request que alcança protected resources sem credentials válidos.
**Para path traversal:** Mostre o path que resolve fora do diretório intended.

### Quando Dynamic Testing Não É Viável
- Rely em static trace: source → transforms → sink
- State: "Static analysis only — no dynamic confirmation"
- Note o que seria necessário para confirmar dinamicamente
- Ainda válido para `confirmed` se static trace é unambíguo

## Step 6: Render Verdict

| Verdict | Critérios |
|---------|----------|
| **confirmed** | Data attacker-controlled alcança dangerous sink com proteção insuficiente. Exploit path claro. Todos 5 gates passed. |
| **rejected** | Pattern não existe, código unreachable, ou mitigações previnem completamente exploitation. Evidência concreta de por quê. |
| **needs-more-info** | Não pode determinar. Especifique exatamente o que está faltando. |

## Step 7: Record

```bash
python3 scripts/scan_db.py validate \
  --finding-id <id> \
  --verdict <confirmed|rejected|needs-more-info> \
  --evidence "source: req.query.q → sink: db.raw() em queries.js:52, sem parameterization" \
  --poc "GET /api/search?q=' OR 1=1--" \
  --notes "Static trace only, no dynamic confirmation"
```

## Princípios

- Finding sem traceable data flow não é confirmed — é hipótese.
- Scanners reportam patterns, não exploits. Seu job é determinar se o pattern é explorável em contexto.
- "Rejected" é fine. Documente por quê e siga em frente.
- "Needs-more-info" é honesto. Melhor que adivinhar.
- Mitigações reduzem risco mas não eliminam findings. SQLi behind WAF ainda é SQLi.
- **Kill false positives agressivamente, mas não mate findings reais.** Report curto com 3 findings reais vale mais que report longo com 30 teóricos.

# Full Repository Security Scan

## Propósito

Auditoria de segurança estruturada de um repositório inteiro. Pipeline de 6 fases com agentes paralelos, validação adversarial, e verificação independente.

---

## Pipeline de 6 Fases

```
Phase 1: Recon     → architecture.md (agentes paralelos mapeiam o alvo)
Phase 2: Hunt      → findings brutos (agentes paralelos por attack class)
Phase 3: Validate  → findings confirmados (adversarial — tenta DISprovar)
Phase 4: Report    → security-report.html + report.json
Phase 5: Schema    → findings.json validado contra report-schema.json
Phase 6: Verify    → verificação independente de cada claim factual
```

---

## Phase 1: Reconnaissance

Lance **múltiplos agentes em paralelo** para mapear aspectos diferentes do codebase:

**Agent 1a: Overview, stack e baseline comparável**
- O que é esta aplicação? Que tipo de software?
- Quem usa e como? (end users, devs, operadores, outros services)
- Tech stack? (languages, frameworks, databases, runtime, deployment model)
- Qual software mainstream comparável existe? Que tradeoffs de security o comparável aceita?
- Estrutura de diretórios high-level com file paths para entry points chave

**Agent 1b: Trust boundaries e access control**
- Trust boundaries — onde input não-confiável entra? (HTTP, CLI, file reads, IPC, message queues, env vars, config)
- Authentication — como callers provam identidade?
- Authorization — como permissions são enforced?
- Privilege separation — roda como root? Drop privileges? Sandboxing?
- Bypass mechanisms (dev-only modes, test helpers, setup flows, debug flags)

**Agent 1c: Input surface inventory**
- Network-facing surfaces (HTTP endpoints, gRPC, WebSocket, TCP/UDP) com method/verb e propósito
- File-based input (uploads, config parsing, import/export)
- IPC e inter-service (message queues, shared memory, Unix sockets, env vars, CLI args)
- User-generated content surfaces
- External integrations (OAuth, webhooks, third-party APIs, plugin loading, dynamic code execution)
- Todos os lugares onde input alcança dangerous sinks

### Síntese

Colete outputs dos 3 agentes e sintetize em `architecture.md`:
- 1-2 páginas com application type, tech stack, trust model, input surfaces, baseline comparável
- Key file paths de todos agentes — starting points para Phase 2
- Se codebase é maior/mais complexo que esperado (plugin system, multi-tenant, complex auth chains), lance agentes adicionais antes de prosseguir

### Multi-Run Additive

Se runs anteriores existem (cheque `.security/scans/`):
1. **Skip known findings** — não re-descubra o mesmo bug. Mencione prior findings no report mas foque hunting em ground novo.
2. **Target gaps** — se runs anteriores focaram em injection e auth, pese este run para business logic, creative attacks, e wildcard.
3. **Resolve disagreements** — se runs anteriores deram verdicts conflitantes no mesmo finding, valide definitivamente.

Se nenhum run anterior existe, note no report que coverage melhora com runs adicionais.

---

## Phase 2: Hunt

Siga `steering/hunting.md` para:
- Selecionar attack classes relevantes ao application type
- Lançar agentes paralelos (um por classe × subsistema)
- Cada agente recebe architecture.md + hunting methodology + validation rules
- Agentes podem spawnar sub-agents para deep dives

---

## Phase 3: Validate (Adversarial)

**Consolidar duplicatas primeiro** — Phase 2 deliberadamente overlapa scopes.

Para cada finding restante, lance um **agente de validação separado** que tenta **DISprovar** o finding:

```
Seu trabalho é DISPROVAR este finding. Leia o source code real em cada step.
Se não conseguir disprovar, confirme com o código exato que o torna explorável.

Retorne um de:
- "CONFIRMED: [explicação com code evidence]"
- "REJECTED: [o que o finding errou, com code evidence]"
```

**Testes de validação:**
1. **Exploitation test**: Leia o código real em cada step do trace. O data flow funciona como claimed? Pode construir o exact input que triggera?
2. **Impact test**: O que o atacante realmente ganha? Se "aprende field names" ou "causa error" = LOW máximo.
3. **Baseline test**: O comparável tem o mesmo pattern? Se sim, foi explorado? Se nunca explorado em anos de produção, entenda por quê antes de reportar.
4. **Mitigation test**: Existe outra layer que previne exploitation? Cheque middleware, DB constraints, framework defaults.
5. **Parser/runtime behavior test**: Se o exploit depende de como parser/runtime handles input específico, verifique contra spec ou implementação — não reasoning from intuition.

**Kill false positives agressivamente, mas não mate findings reais.** Report curto com 3 findings reais vale mais que report longo com 30 teóricos.

---

## Phase 4: Report

Gere o report usando `steering/reporting.md`. Siga `references/report-format.md` para o HTML.

Adições ao report padrão para full-scan com pipeline:
- Seção de coverage: quais attack classes foram exercitadas, quais subsistemas
- Seção de findings rejeitados (colapsável): mostra rigor sem cluttering findings reais
- Positive patterns: o que o codebase faz bem (calibra confiança na auditoria)

---

## Phase 5: Structured Output e Schema Check

Para cada finding que sobreviveu Phase 3, produza JSON conformando ao schema em `references/report-schema.json`.

1. Leia `references/report-schema.json` antes de escrever output. Siga exatamente — `additionalProperties: false` enforced.
2. Para cada finding, popule todo required field. Se não pode preencher `trace` com real file paths e line numbers verificados, o finding não está suficientemente verificado — volte e verifique ou rejeite.
3. Valide com: `node scripts/validate-findings.cjs <output>/findings.json`
4. Fix qualquer falha antes de prosseguir.

Escreva em: `.security/scans/<timestamp>/findings.json`

---

## Phase 6: Independent Verification

O structured output de Phase 5 força self-validation, mas o mesmo agente que escreveu o finding também escreveu o JSON. Esta phase usa agentes frescos para verificar independentemente.

Lance **um agente por finding confirmado**, todos em paralelo:

```
Você é um verificador independente. Você NÃO escreveu este finding.
Seu trabalho é ler o source code real e verificar que todo claim factual está correto.

1. Leia file e line number citados em CADA trace step. Verifique:
   - File existe no path citado
   - Line number corresponde ao código descrito
   - Scope (function name) está correto
   - Description reflete acuradamente o que o código faz

2. Verifique root_cause lendo o file citado e confirmando que o defeito descrito existe.

3. Verifique execution payloads:
   - Endpoint existe na URL claimed?
   - HTTP method corresponde?
   - Input passaria validation como descrito?
   - Auth/access checks passariam como descrito?

4. Verifique conditions — há pré-requisitos que o finding não mencionou?

5. Cheque remediation code_changes — o fix preveniria o ataque sem quebrar funcionalidade normal?

Retorne um de:
- "VERIFIED" — todos claims checked contra source
- "CORRECTED: [field]: [errado] → [correto]"
- "REJECTED: [razão]"
```

Aplique correções:
- **VERIFIED**: nenhuma mudança
- **CORRECTED**: atualize campos específicos, re-run schema validation
- **REJECTED**: mude verdict para `"rejected"` ou remova

Após correções, reconcilie deliverables: atualize HTML report e findings.json para que não discordem.

---

## Inicialização e Persistência

```bash
python3 scripts/scan_db.py init --repo <path>
```

Findings são persistidos no SQLite durante todo o processo. O `finalize.py` sela ambos os formatos (JSON + HTML) no final.

---

## Completion Criteria

O scan está completo quando:
- [ ] Phase 1 produziu architecture.md com trust model e input surfaces
- [ ] Phase 2 exercitou attack classes relevantes com agentes paralelos
- [ ] Phase 3 validou adversarially cada finding (confirmado ou rejeitado)
- [ ] Phase 4 produziu HTML report conforme template
- [ ] Phase 5 produziu findings.json válido contra schema
- [ ] Phase 6 verificou independentemente cada claim factual
- [ ] Report e findings.json concordam (sem discrepâncias)

# Vulnerability Hunting

## Propósito

Caça ativa de vulnerabilidades usando agentes paralelos especializados por classe de ataque. Este é o motor principal do `full-scan` — Phase 2 na pipeline de 6 fases.

## Orquestração

Lance **múltiplos agentes em paralelo** via Task tool. Cada agente recebe:

1. O resumo de arquitetura da Phase 1 (verbatim)
2. A classe de ataque específica e escopo
3. File paths relevantes como ponto de partida
4. A hunting methodology (abaixo)
5. As validation rules (abaixo)

**Quantos agentes?** Use Phase 1 para decidir. Agentes focados produzem melhores resultados que agentes amplos. Para uma biblioteca pequena, 3-4 agentes. Para uma aplicação grande com subsistemas distintos, lance 8-12+ — divididos por classe de ataque E por subsistema.

---

## Attack Classes

Selecione classes relevantes ao tipo de aplicação. Nem toda classe se aplica a todo codebase.

### Injection

Trace input não-confiável do entry point ao dangerous sink:

- **Web apps**: SQL queries, HTML output, shell commands, template engines, file paths, HTTP redirects, deserialization
- **Libraries**: funções que processam dados do caller sem validação — buffer operations, parsers, format strings
- **CLI tools**: construção de shell commands, file path handling, interpolação de environment variables
- **Services**: query construction, message serialization, log injection, LDAP/XPATH queries

Não cheque apenas paths diretos. Procure:
- Injection indireta: dado armazenado safe, depois retrieved e usado em contexto perigoso por código diferente
- Injection via field names, keys, headers e metadata — não só values
- Injection em sistemas secundários (logs, caches, search indexes, analytics)

### Access Control

Pode um caller fazer algo que não deveria? Vá além de verificar se permission checks existem — verifique se checam a *permissão correta* para o *recurso correto* via o *mecanismo correto*:

- Existe path para o mesmo state change que checa uma permissão diferente (mais fraca)?
- Um field no request body pode override o que o permission system pretendia restringir?
- Existem endpoints que gate em authentication mas esquecem authorization?
- O mesmo recurso tem múltiplos access paths com checks inconsistentes?
- Operações bulk/batch/export/import enforcam per-item permissions?

### Resource and File Handling

- Path traversal (read/write fora do diretório pretendido) — incluindo via symlinks, encoded sequences, null bytes
- SSRF (fazer a aplicação fetch URLs controladas pelo atacante) — incluindo via redirects, DNS rebinding, URL parser differentials
- Unsafe deserialization, archive extraction (zip slip), temp file handling
- Memory safety (se aplicável): buffer overflows, use-after-free, integer overflow
- Race conditions em file operations (TOCTOU entre check e use)

### Cryptography and Secrets

- Weak randomness para valores security-critical (tokens, keys, nonces)
- Hardcoded secrets, secrets em logs, error messages, URLs, ou client-visible responses
- Broken key derivation, missing HMAC verification, nonce reuse
- Timing side-channels em secret comparison
- Misuse de crypto primitives (ECB mode, unauthenticated encryption, static IVs)
- O que acontece quando crypto operations falham? O error path faz fallback para no-crypto?

### Business Logic

Onde os bugs reais se escondem. Scanners não encontram logic errors.

Para cada major workflow:
- **State machine violations**: Pode pular steps? Ir backwards? Alcançar estado inválido? Replay de um flow completed? Partial failure — se step 2 de 3 falha, step 1 é rolled back?
- **Race conditions com business impact**: Operações concorrentes que produzem estados inválidos (double-spend, double-approve, lost updates). Foque em operações check-then-act não-atômicas.
- **Numeric/quantity manipulation**: Negative values, zero, overflow, precision loss, type coercion string↔number.
- **Access boundary violations**: Não "o permission check existe" mas "é o check certo para a business rule?" Input em uma operação bypass restrição enforced em operação diferente para mesmo efeito?
- **Implicit trust assumptions**: Data de storage, config, outros componentes assumida safe porque "validamos na entrada." E se um code path diferente escreveu?
- **Time-based logic**: Expiry checks, scheduling, rate windows, clock skew. O que acontece em boundary moments exatos? Timezone differences entre componentes?
- **Default and fallback behavior**: Qual a security posture quando config está missing? Feature flag off? Dependência unavailable? Sistema mid-migration?

### Feature Abuse and Data Leakage

Features legítimas usadas para propósitos não-pretendidos. Não procure bugs no código — procure bugs no design:

- **Export/backup como exfiltration**: Low-privilege user pode trigger export que inclui dados above their access? Export de outros users? Dados deleted/draft/private?
- **Import/restore como injection**: Import pode overwrite dados existentes? Criar records que bypass validação normal? Inject em collections sem write access?
- **Search/filter/sort como oracle**: Search queries revelam se content existe que o user não pode acessar diretamente? Filter params permitem probe de statuses/roles/fields que não deveriam ser visíveis?
- **Enumeration via side effects**: Error messages diferem entre "não existe" e "sem acesso"? Response times diferem? Sizes? Status codes?
- **Preview/draft/staging leakage**: Preview tokens scoped a um item ou unlock acesso mais amplo? Draft discoverable via search, RSS, sitemaps, API listing?
- **Notification/webhook como SSRF**: User pode set notification/webhook/callback URL que o server fetches? Validado contra internal networks?

### Chained Attacks and Trust Boundaries

Comportamentos individualmente safe que se tornam perigosos em combinação:

- **Multi-step chains**: Mapeie o que um low-privilege user CAN do, depois procure combinações. Info disclosure + IDOR + missing rate limit. Open redirect + OAuth callback = token theft.
- **Cross-component trust gaps**: Component A valida input e passa para B. B re-valida ou confia em A? E se validação de A é sutilmente diferente do que B precisa?
- **Second-order attacks**: Dados safe quando stored mas perigosos quando usados em contexto diferente. Field name safe em SQL vira key em JSON path expression. Slug safe em URL vira parte de file path.
- **Scope and capability escalation**: Tokens/API keys/OAuth scopes que grant acesso mais amplo que o nome implica. Session cookies que sobrevivem role downgrade.
- **Timing and ordering**: Usar feature antes de setup complete? Agir em resource entre soft-delete e hard-delete? Usar token entre revocation e cache expiry?

### Wildcard

Não recebe categoria. Recebe o codebase e a instrução de quebrá-lo. Ignore vulnerability classes padrão — outros agentes cobrem isso. Encontre o que ninguém pensou em procurar:

- Código mais estranho do codebase? Por que existe? O que acontece se abusado?
- Features half-finished/experimentais/bolted-on? Segurança mais fraca, menos review.
- API usada de forma que o frontend nunca faria? UI constrains users, API não.
- Endpoints/parâmetros/headers hidden ou undocumented?
- Mix de features não desenhadas para funcionar juntas?
- Git history: reverted security fixes, commented-out auth checks, secrets committed then removed?
- Com valid account: máximo dano sem detecção? Corrupting data, poisoning caches, exhausting resources.

### Obvious Things

Outros agentes caçam bugs sutis. Este checa o "óbvio" que é fácil ignorar:

- Hardcoded passwords, API keys, tokens, secrets no source?
- TODO/FIXME/HACK/XXX comments referenciando security?
- Debug mode/dev mode proper gated? Habilitável em prod via env var, query param, header?
- Test/example/seed credentials que funcionam em prod?
- Endpoints `/debug`, `/admin`, `/test`, `/status`, `/health`, `/metrics`, `/env`, `/.env`, `/config` unprotected?
- Arquivos `.env`, `credentials.json`, `*.pem`, `*.key` checked into repo?
- `.gitignore` cobre secrets, uploads, e local config?
- Dependencies pinned? CVEs conhecidos no dependency tree?
- `eval()`, `exec()`, `child_process`, `Function()`, `vm.runInContext`, `import()` com dynamic input?
- CORS headers `*` ou overly permissive com `Access-Control-Allow-Credentials`?
- Cookies missing `HttpOnly`, `Secure`, ou `SameSite`?
- Open redirects? (params named `redirect`, `return`, `next`, `url`, `goto`, `continue`)
- TLS enforced? HTTP-only endpoints?
- Error responses em prod retornando stack traces, internal paths, SQL errors?

**IMPORTANTE**: Para qualquer finding deste agente, verificar o full code path, não só surface appearance. Um flag não é um finding — trace o impacto antes de reportar.

---

## Hunting Methodology — 12 Ângulos

Inclua em todo prompt de agente Phase 2:

### Como caçar

Não apenas cheque se defesas existem. Tente quebrá-las. LEIA O CÓDIGO EM PROFUNDIDADE. Não pare na primeira função. Siga os dados por cada layer — de entry point até validation, transformation, storage, retrieval, e output. Bugs vivem nos gaps entre layers.

1. **O HAPPY PATH ESTÁ DEFENDIDO. ATAQUE O SAD PATH.** Error handlers, fallback branches, catch blocks, default cases, timeout paths, retry logic, cleanup routines. Erros são handled com o mesmo rigor que success? Failed validation deixa state half-modified?

2. **O QUE ACONTECE NAS BOUNDARIES?** Empty input. Maximum-length. Null vs undefined vs missing. Zero. Negativo. Unicode edge cases. Primeiro e último item. Um mais que o máximo. Exatamente no rate limit. Momento de token expiry.

3. **O QUE COMPONENTES ASSUMEM SOBRE OUTROS?** DB layer assume que API layer validou? Renderer assume content sanitized no write? Auth middleware assume que routes se registram corretamente? Encontre onde trust é implícito e teste se é justificado.

4. **E SE OPERAÇÕES ACONTECEM NA ORDEM ERRADA?** Call step 3 antes de step 1. Delete durante create. Callback antes do request. Confirmation endpoint sem iniciar o flow. Replay de flow completed.

5. **E SE DUAS COISAS ACONTECEM SIMULTANEAMENTE?** Dois requests ao mesmo resource. Modify durante read. Delete durante iterate. Publish enquanto outro edita. Dois users claiming mesmo unique resource.

6. **ONDE DOIS PARSERS OU VALIDATORS DISCORDAM?** Input aceito pelo schema mas rejeitado pelo DB. URL parsed diferente pelo router vs app code. Content-type diz uma coisa, body é outra. Filename extension vs MIME type vs magic bytes.

7. **O QUE SOBREVIVE UM ROUND TRIP?** Data stored e retrieved — é o mesmo? Encoding muda? Escaping double-up? Relative path resolved diferente em read vs write? Serialization perde type info?

8. **O QUE A CONFIGURAÇÃO CONTROLA?** Config missing ou default — o que acontece? Environment variable pode override security control? Feature flag desabilita validation? Security posture durante setup/first-run antes de config completo?

9. **SIGA O DINHEIRO (OU O PRIVILÉGIO).** Para toda operação que muda state: quem autorizou? Trace back ao permission check. Checa a permissão certa? Contra o recurso certo? Existe path paralelo para o mesmo state change que checa diferente ou não checa?

10. **PROCURE CONTEXTO VAZADO.** Error messages que revelam internal paths. Stack traces em prod. Timing differences que revelam se record existe. Response size differences. HTTP headers com versões. Debug endpoints que sobreviveram para prod.

11. **QUE PARÂMETROS OVERRIDAM DEFAULTS SECURITY-RELEVANT?** Onde default é safe mas user-supplied parameter pode mudar. Procure todo input que override security-relevant default e cheque se o override é gated por permissions apropriados.

12. **ONDE CLAIMS NÃO-VERIFICADOS DIRIGEM DECISÕES DE TRUST?** Self-declared identity, capability, ou metadata influenciando access/trust decision sem verificação independente.

---

## Validation Rules — Aplicar antes de reportar QUALQUER finding

1. Você DEVE construir um ataque concreto (exact inputs, requests, ou action sequence)
2. O ataque DEVE alcançar impacto meaningful (não apenas "aprender field names" ou "causar um error")
3. Cheque se outra layer já previne exploitation — se sim, é hardening note, não finding
4. Se o baseline comparável tem o mesmo pattern, note se foi explorado lá
5. Se seu exploit depende de parser/runtime behavior, verifique contra a spec ou implementação — não assuma
6. Retorne APENAS findings confirmados com ataques concretos, ou "Nenhuma vulnerabilidade explorável encontrada" se isso é honesto

---

## Spawn Sub-Agents

Se precisar entender um subsistema em profundidade para avaliar um potential finding — use o Task tool para lançar um research agent. Não tente segurar tudo no seu próprio contexto. Vá fundo onde importa.

**SEU ESCOPO É SEU FOCO PRIMÁRIO, NÃO UMA FRONTEIRA.** Se ao investigar sua área atribuída notar algo errado em categoria diferente — um permission issue ao tracing injection, uma race condition ao reviewing auth — reporte. Não ignore um bug porque "não é sua área." Atacantes não respeitam fronteiras de categoria.

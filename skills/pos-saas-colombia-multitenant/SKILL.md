---
name: pos-saas-colombia-multitenant
description: Arquitecto de referencia para diseñar y mantener el backend de un POS (Punto de Venta) SaaS B2B multitenant con facturación recurrente mensual/anual, usando pasarelas de pago colombianas (Wompi, ePayco, PSE, Nequi, Daviplata, Efecty) — no Stripe. Usar siempre que el trabajo incluya: modelado de datos multitenant, aislamiento de datos (tenant_id, PostgreSQL Row Level Security), middleware de contexto de tenant, integración de webhooks de pasarelas colombianas, lógica de suscripciones/dunning/suspensión automática, o estructura de carpetas Clean Architecture para este tipo de sistema. Invocar también ante menciones de "aislamiento de tenant", "RLS", "Wompi", "ePayco", "PSE", "Nequi", "activación automática de pago", "cobro recurrente COP" o "POS multitenant".
---

# POS SaaS Multitenant — Colombia Edition

Skill de arquitectura de referencia para un backend de Punto de Venta como SaaS, con dos planos desacoplados (Control Plane / Application Plane), aislamiento de datos por `tenant_id` reforzado con PostgreSQL RLS, y facturación recurrente mediante pasarelas de pago locales colombianas.

## Precondición de este vault

Antes de aplicar esta skill, el agente debe haber cargado la **Core Always-First Suite** definida en `AGENTS.md` del vault (compresión de tokens, YAGNI, spec-first, memoria persistente, `archify` cada 3 commits). Esta skill no reemplaza esas reglas base, las complementa.

## Decisiones abiertas — NO asumir, preguntar antes de generar código

Esta skill describe un patrón de referencia, no una decisión ya tomada. Antes de escribir código, el agente debe confirmar con el usuario (una sola vez por proyecto, no en cada invocación):

1. **Stack de lenguaje/framework**: el código de ejemplo en `references/` está en TypeScript/NestJS + `pg`. Si el proyecto real usa otro stack (Python/FastAPI, Go, Laravel), traducir los *patrones*, no copiar literal el código.
2. **ORM vs. SQL crudo**: si se usa Prisma/Drizzle/TypeORM, verificar cómo cada uno maneja `SET LOCAL` / `set_config` dentro de una transacción — el comportamiento con pools en modo *transaction* varía y puede romper el aislamiento si se asume incorrectamente.
3. **Pasarela(s) de pago definitiva(s)**: el patrón soporta múltiples pasarelas vía abstracción (`gateway_name`), pero implementar las cuatro (Wompi, ePayco, PSE directo, Nequi) desde el día uno multiplica el costo de testing. Confirmar si se arranca con una sola.
4. **Estado del proyecto**: si ya existe una base de datos en producción con otro esquema, esto es una migración (requiere plan de migración y ventana de mantenimiento), no un boilerplate desde cero.
5. **Modo de PgBouncer** (si aplica): el patrón de RLS asume modo *transaction*. Si el proveedor de hosting usa modo *session* o no usa pooler, la inyección de contexto puede simplificarse (o requerir ajuste).

Si el agente no tiene esta información en el contexto de la conversación actual, debe preguntarla antes de generar DDL o código — no asumir por defecto.

## Mapa de las 7 capas

```
CAPA 1  Edge/Gateway      → Subdomain router + rate limiter por plan (Redis)
CAPA 2  Auth/IAM          → JWT con claims inmutables (tenant_id, role, store_id)
CAPA 3  Middleware        → AsyncLocalStorage + wrapping transaccional
CAPA 4  Dominio           → Control Plane (global) vs Application Plane (POS)
CAPA 5  Persistencia      → PostgreSQL + Row Level Security + PgBouncer-safe context
CAPA 6  Cache/Async       → Redis namespacing + workers con tenant_id en payload
CAPA 7  Observabilidad    → Logs estructurados + tests de aislamiento cruzado en CI/CD
```

## Reglas de oro (no negociables)

- El `tenant_id` **nunca** se lee del body JSON ni de parámetros de URL. Se extrae exclusivamente del JWT verificado en el borde (Capa 2).
- Toda tabla del Application Plane usa `tenant_id` como primer componente de su clave primaria compuesta y de todos sus índices.
- `ALTER TABLE ... FORCE ROW LEVEL SECURITY` es obligatorio, no opcional — sin esto, el rol propietario de las tablas bypasea las políticas.
- La inyección de contexto en PostgreSQL usa `set_config(..., true)` (alcance de transacción), nunca `SET SESSION`, para no filtrar contexto entre requests cuando hay pooling.
- RLS es la **segunda línea de defensa**, no la única: el filtro explícito por `tenant_id` en el código de la aplicación sigue siendo obligatorio.
- Ningún webhook de pasarela de pago se procesa sin: (a) validar firma/checksum, (b) verificar idempotencia contra una tabla de gateway_events, (c) reconsultar el estado canónico en la API de la pasarela antes de confiar en el payload recibido.

## Archivos de referencia

Leer solo el archivo relevante a la tarea puntual — no cargar los cuatro si solo se necesita uno:

| Archivo | Cuándo leerlo |
|---|---|
| `references/01-database-schema-rls.md` | Al diseñar/modificar tablas, políticas RLS, índices, o el wrapper de contexto de PostgreSQL |
| `references/02-middleware-context.md` | Al implementar el middleware de extracción de JWT, `AsyncLocalStorage`, o el repositorio tenant-aware |
| `references/03-payment-gateways-colombia.md` | Al integrar Wompi/ePayco/PSE/Nequi, diseñar el flujo de suscripciones, o el handler de webhooks |
| `references/04-folder-structure.md` | Al iniciar un proyecto nuevo o revisar la organización de carpetas |

## Checklist de entregables al invocar esta skill

Al completar una tarea con esta skill, verificar que el resultado incluya (según aplique):

- [ ] Tablas con `tenant_id` liderando PK e índices compuestos
- [ ] Políticas RLS con `ENABLE` + `FORCE`
- [ ] Función/wrapper de `set_config` con alcance transaccional
- [ ] Middleware que rechaza requests sin `tenant_id` resuelto desde JWT
- [ ] Si hay webhooks: tabla de idempotencia + verificación de firma + refetch a la API de la pasarela
- [ ] Si hay suscripciones: manejo explícito de `past_due` → `suspended` con bloqueo `HTTP 402`
- [ ] Nota explícita de qué decisiones abiertas (sección anterior) siguen sin confirmar

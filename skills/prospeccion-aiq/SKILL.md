---
name: prospeccion-aiq
description: Construye y ejecuta una lista de prospectos calificados en Instagram para vender servicios de IA — descubre cuentas por bola de nieve, las enriquece con email y señal de monetización, las puntúa y decide a quién contactar y por qué canal. Usala siempre que alguien hable de conseguir clientes, prospectar, armar una lista de leads, "no sé a quién venderle", cuentas de Instagram para contactar, scraping de perfiles, o cuando pregunte cómo llenar el embudo sin pagar anuncios. También cuando tenga una lista y no sepa a quién priorizar.
---

# Prospección AIQ — de cero a lista calificada

El problema de la prospección casi nunca es el mensaje. Es **a quién se lo mandás**. Una lista de 3.000 cuentas sin filtrar produce menos que 100 bien elegidas, porque el tiempo se va contestando a gente que nunca iba a pagar.

Esta skill produce una cosa concreta: **una lista de handles con email de contacto, señal de que monetizan y un puntaje**, lista para trabajar de mayor a menor.

## Antes de arrancar, definí a quién buscás

No sirve "dueños de negocio". Necesitás una frase que se pueda verificar mirando un perfil:

> *"Creadores de habla hispana que venden una mentoría o un curso propio, con link de pago en la bio y publicación en los últimos 15 días."*

Si no podés decidir en 5 segundos mirando un perfil si entra o no entra, la definición todavía es mala. Preguntale al usuario y afinala antes de descubrir nada — descubrir con una definición floja multiplica el trabajo de descarte después.

## Las cuatro fuentes, en orden de conveniencia

### 1. Cuentas relacionadas — la bola de nieve

El endpoint `web_profile_info` de Instagram devuelve `edge_related_profiles`: las cuentas que el propio Instagram considera parecidas. Es su grafo de similitud, gratis, en una llamada que ya hacés.

**Cómo se usa:** cargás 20 semillas del perfil que buscás → cada una devuelve ~20 relacionadas → las nuevas se vuelven semilla. En 3 saltos tenés miles de handles del nicho exacto, con costo extra cero.

Empezá siempre por acá. Es la fuente con mejor relación esfuerzo/calidad.

### 2. Biblioteca de Anuncios de Meta — la mejor señal

Es pública, gratis y filtrable por país. **El que paga anuncios ya demostró que gasta plata para conseguir clientes**, que es el calificador más fuerte que existe.

Se busca por palabras del nicho (*mentoría, curso, asesoría, plantillas, formación, agencia*), se saca la página de Facebook de cada anuncio y de ahí la cuenta de Instagram vinculada.

⚠️ La API `ads_archive` está restringida a anuncios políticos en la mayoría de países. Esto sale de la interfaz web pública, no de la API.

### 3. Comentaristas de cuentas grandes

Tomás las cuentas grandes del nicho y cosechás quién comenta seguido. Volumen alto, calidad media. Sirve cuando la bola de nieve se agotó.

### 4. Hashtags y ubicaciones

Máximo volumen, mínima calidad. Sirve para llenar el embudo, no para priorizar.

## El campo que casi nadie mira

La misma llamada a `web_profile_info` que trae seguidores y bio **también devuelve el email**:

| Campo | Por qué importa |
|---|---|
| `business_email` | El canal de contacto en frío sin quemar tu cuenta de Instagram |
| `business_phone_number` | WhatsApp directo |
| `external_url` | El link en bio: dice si monetiza y con qué plataforma |
| `category_name` | "Entrenador personal", "Consultor de negocios" |
| `is_business_account` | Filtro de calidad |
| `edge_follow.count` | Seguidos, para detectar cuentas infladas |
| `edge_related_profiles` | El motor del descubrimiento |

Si el extractor que estás usando solo guarda nombre, seguidores y bio, **está tirando el dato más valioso de la respuesta**. Ampliarlo es cambiar cuatro líneas.

## El scoring: no filtres por seguidores

Un creador con 80.000 seguidores que no vende nada no te paga nada. Uno con 6.000 que vende una mentoría de US$800, sí. Lo que se puntúa es **evidencia de que ya mueve dinero**.

| Señal | De dónde sale | Puntos |
|---|---|---|
| Corre anuncios en Meta | Biblioteca de Anuncios | **+40** |
| Link a Hotmart / Kajabi / Systeme / Stan / Calendly / `wa.me` | `external_url` | **+25** |
| Bio dice mentoría, curso, asesoría, agencia, consultoría | `biography` | +15 |
| Cuenta profesional con email público | `business_email` | +10 |
| Publica 3+ veces por semana | `media_count` vs antigüedad | +10 |
| Engagement > 2 % | (likes + comentarios) / seguidores | +10 |

**Descarte automático:**
- Menos de 3.000 seguidores **y** sin producto en el link
- Sin link en bio
- Última publicación hace más de 30 días → cuenta abandonada
- Seguidos/seguidores > 0,8 → cuenta inflada o engagement recíproco

**Contactá de 60 puntos para arriba.** Mandar 100 mensajes buenos rinde más que 1.000 al vacío, y además no te quema la cuenta.

## El canal: email antes que DM

Instagram limita los mensajes directos con dureza. Una cuenta nueva se restringe a los 10-20 diarios. Si quemás tu cuenta principal perdés tu activo más caro, y no hay forma rápida de recuperarlo.

Por eso el `business_email` vale tanto: **es el canal que ellos mismos publicaron** para que los contacten, y no depende de la salud de tu cuenta.

**Orden:**
1. **Email** al `business_email` → el volumen principal
2. **WhatsApp** si hay `business_phone_number` → mejor tasa de respuesta
3. **DM** solo a los de score más alto, desde una cuenta secundaria, con ritmo bajo

### Sobre el scraping, sin vueltas

Traer datos de Instagram fuera de la API oficial va contra sus términos. El riesgo real es bloqueo de IP y de cuenta. Hacelo con un servicio que maneje proxies o desde una cuenta dedicada que no sea la tuya, con ritmo bajo y pausas. **Nunca desde la cuenta principal ni desde tu IP de casa sin límite.** Decilo cuando alguien pregunte, no lo escondas.

## La matemática, para saber cuánto hace falta

Objetivo de ejemplo: 10 ventas de US$500 = US$5.000/mes.

| Etapa | Tasa | Cantidad |
|---|---|---|
| Descubiertos | — | 3.000/mes |
| Pasan score 60 | 15 % | 450 |
| Contactados por email | — | 450 |
| Responden | 8-12 % | ~45 |
| Agendan demo | 40 % | ~18 |
| **Cierran** | **50 %** | **9** |

Estos números dependen de dos cosas: que el score filtre de verdad (por eso pesa tanto la señal de anuncios) y que la demo sea **en vivo con el producto corriendo**, no un video grabado.

Cuando alguien te diga que "prospectar no funciona", pedile los números de su embudo. Casi siempre falla en la primera fila: descubrió 200 cuentas, no 3.000.

## Qué entregar

Cerrá siempre con una tabla que se pueda trabajar, ordenada por score descendente:

```
handle · nombre · seguidores · categoría · email · link en bio · plataforma detectada · corre ads · engagement · score · canal sugerido
```

Y arriba, tres líneas: cuántos se descubrieron, cuántos pasaron el filtro, y **por qué canal conviene empezar**. Si el usuario no puede empezar a trabajar con lo que le diste sin hacerte otra pregunta, la entrega está incompleta.

## Errores que se repiten

- **Filtrar por seguidores.** Es la métrica más fácil de mirar y la que menos correlaciona con que te paguen.
- **Empezar por hashtags.** Da volumen inmediato y basura. Dejalo para el final.
- **Mandar DMs desde la cuenta principal.** Un bloqueo cuesta más que todos los leads que ibas a sacar.
- **Contactar a todos.** El score existe para no hacerlo. Si vas a contactar a los 450 igual, no hacía falta puntuar nada.

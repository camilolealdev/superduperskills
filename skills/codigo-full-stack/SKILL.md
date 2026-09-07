---
name: codigo-full-stack
description: Construye aplicaciones completas de punta a punta — interfaz, API, base de datos, autenticación y despliegue — con criterio de producción y sin sobredimensionar. Cubre elección de stack, modelo de datos, endpoints, manejo de errores, secretos y puesta en línea. Usala siempre que haya que armar una app, un panel, un formulario que guarde datos, un CRUD, una landing con backend, una integración con una API, un webhook, o cuando alguien diga "necesito una web que haga X", "quiero un dashboard", "hay que conectar esto con aquello", o pida agregarle backend a algo que ya existe. También cuando haya que decidir entre stacks o cuando algo funcione en local y falle en producción.
---

# Código full-stack

El objetivo no es escribir el código más elegante: es que **algo funcione en producción, se pueda entender dentro de tres meses y no se caiga por una razón boba**. Casi todos los proyectos que mueren lo hacen por sobredimensionar al principio o por descubrir en el despliegue algo que se podía haber decidido el primer día.

## Antes de escribir una línea

Cuatro preguntas. Sin estas, cualquier decisión de stack es una apuesta:

1. **¿Quién lo usa y cuántos son?** Tres personas de un equipo y diez mil usuarios anónimos no se construyen igual.
2. **¿Qué datos guarda y quién puede verlos?** Si hay datos de terceros, la autorización deja de ser opcional.
3. **¿Con qué se tiene que integrar?** Las integraciones definen el stack más que las preferencias.
4. **¿Quién lo va a mantener?** Si es alguien que no programa, elegí lo aburrido y lo alojado.

Si el usuario no sabe responder la 2, ayudalo a responderla antes de seguir. Es la que más caro sale corregir después.

## Elegir stack: por defecto lo aburrido

Elegí tecnología nueva solo cuando resuelva un problema que el default no resuelve. La novedad se paga en documentación que no existe y en errores que nadie tuvo antes.

| Situación | Por defecto | Por qué |
|---|---|---|
| App con usuarios, datos y panel | **Next.js + Postgres (Supabase o Neon)** | Un solo repo, auth resuelta, despliegue en minutos |
| Solo un panel interno | **HTML + JS plano + Supabase** | Sin build, sin framework, se edita y se sube |
| API que consumen otros | **FastAPI** o **Express** | Rápidas de escribir, documentación automática |
| Procesos pesados o programados | **Cola + worker** (no un endpoint HTTP) | Un request que tarda 3 minutos se va a cortar |
| Sitio de contenido | **Astro** o estático | Si no hay estado de usuario, no hace falta servidor |

**Cuándo NO usar Next.js:** si es un panel interno para tres personas, un `index.html` con `fetch` te ahorra el build, el deploy y las actualizaciones de dependencias. Se subestima mucho lo lejos que llega.

## El modelo de datos primero

El esquema es lo más caro de cambiar. Antes de la primera pantalla, escribí las tablas con sus relaciones y mostráselas al usuario en palabras que entienda.

Cuatro reglas que evitan la mayoría de los dolores:

- **Claves foráneas de verdad**, con `on delete` explícito. Decidir si borrar un cliente borra sus pedidos es una decisión de negocio, no técnica: preguntala.
- **Timestamps en todo** (`created_at`, `updated_at`). Nunca te vas a arrepentir de tenerlos y siempre de no tenerlos.
- **Enums como `check` o tabla**, no strings libres. Un `estado` con typos es un bug silencioso.
- **Nada de borrado físico donde importe el historial.** Un `archivado boolean` te salva de la llamada de "borré sin querer".

## La interfaz

Lo que separa una app que se ve profesional de una que se ve armada en una tarde no es el framework de CSS: son **los estados**.

Toda vista que trae datos tiene cuatro, y hay que dibujar los cuatro:

1. **Cargando** — un esqueleto, no un spinner centrado en blanco
2. **Vacío** — con qué hacer para dejar de estar vacío, no solo "sin resultados"
3. **Error** — qué pasó y qué puede hacer, no "algo salió mal"
4. **Con datos** — el único que todos dibujan

Y tres detalles que se notan mucho:

- **Deshabilitá el botón mientras se envía.** El doble submit crea registros duplicados y es el bug más común de los formularios.
- **Confirmá lo destructivo** nombrando lo que se borra: "Borrar el cliente Pérez y sus 12 pedidos", no "¿Estás seguro?".
- **Que funcione con el teclado.** Enter envía, Escape cierra.

## El backend

**Validá la entrada en el servidor, siempre.** La validación del formulario es comodidad para el usuario; la del servidor es la que evita que te rompan la base. Cualquiera puede llamar a tu API sin pasar por tu HTML.

**Los errores tienen que decir qué hacer.** Un `500 Internal Server Error` no ayuda a nadie. Devolvé qué falló y, si es del usuario, qué corregir. Y logueá lo que no se puede mostrar.

**Cuidá el N+1.** Traer una lista y después pedir un dato por cada fila es la causa número uno de "funcionaba con 10 registros y con 5.000 se murió". Traelo con un join o con una sola consulta.

**Lo que tarda, va a una cola.** Si un endpoint hace algo de más de unos segundos —generar un PDF, llamar a tres APIs, procesar un video— devolvé un id y procesá aparte. Los timeouts de los proveedores no se negocian.

## Secretos y accesos

- **Ninguna clave en el código, nunca.** Variables de entorno, y el `.env` en `.gitignore` desde el primer commit.
- **Las claves de servicio no llegan al navegador.** Si el frontend la puede leer, es pública.
- **Autenticación no es autorización.** Saber quién es no es lo mismo que decidir qué puede ver. Si hay datos por usuario, se chequea en cada consulta — en Postgres, con RLS.
- **Si una clave se filtró, se rota.** No se borra el commit y se sigue: se rota.

## Antes de decir que está listo

Una lista corta que atrapa casi todo:

- [ ] Corre desde cero en otra máquina siguiendo el README
- [ ] Las variables de entorno están documentadas (con un `.env.example`)
- [ ] Los cuatro estados de la interfaz están dibujados
- [ ] La validación está también en el servidor
- [ ] Nada destructivo pasa sin confirmación
- [ ] Los errores dicen qué hacer
- [ ] Probado en un teléfono de verdad, no solo achicando la ventana
- [ ] Las claves no están en el repo

## Cuando algo anda en local y falla en producción

Casi siempre es una de cinco, en este orden:

1. **Variable de entorno que no está** en el entorno de producción
2. **CORS** — el dominio real no está en la lista permitida
3. **Migración de base** que corrió en local y no allá
4. **Rutas o mayúsculas** — el disco de tu Mac no distingue mayúsculas, el servidor sí
5. **Timeout** — el proveedor corta a los 10 o 30 segundos

Antes de tocar código, mirá los logs del despliegue. La respuesta suele estar en la primera pantalla.

## Cómo trabajar

Entregá algo que funcione de punta a punta lo antes posible, aunque sea feo: una pantalla, un endpoint, una tabla. Un camino completo y angosto revela los problemas reales —los de integración, los de permisos, los de despliegue— que ninguna cantidad de planificación anticipa.

Después ensanchalo. Es más rápido que construir tres capas perfectas que se conocen el último día.

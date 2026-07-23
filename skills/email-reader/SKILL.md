---
name: email-reader
version: "1.0.0"
description: >
  Reads and fetches emails from Gmail (all folders/labels) and IMAP accounts.
  Use when the user asks to check email, read inbox, show unread messages,
  list folders, or fetch messages from any mailbox folder.
tags: [email, gmail, imap, inbox, folders]
metadata:
  openclaw:
    emoji: "📥"
    requires:
      env:
        - name: GMAIL_CREDENTIALS_PATH
          description: "Ruta al archivo credentials.json de Gmail API"
        - name: GMAIL_TOKEN_PATH
          description: "Ruta al token OAuth generado (se crea automáticamente)"
      bins: []
    install: []
---

# Email Reader Skill

## Descripción
Esta skill conecta con Gmail (vía OAuth2) e IMAP genérico para leer correos
de TODAS las carpetas y etiquetas del usuario.

## Cuándo usarla
- "Revisa mi correo"
- "Muéstrame los no leídos"
- "¿Qué hay en mi bandeja de entrada?"
- "Lee los correos de la carpeta Proyectos"
- "Muéstrame todos mis correos de spam"
- "¿Cuántas carpetas tengo en Gmail?"
- "Revisa el hilo de [asunto]"

## Flujo de ejecución

### PASO 1 — Autenticar con Gmail
Usa el script `scripts/auth.py` para autenticar con OAuth2.
Si ya existe un token válido en `GMAIL_TOKEN_PATH`, reutilízalo.
Si el token está expirado, refrészcalo automáticamente.
Si no existe, lanza el flujo OAuth en el navegador.

```bash
python3 scripts/auth.py
```

### PASO 2 — Listar TODAS las carpetas/etiquetas
Llama a `labels.list()` de Gmail API para descubrir dinámicamente
todas las etiquetas del usuario (sistema + personalizadas):

Etiquetas de sistema conocidas: INBOX, SPAM, TRASH, SENT, DRAFTS, STARRED,
IMPORTANT, ALL_MAIL, CATEGORY_SOCIAL, CATEGORY_PROMOTIONS,
CATEGORY_UPDATES, CATEGORY_FORUMS.

```bash
python3 scripts/list_folders.py
```

Muestra al usuario la lista de carpetas encontradas y pregunta
cuáles quiere leer, o lee INBOX + SPAM por defecto.

### PASO 3 — Leer correos de cada carpeta
Para cada carpeta seleccionada, llama a `messages.list()` con paginación:
- Usa `nextPageToken` para leer más de 500 correos si es necesario.
- Guarda el ID del último correo procesado en `.email_checkpoint.json`
  para leer solo correos nuevos en la siguiente ejecución.
- Decodifica el cuerpo: primero intenta `text/plain`, luego `text/html`
  (usando BeautifulSoup para extraer texto limpio del HTML).
- Detecta y lista adjuntos (nombre, tipo MIME, tamaño) sin descargarlos.

```bash
python3 scripts/fetch_emails.py --label INBOX --max 50
python3 scripts/fetch_emails.py --label SPAM --max 50
```

### PASO 4 — Leer hilos completos (si el usuario pide contexto)
Si el usuario quiere ver la conversación completa de un correo,
usa `threads.get()` para obtener todos los mensajes del hilo.

```bash
python3 scripts/fetch_thread.py --thread-id <THREAD_ID>
```

### PASO 5 — Presentar resultados
Muestra un resumen al usuario con formato:
```
📥 INBOX — 12 correos (3 no leídos)
  • [hoy 09:14] juan@empresa.com — Propuesta Q1 2026
  • [ayer 18:30] newsletter@medium.com — Top 10 AI tools
  ...

🗑️ SPAM — 45 correos
  • [hace 2 días] promo@descuentos.xyz — ¡GANA UN IPHONE!
  ...
```

## Soporte IMAP (cuentas no-Gmail)
Para Outlook, Yahoo o servidor propio, usa `scripts/imap_fetch.py`.
Requiere variables: `IMAP_HOST`, `IMAP_USER`, `IMAP_PASSWORD`.

```bash
python3 scripts/imap_fetch.py --host imap.outlook.com --folder INBOX
```

## Parámetros disponibles
- `--label` / `--folder`: carpeta específica a leer
- `--max`: máximo de correos a traer (defecto: 50)
- `--unread-only`: solo correos no leídos
- `--since`: correos desde una fecha (ej: "2026-01-01")
- `--from`: filtrar por remitente
- `--all-folders`: leer todas las carpetas

## Notas de seguridad
- El token OAuth se cifra en reposo con `cryptography.fernet`.
- No loguear cuerpos de correos con datos sensibles.
- Respetar el límite de Gmail API: 250 unidades/usuario/segundo.
  Usar backoff exponencial si se recibe error 429.

# AI Dev Server Guide

Reference for AI agents interacting with the Astro development server programmatically.

---

## 1. Background Mode

Start the dev server as a detached background process that blocks until the server is fully ready to accept requests:

```bash
astro dev --background
```

### Auto-Detection

Astro automatically detects AI agent environments and enables background mode without explicit flags. This applies to known CI/agent runtimes.

### Lockfile

A lockfile at `.astro/dev.json` prevents duplicate server instances. If a server is already running, the lockfile ensures a second `astro dev --background` call returns the existing instance info instead of spawning a new process.

### Commands

| Command | Description |
|---------|-------------|
| `astro dev --background` | Start detached server, block until ready |
| `astro dev stop` | Stop the running background server |
| `astro dev status` | Check if a background server is running |
| `astro dev logs` | Stream logs from the background server |

### Opt-Out

Disable automatic background mode by setting the environment variable:

```bash
ASTRO_DEV_BACKGROUND=0 astro dev
```

---

## 2. Health Endpoint

Verify the dev server is ready before making requests:

```
GET /_astro/status
```

Response:

```json
{"ok": true}
```

> **Important:** This endpoint is only available in development mode. It does not exist in production builds.

### Usage

```bash
curl http://localhost:4321/_astro/status
```

Wait for a `200` response with `{"ok": true}` before issuing any page requests.

---

## 3. JSON Logging

Enable structured JSON output for machine-readable log parsing:

```bash
astro dev --json
```

### Configuration in `astro.config.mjs`

```js
import { logHandlers } from 'astro';

export default defineConfig({
  logger: logHandlers.json(),
});
```

### Compose Multiple Handlers

Output to both console and JSON simultaneously:

```js
import { logHandlers } from 'astro';

export default defineConfig({
  logger: logHandlers.compose(
    logHandlers.console(),
    logHandlers.json()
  ),
});
```

### Auto-Enabled

JSON logging is automatically enabled when an AI agent environment is detected.

### Use Cases

- Error parsing — structured error objects with file, line, column
- Build status — track compilation progress programmatically
- HMR events — detect when hot module replacement completes after file changes

---

## 4. Agent Workflow

Step-by-step workflow for AI agents developing with Astro:

```bash
# 1. Start the dev server in background (blocks until ready)
astro dev --background

# 2. Verify the server is ready
curl http://localhost:4321/_astro/status

# 3. Make changes to source files
# (edit .astro, .ts, .css files as needed)

# 4. Verify output after HMR processes changes
curl http://localhost:4321/page-to-test

# 5. Cleanup when done
astro dev stop
```

### Notes

- Step 2 should return `{"ok": true}` before proceeding.
- After step 3, wait briefly for HMR to process before step 4.
- Always run step 5 to avoid orphaned processes.

---

## 5. Idempotency Rules

The dev server commands are designed to be safely called multiple times:

| Scenario | Behavior |
|----------|----------|
| Start when already running | Returns existing instance info (port, PID) |
| Stop when not running | Silent success (exit code 0) |
| Crash or unexpected termination | Lockfile is cleaned up, no zombie processes |

These guarantees mean agents can call `astro dev --background` at the start of every task without checking current state first, and call `astro dev stop` at cleanup without error handling.

---

## 6. MCP Integration

The Astro Docs MCP server provides real-time documentation access:

- **Endpoint:** `https://mcp.docs.astro.build/mcp`
- **Tool:** `search_astro_docs`

### Usage

Always query the MCP server for the latest API details, configuration options, and component references rather than relying on cached knowledge.

```
search_astro_docs("dev server background mode")
search_astro_docs("content collections config")
```

This ensures agents work with current documentation even as Astro's API evolves between versions.

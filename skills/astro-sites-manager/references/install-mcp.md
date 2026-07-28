# Installing the Astro Docs MCP Server

The Astro Docs MCP server provides real-time access to the latest Astro documentation via the Model Context Protocol.

- **URL:** `https://mcp.docs.astro.build/mcp`
- **Transport:** Streamable HTTP
- **Tool:** `search_astro_docs`
- **Source:** Open-source, powered by kapa.ai

---

## By Tool

### Kiro CLI

```bash
kiro-cli mcp add --name astro-docs --scope global --command npx --args "-y" --args "mcp-remote" --args "https://mcp.docs.astro.build/mcp"
```

Or create/edit `~/.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "astro-docs": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"],
      "env": {}
    }
  }
}
```

### Claude Code CLI

```bash
claude mcp add --transport http astro-docs https://mcp.docs.astro.build/mcp
```

### Codex CLI

Add to `~/.codex/config.toml`:

```toml
[mcp_servers.astro-docs]
command = "npx"
args = ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
```

### Cursor

Use the deeplink or add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "Astro docs": {
      "type": "http",
      "url": "https://mcp.docs.astro.build/mcp"
    }
  }
}
```

### VS Code (Copilot Chat)

Add to `.vscode/mcp.json`:

```json
{
  "mcpServers": {
    "Astro docs": {
      "type": "http",
      "url": "https://mcp.docs.astro.build/mcp"
    }
  }
}
```

### Windsurf

Edit `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "Astro docs": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
    }
  }
}
```

### Gemini CLI

Add to `.gemini/settings.json`:

```json
{
  "mcpServers": {
    "Astro docs": {
      "httpUrl": "https://mcp.docs.astro.build/mcp"
    }
  }
}
```

### Zed

Add to `~/.config/zed/settings.json`:

```json
{
  "context_servers": {
    "Astro docs": {
      "settings": {},
      "enabled": true,
      "url": "https://mcp.docs.astro.build/mcp"
    }
  }
}
```

### Claude.ai / Claude Desktop

1. Go to Settings → Connectors
2. Click "Add custom connector"
3. URL: `https://mcp.docs.astro.build/mcp`
4. Name: `Astro docs`

### Warp

Settings → AI → MCP Servers → Add:

```json
{
  "mcpServers": {
    "Astro docs": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"],
      "start_on_launch": true
    }
  }
}
```

---

## Generic (any tool supporting MCP)

**Streamable HTTP** (preferred):

```json
{
  "mcpServers": {
    "Astro docs": {
      "type": "http",
      "url": "https://mcp.docs.astro.build/mcp"
    }
  }
}
```

**Local Proxy** (for tools that only support stdio):

```json
{
  "mcpServers": {
    "Astro docs": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.docs.astro.build/mcp"]
    }
  }
}
```

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Server not responding | Verify URL is exactly `https://mcp.docs.astro.build/mcp` |
| Tool not connecting | Check internet access; some firewalls block MCP |
| Stale results | MCP always fetches latest docs — no cache to clear |
| Local proxy crashes | Ensure `npx` is in PATH and Node.js ≥ 18 installed |

Issues: https://github.com/withastro/docs-mcp/issues

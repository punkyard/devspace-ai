---
description: "Context7 MCP install and usage notes; use for editor integrations"
---
# 📚 Context7 MCP — install & usage (draft)

## ✅ Prerequisites

- Node.js >= 18 or bun
- Context7 API key (optional for higher rate limits)

## 🚀 Run via NPX (stdio transport, recommended)

```
npx -y @upstash/context7-mcp --transport stdio
```

## ⚙️ VS Code `mcp.json` snippet

Use an input prompt to avoid committing secrets:

```
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp", "--transport", "stdio"],
      "env": { "CONTEXT7_API_KEY": "${input:context7-api-key}" }
    }
  }
}
```

## 🔧 Tools exposed

- `resolve-library-id` — resolve a library name to a context7 ID
- `get-library-docs` — fetch docs for a library id (supports topic and tokens limits)

## 📝 Notes

- prefer STDIO transport for local editor integration — SSE is deprecated
- MCP client = VS Code with MCP integration (this workspace uses `.vscode/mcp.json`)
- rule: for code-generation that needs docs, first `use context7` to fetch docs, then generate code

## 🔒 Secrets

- use `CONTEXT7_API_KEY` as env var locally and `${input:context7-api-key}` in `.vscode/mcp.json`
- do NOT commit keys

## 🔑 Create a Context7 API key

1. create an account at Upstash (Context7 is an Upstash product)
2. in the Upstash console, create a Context7 project (library/docs service)
3. open the project settings and generate an API key (copy it)
4. in VS Code, when prompted by `.vscode/mcp.json` input `context7-api-key`, paste the key (it is stored securely by VS Code)

tip: if the internet is unavailable right now, skip this and proceed; Copilot will remind you to complete it later

## tie-in with README checklist

- the README includes tasks to create API keys and start the MCP servers; the start prompt will walk the user through those steps
- see also `mcp-bravesearch.instructions.md` for Brave API key creation

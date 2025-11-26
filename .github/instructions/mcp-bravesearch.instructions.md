# ---
applyTo: '**'
description: "Brave Search MCP install and usage notes; use for web search, news, images, video and summarizer"
---
# 🔍 Brave Search MCP — install & usage (draft)

This file documents how to install and run the Brave Search MCP server for use as an MCP in editors and agents.

## ✅ Prerequisites

- Node.js 22+ and npm, or Docker
- Brave Search API key input (do not commit)

## 🚀 Run via NPX (stdio transport, recommended)

```
npx -y @brave/brave-search-mcp-server --transport stdio
```

## ⚙️ VS Code `mcp.json` snippet

Use an input prompt to avoid committing secrets:

```
{
  "inputs": [
    {
      "password": true,
      "id": "brave-api-key",
      "type": "promptString",
      "description": "Brave Search API Key"
    }
  ],
  "servers": {
    "brave-search-mcp": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server", "--transport", "stdio"],
      "env": { "BRAVE_API_KEY": "${input:brave-api-key}" }
    }
  }
}
```

## 🐳 Docker run example (local)

```
docker run -i --rm -e BRAVE_API_KEY="$BRAVE_API_KEY" mcp/brave-search
```

**Tool whitelist:** prefer to enable only `brave_web_search` and `brave_summarizer` unless other tools are needed — use `--enabled-tools` to whitelist.

**Security note:** do not store tokens in repository — use VS Code inputs, environment variables, or local .env files (gitignored).

## 🔒 Secrets

- use the environment variable name `BRAVE_API_KEY` for local runs and in `.vscode/mcp.json` inputs
- do NOT commit API keys — use `${input:brave-api-key}` in `.vscode/mcp.json` or set `BRAVE_API_KEY` in your local environment
- if a session note in `/context/` references keys or setup steps, mark it `safe-to-push: false` unless you remove secrets first

## 🔑 Create a Brave Search API key

1. create a Brave account and go to the Brave Search API dashboard
2. create a new API key for the Search API and copy it
3. in VS Code, when prompted by `.vscode/mcp.json` input `brave-api-key`, paste the key (stored securely by VS Code)
4. for local shell use, export it as `BRAVE_API_KEY` for this session only

tip: if the internet is unavailable, skip now and proceed; Copilot will remind you to complete this later

## tie-in with README and start prompt

- README includes tasks to create API keys and start MCP servers
- `.github/prompts/start.prompt.md` will guide the user through these steps when the “start” task is run

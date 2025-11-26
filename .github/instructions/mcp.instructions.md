---
applyTo: '**'
description: "MCP servers — workspace guidance and conventions for local VS Code MCP servers"
---
# 🔌 MCP servers — workspace guidance

This file documents how MCP servers are defined for this workspace and the conventions used.

- preferred transport: `stdio` (default) for local security and compatibility with VS Code/Claude Desktop
- use `.vscode/mcp.json` for editor-local server entries and use VS Code `inputs` for secret prompts
- use API_KEYs as input variables when running MCP servers locally
- do NOT commit API keys — use VS Code inputs or environment variables

## 📋 MCP servers in this workspace

| name | package/command | env var | typical use |
|------|-----------------|---------|-------------|
| Time | `mcp-server-time` (uvx … --local-timezone Europe/Paris) | none | canonical timestamps, timezone conversions |
| Brave Search | `@brave/brave-search-mcp-server` (npx -y … --transport stdio) | `BRAVE_API_KEY` | web search, news, image, video, summarizer |
| Context7 | `@upstash/context7-mcp` (npx -y … --transport stdio) | `CONTEXT7_API_KEY` | fetch library docs, code-centric context |
| GitHub | `@mcp/github` (npx -y … --transport stdio) | `GITHUB_TOKEN` | repo metadata, PRs, issues, releases |

**Usage rule:** for code-generation that needs docs, prefer Context7 first, then synthesize.

See `mcp-time.instructions.md`, `mcp-bravesearch.instructions.md`, `mcp-context7.instructions.md` and `mcp-github.instructions.md` for installation process and concrete examples.

VS Code automatically starts MCP servers when Copilot uses them (no manual start required).

## MCP best practices

- prefer stdio for local MCP servers; use http/sse only when necessary
- configure sensitive inputs in `.vscode/mcp.json` using `inputs`; never commit API keys
- grant minimum required scopes for PATs and tools; avoid broad permissions
- install and start servers only from trusted sources and review the command used
- use clear naming: camelCase for servers, snake_case for tool names
- group related tools in tool sets and avoid enabling more than 128 tools per request
- use dev/watch/debug modes while developing servers and enable autostart only when safe
- require explicit user approval for sampling or file-writing tools; use read-only tools when possible

> print "🛠️ MCP" each time you read this file
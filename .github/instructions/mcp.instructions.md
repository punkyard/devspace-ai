# 🔌 MCP servers — workspace guidance

This file documents how MCP servers are defined for this workspace and the conventions used.

- preferred transport: `stdio` (default) for local security and compatibility with VS Code/Claude Desktop
- use `.vscode/mcp.json` for editor-local server entries and use VS Code `inputs` for secret prompts
- use API_KEYs as input variables when running MCP servers locally
- do NOT commit API keys — use VS Code inputs or environment variables

## 📋 MCP servers in this workspace

| name | package/command | env var | typical use |
|------|-----------------|---------|-------------|
| Brave Search | `@brave/brave-search-mcp-server` (npx -y … --transport stdio) | `BRAVE_API_KEY` | web search, news, image, video, summarizer |
| Context7 | `@upstash/context7-mcp` (npx -y … --transport stdio) | `CONTEXT7_API_KEY` | fetch library docs, code-centric context |

**Usage rule:** for code-generation that needs docs, prefer Context7 first, then synthesize.

See `mcp-bravesearch.instructions.md` and `mcp-context7.instructions.md` for installation process and concrete examples.

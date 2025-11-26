---
description: "GitHub MCP install and usage notes; use for repository metadata, PRs, issues"
---
# 🔧 GitHub MCP — install & usage (draft)

This file documents how to install and run a GitHub MCP server for use as an MCP in editors and agents when the workspace needs to access repository, issue, or PR data.

## ✅ Prerequisites

- Node.js 22+ and npm, or Docker
- a GitHub Personal Access Token (PAT) with minimal scopes required (e.g., `repo` for private repos, `public_repo` for public-only usage) — do not commit
- for GitHub Enterprise: optionally set `GITHUB_API_URL` to the enterprise hostname

## 🚀 Run via NPX (stdio transport, recommended)

```
npx -y @mcp/github --transport stdio
```

## ⚙️ VS Code `mcp.json` snippet

Use editor inputs to avoid committing secrets. Example:

```
{
  "inputs": [
    {
      "password": true,
      "id": "github-pat",
      "type": "promptString",
      "description": "GitHub Personal Access Token (PAT)"
    },
    {
      "id": "github-api-url",
      "type": "promptString",
      "description": "(optional) GitHub API URL for enterprise hosts",
      "default": "https://api.github.com"
    }
  ],
  "servers": {
    "github-mcp": {
      "command": "npx",
      "args": ["-y", "@mcp/github", "--transport", "stdio"],
      "env": { "GITHUB_TOKEN": "${input:github-pat}", "GITHUB_API_URL": "${input:github-api-url}" }
    }
  }
}
```

## 🐳 Docker run example (local)

```
docker run -i --rm -e GITHUB_TOKEN="$GITHUB_TOKEN" -e GITHUB_API_URL="$GITHUB_API_URL" mcp/github
```

**Tool whitelist:** Prefer read-only endpoints (e.g., `repos`, `pulls`, `issues`) unless write operations are needed; grant minimal scopes on PATs.

**Security note:** do not store tokens in repository — use VS Code inputs, environment variables, or local .env files (gitignored).

## 🔒 Secrets

Always store PATs using editor inputs or environment variables; rotate tokens frequently and minimize scopes.

## 📝 Usage

- Use the GitHub MCP for repository metadata, PR details, issue searches, release assets, and basic code browsing when building code-aware features.
- Avoid enabling broad scopes unless required (e.g., `workflow` write permissions for actions).
- For large repos or enterprises, consider the `GITHUB_API_URL` to point to a local enterprise endpoint.

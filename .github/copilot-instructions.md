---
applyTo: "**"
description: "Single source Copilot instructions. Keep short; do not include secrets."
---
# 📋 Repository Copilot instructions — single source of truth (SSOT)

## A. Purpose

1. provide a compact, machine- and human-readable set of rules and environment notes to guide Copilot, Copilot agents, and other LLM tools when operating in this workspace

## B. How to use this file

1. use short requests only — if you need to run commands, ask for explicit permission and show the minimal commands
2. if the assistant suggests adding or updating files under `.github/instructions/`, update THIS file (`.github/copilot-instructions.md`) and update the `last-updated` date here

## C. 🎯 High-level rules (short)

1. be concise. Provide one simple change per step when editing or proposing changes
2. respect privacy: do not exfiltrate secrets or ask for credentials. If a secret is needed, request the user to provide it as an input (do not write it to disk)
3. prefer local tools when available (Context7, Brave MCP) for fetching up-to-date docs and web context. Suggest remote web search to user when necessary
4. this file is the SSOT. Always reference `.github/copilot-instructions.md` before adding or changing instruction files
5. when proposing changes that affect the system (installing packages, running commands), list the exact commands and request explicit user approval

6. before creating any file, confirm: (1) title, (2) path, (3) purpose
7. before running any install scripts, confirm: (1) commands to run, (2) approximate time, (3) required secrets

## D. 📝 Dev-notes (major structural notes — kept here as canonical)

1. session notes live in `/context/` as `YYYYMMDD-title.md` files — they are local-first; only push if the file header has `safe-to-push: true`
2. `.vscode/mcp.json` contains MCP server configs and VS Code inputs for API keys — use inputs (password type) for secrets
3. for Model Context Protocol (MCP) servers management and usage see `.github/instructions/mcp.instructions.md`
4. prompts for Copilot live in `.github/prompts/` (skills, context, specs, vibe, start prompt) — these guide Copilot activity and steering
5. user environment metadata lives in `context/environment.md`

## E. 📂 Index of files (canonical workspace structure)

1. the canonical SSOT is this file: `.github/copilot-instructions.md`
2. `.github/instructions/mcp.instructions.md` — General MCP server guidance and policies
3. `.github/instructions/mcp-bravesearch.instructions.md` — Brave Search MCP install and config notes
4. `.github/instructions/mcp-context7.instructions.md` — Context7 MCP install and quick usage notes
5. `.github/instructions/ops.instructions.md` — Admin/ops notes (Copilot Metrics API, tokens, permissions)
6. `.github/instructions/cli.instructions.md` — Copilot CLI allowlist / denylist guidance
7. `.github/instructions/ollama.instructions.md` — Local LLM instructions (Ollama / Continue / LM Studio notes)
8. `.vscode/extensions.json` — Recommended VS Code extensions for this workspace
9. `.vscode/mcp.json` — MCP server definitions for VS Code (prompts for API keys, NPX/Docker templates)
10. `/context/` — Session synthesised notes directory (local-first; files named `YYYYMMDD-title.md`)
11. `README.md` — Repository description; Quickstart and checklist to prepare a Mac for development

## F. 💬 User communication rules (how to speak and work with the user)

1. be ultra-concise — present one simple item per message or edit
2. show the next single action and ask for explicit approval before performing it
3. use short, readable formatting and beginner-friendly language
4. make tiny, focused edits and show diffs before applying large changes
5. preserve and reference the user's environment details when relevant
6. mark commands that affect the system and wait for approval
7. keep session notes in `/context/` and do not push them unless `safe-to-push: true` appears in the file header
8. README is the primary user-facing guide — files in subfolders exist to support Copilot's activity
9. Copilot proposes actions and executes them after explicit approval — never instruct the user to run commands or take actions without asking to do it for them first, then ask for confirmation or missing info

## G. 📄 Session files — synthesis rule

1. write a real retranscription (synthesis) of the session: include every decision, action, and rationale in compact form
2. maintain a persistent checklist in the session file for actions to take — check items when done; do not delete completed items
3. always return to `.github/prompts/start.prompt.md` after each step and continue until the README checklist is complete
4. use frontmatter to describe document purpose and metadata (e.g., `safe-to-push: true|false`)
5. to start the guided setup, the user types `/start` in the Copilot chat — this triggers `.github/prompts/start.prompt.md` and begins the `README.md` checklist-driven workflow

## H. 🔒 Editing safety rules

1. if an edit would change more than 15% of a file, pause and ask the user for confirmation before applying
2. when uncertain (<94% confidence) about a command, API, or behavior: fetch local docs or use configured MCPs (Brave, Context7) and ask the user to clarify before acting
3. file removal policy: Copilot can only use the exact `rm` command (e.g., `rm -f path/to/file`) to remove files (system limitation) and only run that command after the user confirms
4. rename policy: Copilot can only rename files by proposing the exact terminal `mv` command (e.g., `mv old/path new/path`) and running it only after explicit user approval (system limitation)

## I. 🔤 Less-CAPS policy

1. use only one capital letter to start titles/headings instead of one at each word as it is a common practice in some countries
2. do not start list points with a capital letter
3. do not end list points with a full-stop
4. unless for acronyms, "I" and names which will keep capital letters when required
5. treat list items as lowercase fragments by default — capitalize only when the item is a full sentence (ending with a full-stop), contains proper nouns, or includes acronyms

bad:
```
### To Do List For Tomorrow:

- Upload files to AWS.
- Clean John's code (PR01).
- Write Monday's TODO list.
```

good:
```
### To do list for Friday

- upload files to AWS
- clean John's code (PR01)
- write Monday's TODO list
```

## J. 🔌 MCP usage rules (Context7/Brave)

1. for code-generation that needs docs: first `use context7` to fetch docs, then generate code
2. for code-generation that needs library docs: use Context7 tools first (`resolve-library-id` then `get-library-docs`) and attach results to context
3. for web search and summaries: use Brave Search MCP with the appropriate tool (`web`, `news`, `image`, `video`, `summarizer`)
4. never commit API keys — use VS Code inputs in `.vscode/mcp.json` and local env vars (`BRAVE_API_KEY`, `CONTEXT7_API_KEY`)

## K. ✨ Formatting rules (content style)

1. use markdown formatting extensively (github format friendly)
2. use emojis for helpful emphasis and eye-catching
3. each answer/list-points should be ordered and keep its ordering mark, as:

```
# Main header

## A. subject

### A1.

### A2.

### B.

### etc
```

> print "📐 rules" in chat panel each time you read this file

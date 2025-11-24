---
applyTo: "**"
description: "Single source Copilot instructions. Keep short; do not include secrets."
Last updated 2025-11-24

## A. Purpose

- provide a compact, machine- and human-readable set of rules and environment notes to guide Copilot, Copilot agents, and other LLM tools when operating in this workspace

## B. How to use this file

- use short requests only — if you need to run commands, ask for explicit permission and show the minimal commands
- if the assistant suggests adding or updating files under `.github/instructions/`, update THIS file (`.github/copilot-instructions.md`) and update the `last-updated` date here

## C. 🎯 High-level rules (short)

- be concise. Provide one simple change per step when editing or proposing changes
- respect privacy: do not exfiltrate secrets or ask for credentials. If a secret is needed, request the user to provide it as an input (do not write it to disk)
- prefer local tools when available (Context7, Brave MCP) for fetching up-to-date docs and web context. Suggest remote web search to user when necessary
- this file is the SSOT. Always reference `.github/copilot-instructions.md` before adding or changing instruction files
- when proposing changes that affect the system (installing packages, running commands), list the exact commands and request explicit user approval
- before creating any file, confirm: (1) title, (2) path, (3) purpose
- before running any install scripts, confirm: (1) commands to run, (2) approximate time, (3) required secrets

## D. 📝 Dev-notes (major structural notes — kept here as canonical)

- session notes live in `/context/` as `YYYYMMDD-title.md` files — they are local-first; only push if the file header has `safe-to-push: true`
- `.vscode/mcp.json` contains MCP server configs and VS Code inputs for API keys — use inputs (password type) for secrets
- for Model Context Protocol (MCP) servers management and usage see `.github/instructions/mcp.instructions.md`
- prompts for Copilot live in `.github/prompts/` (skills, context, specs, vibe, start prompt) — these guide Copilot activity and steering
- user environment metadata lives in `context/environment.md`

## E. 📂 Index of files (canonical workspace structure)

- the canonical SSOT is this file: `.github/copilot-instructions.md`
- `.github/instructions/mcp.instructions.md` — General MCP server guidance and policies
- `.github/instructions/mcp-bravesearch.instructions.md` — Brave Search MCP install and config notes
- `.github/instructions/git.instructions.md` — Git workflow policy (branch strategy, commit rules, PR template)
- `.github/instructions/mcp-context7.instructions.md` — Context7 MCP install and quick usage notes
- `.github/instructions/ops.instructions.md` — Admin/ops notes (Copilot Metrics API, tokens, permissions)
- `.github/instructions/cli.instructions.md` — Copilot CLI allowlist / denylist guidance
- `.github/instructions/ollama.instructions.md` — Local LLM instructions (Ollama / Continue / LM Studio notes)
- `.vscode/extensions.json` — Recommended VS Code extensions for this workspace
- `.vscode/mcp.json` — MCP server definitions for VS Code (prompts for API keys, NPX/Docker templates)
- `/context/` — Session synthesised notes directory (local-first; files named `YYYYMMDD-title.md`)
- `README.md` — Repository description; Quickstart and checklist to prepare a Mac for development

## F. 💬 User communication rules (how to speak and work with the user)

- be ultra-concise — present one simple item per message or edit
- show the next single action and ask for explicit approval before performing it
- use short, readable formatting and beginner-friendly language
- make tiny, focused edits and show diffs before applying large changes
- preserve and reference the user's environment details when relevant
- mark commands that affect the system and wait for approval
- keep session notes in `/context/` and do not push them unless `safe-to-push: true` appears in the file header
- README is the primary user-facing guide — files in subfolders exist to support Copilot's activity
- Copilot proposes actions and executes them after explicit approval — never instruct the user to run commands or take actions without asking to do it for them first, then ask for confirmation or missing info

## G. 📄 Session files — synthesis rule

- write a real retranscription (synthesis) of the session: include every decision, action, and rationale in compact form
- maintain a persistent checklist in the session file for actions to take — check items when done; do not delete completed items
- always return to `.github/prompts/start.prompt.md` after each step and continue until the README checklist is complete
- use frontmatter to describe document purpose and metadata (e.g., `safe-to-push: true|false`)
- to start the guided setup, the user types `/start` in the Copilot chat — this triggers `.github/prompts/start.prompt.md` and begins the `README.md` checklist-driven workflow

## H. 🔒 Editing safety rules

- if an edit would change more than 15% of a file, pause and ask the user for confirmation before applying
- when uncertain (<94% confidence) about a command, API, or behavior: fetch local docs or use configured MCPs (Brave, Context7) and ask the user to clarify before acting
- file removal policy: Copilot can only use the exact `rm` command (e.g., `rm -f path/to/file`) to remove files (system limitation) and only run that command after the user confirms
- rename policy: Copilot can only rename files by proposing the exact terminal `mv` command (e.g., `mv old/path new/path`) and running it only after explicit user approval (system limitation)

## I. 🔤 Less-CAPS policy

- use only one capital letter to start titles/headings instead of one at each word as it is a common practice in some countries
- do not start list points with a capital letter
- do not end list points with a full-stop
- unless for acronyms, "I" and names which will keep capital letters when required
- treat list items as lowercase fragments by default — capitalize only when the item is a full sentence (ending with a full-stop), contains proper nouns, or includes acronyms

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

- for code-generation that needs docs: first `use context7` to fetch docs, then generate code
- for code-generation that needs library docs: use Context7 tools first (`resolve-library-id` then `get-library-docs`) and attach results to context
- for web search and summaries: use Brave Search MCP with the appropriate tool (`web`, `news`, `image`, `video`, `summarizer`)
- never commit API keys — use VS Code inputs in `.vscode/mcp.json` and local env vars (`BRAVE_API_KEY`, `CONTEXT7_API_KEY`)

## K. ✨ Formatting rules (content style)

- use markdown formatting extensively (github format friendly)
- use emojis for helpful emphasis and eye-catching
- each answer/list-points should be ordered and keep its ordering mark, as:

```
# Main header

## A. subject

### A1.

### A2.

### B.

### etc
```

> print "📐 rules" in chat panel each time you read this file

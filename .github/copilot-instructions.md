---
applyTo: "**"
description: "Single source Copilot instructions. Keep short; do not include secrets."
---
# 📋 Repository Copilot instructions — single source of truth (SSOT)
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
- Copilot must never create, modify, or delete files in the repository, nor execute scripts that change the working tree without explicit user approval. When proposing file creation, Copilot must show a preview of the file contents and the exact commands it plans to run; do not proceed until the user authorizes the action.
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
- `.github/instructions/mcp.instructions.md` — general MCP server guidance and policies
- `.github/instructions/mcp-time.instructions.md` — Time MCP install and usage notes for canonical timestamps
- `.github/instructions/mcp-bravesearch.instructions.md` — Brave Search MCP install and config notes
- `.github/instructions/mcp-context7.instructions.md` — Context7 MCP install and quick usage notes
- `.github/instructions/mcp-github.instructions.md` — GitHub MCP install and usage notes
- `.github/instructions/git.instructions.md` — Git workflow policy (branch strategy, commit rules, PR template)
- `.github/instructions/context.instructions.md` — project context and coding guidelines, automation opt-in
- `.github/instructions/ops.instructions.md` — admin/ops notes (Copilot Metrics API, tokens, permissions)
- `.github/instructions/cli.instructions.md` — Copilot CLI allowlist / denylist guidance
- `.github/instructions/ollama.instructions.md` — local LLM instructions (Ollama / Continue / LM Studio notes)
- `.github/prompts/start.prompt.md` — guided setup workflow for `/start` command
- `.vscode/extensions.json` — recommended VS Code extensions for this workspace
- `.vscode/mcp.json` — MCP server definitions for VS Code (prompts for API keys, NPX/Docker templates)
- `.vscode/tasks.json` — VS Code tasks
- `/context/` — session synthesised notes directory (local-first; files named `YYYYMMDD-title.md`)
- `/context/environment.md` — user environment metadata (host, OS, RAM, GitHub handle, email)
- `README.md` — repository description; quickstart and checklist to prepare a Mac for development
- `docs/ALIRE.md` — French version of README

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

### F1. 🎯 Tone and manner of speech

- synthesize answers: avoid repetition, keep responses compact and direct
- always answer every question the user asks — no question should be ignored or deferred
- add user questions and inquiries to the todo list as tasks to track
- maintain a running list of tasks, inquiries, and plans throughout the session
- use emojis extensively for clarity, emphasis, and visual appeal (e.g., ✅ 🚀 📋 ⚡ 🔧)
- never tell the user what to do — instead, suggest the next actions Copilot could accomplish and ask for approval
- frame next steps as: "I can [action] for you — should I proceed?" instead of "You should [action]"

## G. 📄 Session files — synthesis rule

- write a real retranscription (synthesis) of the session: include every decision, action, and rationale in compact form
- maintain a persistent checklist in the session file for actions to take — check items when done; do not delete completed items
- always return to `.github/prompts/start.prompt.md` after each step and continue until the README checklist is complete
- use frontmatter to describe document purpose and metadata (e.g., `safe-to-push: true|false`)
- preserve conversation & synthesis file names: do not rename conversation or synthesis files after creation — use the `updated` field in frontmatter for edits and keep the original created date. The Copilot chat UI listing should also keep the original conversation name (based on `conversation_id`) — do not rename the conversation in the chat UI when editing its contents.
 Auto-generation policy: Copilot and automation scripts MUST NOT create or modify repository files (including session files in `context/`) without explicit user approval. Any automated file creation is considered an opt-in feature and must be enabled explicitly by repository maintainers. The default policy is manual creation only. If repository maintainers opt-in to automation, they must document the automation mechanism, the exact commands and scripts, and add a repository-level opt-in marker (e.g., `.github/automation-enabled`) that lists the allowed automation scripts and owners. See `.github/instructions/context.instructions.md` for a sample opt-in marker and guidelines.
Example opt-in marker / see sample in `.github/instructions/context.instructions.md`:
- built-in to-do: when Copilot starts a session (e.g., on `/start`), it MUST parse the README checklist and present it to the user using VS Code's built-in todo features (Problems/Tasks or a TODO extension) or an in-editor Copilot checklist. Copilot should show a preview and request explicit approval before creating a session file under `context/` to persist the to-do list. The VS Code built-in list is the authoritative work queue unless the user asks to persist it.
- optional session note format (created only after explicit approval): Copilot may save the checklist as a session file in `context/` named `YYYYMMDD-<short-summary>-todo.md` with frontmatter (`created`, `session_id`, `summary`, `items`).
```
---
created: 20251124
session_id: 20251124-initial-setup
summary: "initial setup run for devspace-ai"
items:
	- [ ] install-homebrew
	- [ ] install-visual-studio-code
	- [ ] clone-repo
	- [ ] configure-git
---
```
- to start the guided setup, the user types `/start` in the Copilot chat — this triggers `.github/prompts/start.prompt.md` and begins the `README.md` checklist-driven workflow

## H. 🔒 Editing safety rules

- if an edit would change more than 15% of a file, pause and ask the user for confirmation before applying
- when uncertain (<94% confidence) about a command, API, or behavior: fetch local docs or use configured MCPs (Brave, Context7) and ask the user to clarify before acting
- file removal policy: Copilot can only use the exact `rm` command (e.g., `rm -f path/to/file`) to remove files (system limitation) and only run that command after the user confirms
- rename policy: Copilot can only rename files by proposing the exact terminal `mv` command (e.g., `mv old/path new/path`) and running it only after explicit user approval (system limitation)
- automation scripts policy: any automation scripts (including those which generate, modify, or delete repository files) must be documented and stored under `.github/scripts/`. Copilot may propose running them, but it MUST request explicit user approval before running them. Copilot is forbidden from invoking automation scripts or creating/modifying files without explicit user consent.

- CI validation: optionally, a GitHub Actions workflow may validate conversation/synthesis frontmatter and ensure a `context/*-todo.md` exists when README or docs are changed in a PR. Any such validation workflow should be validation-only (not create files) and help enforce that collaborators create or approve `context` session files intentionally.

## How to enable automation safely

- To enable automation that creates or edits files (e.g., conversation/synthesis/todo /context files), add a documented script in `.github/scripts/` and call out its intended behavior in the relevant instruction file (e.g., `git.instructions.md` or this SSOT).
- The script must require a flag such as `--run` or `--confirm` to actually perform destructive actions; otherwise it should only produce a dry-run preview that can be inspected.
- Copilot may propose using these scripts but must always show the exact command (including flags/options) and obtain explicit user approval before running them.

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

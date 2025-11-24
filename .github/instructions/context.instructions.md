---
applyTo: '**'
---
Provide project context and coding guidelines that AI should follow when generating code, answering questions, or reviewing changes.

## Automation opt-in and safety

This file includes a **sample opt-in marker** for enabling repository automation that would create or modify files (for example, conversation/synthesis/todo files in `context/`). Automation is OFF by default and must be explicitly enabled by maintainers for safety. The purpose of the opt-in marker is to ensure explicit consent from repository maintainers before enabling any automation that writes to the repository.

Example opt-in marker (create `.github/automation-enabled` and set `enabled: true` to opt-in):

```
enabled: false # set to true to allow controlled automation
allowed-scripts:
	- .github/scripts/*
owners:
	- <maintainer-github-handle>
```

Notes:
- the `allowed-scripts` entries must be exact script paths under `.github/scripts/`
- `owners` must list GitHub handles authorized to opt-in and approve automation enablement
- scripts should require a confirm flag (e.g., `--run`, `--confirm`) to perform operations that change the working tree
- Copilot must always show a preview of the files it will create and ask for explicit approval before running any script that modifies the repo

How to enable:
1. Copy the sample into `.github/automation-enabled` and set `enabled: true`.
2. Add the exact script(s) to `allowed-scripts` (e.g., `.github/scripts/generate_context_files.py`). If a referenced script does not exist in the repository, either add the intended automation script under `.github/scripts/` or remove the entry — the file must accurately reflect allowed scripts.
3. Add a line for `owners` containing the maintainers that must approve automation for the project.
4. Update documentation in `.github/instructions/` to explain each script's purpose, flags, and required approval process.

If you enable automation, it is your responsibility to monitor and review its actions and ensure it uses safe defaults (for example, `--dry-run` first).
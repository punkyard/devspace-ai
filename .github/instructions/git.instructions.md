---
applyTo: '**'
---
# Git Workflow Policy

## Branch Strategy

### Main Branches
- **`main`** - Production-ready code. Always stable and deployable.
- **`develop`** - Integration branch for features. Latest development changes.

### Supporting Branches
- **`feature/*`** - New features (e.g., `feature/cursor-improvements`)
- **`bugfix/*`** - Bug fixes (e.g., `bugfix/tokenizer-crash`)
- **`hotfix/*`** - Urgent production fixes (e.g., `hotfix/security-patch`)
- **`refactor/*`** - Code refactoring (e.g., `refactor/line-patcher`)

## Commit Guidelines

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks, dependencies

### Examples
```
feat(tokenizer): add support for nested code blocks

fix(cursor): preserve cursor position during line patching

docs(readme): update installation instructions

refactor(app): extract markdown processing into separate module
```

### Commit Best Practices
- Keep commits atomic (one logical change per commit)
- Write clear, descriptive commit messages
- Use present tense ("add feature" not "added feature")
- Reference issue numbers when applicable (e.g., "fixes #123")

### Conversation & context synthesis on commit

- Purpose: create a precise, timestamped synthesis of the conversation that led to a commit and store it in `context/` alongside the code change. This provides clear traceability between code changes and the conversational decisions that motivated them.
- Rule: Every commit should include one conversation transcript file and one synthesis file in the `context/` folder. Both files must share the same base name and creation timestamp so they can be paired together. Do not rename files after creation; instead, record modifications with an `updated:` field in the frontmatter.
 - Rule: Every commit should include one conversation transcript file and one synthesis file in the `context/` folder. Both files must share the same base name and creation timestamp so they can be paired together. Do not rename files after creation; instead, record modifications with an `updated:` field in the frontmatter.
 - Automation: conversation/synthesis files must NOT be automatically generated or modified by Copilot or any automation without explicit maintainer approval and by opt-in. If automation is enabled by maintainers, it must be documented under the repository opt-in marker (for example `.github/automation-enabled`) with allowed scripts and owners; automation must ask for approval before running and creating repository files.
 - Automation: conversation/synthesis files must NOT be automatically generated or modified by Copilot or any automation without explicit maintainer approval and by opt-in. If automation is enabled by maintainers, please follow the procedure documented in `.github/instructions/context.instructions.md` and create the `.github/automation-enabled` opt-in marker with `enabled: true`, a list of `allowed-scripts` under `.github/scripts/`, and `owners` who can approve automation.
 - Purpose: create a precise, timestamped synthesis of the conversation that led to a commit and store it in `context/` alongside the code change. This provides clear traceability between code changes and the conversational decisions that motivated them.
 - Rule: Every commit should include one conversation transcript file and one synthesis file in the `context/` folder. Both files must share the same base name and creation date so they can be paired together. Do not rename files after creation; instead, record modifications with an `updated:` field in the frontmatter.
 - Consent: Copilot must not create these conversation or synthesis files automatically. Copilot must propose the file content preview and request explicit user approval before creating the conversation or synthesis files. If automation is desired, the user must explicitly run an approved script or action to generate these files.
 - Automation policy: Any script that generates conversation, synthesis, or TODO files must live under `.github/scripts/`, be documented in an instructions file, and be runnable only by explicit user action. Copilot may refer to these scripts and propose they run, but Copilot must ask the user for explicit approval and confirm the precise command and arguments before executing them.

- CI validation: optionally a repository-level GitHub Actions workflow may validate session notes or documentation for PRs that change README or docs. If present, this CI check should be validation-only and must not create files; it should fail the PR if a required session note, checklist, or explicit documentation of the change is not included. Requiring a `context/*-todo.md` file is a maintainer policy; if adopted, it must be documented and enforced consistently via the opt-in marker and CI.
-- Naming convention: use an ISO-like date (YYYYMMDD) and a short hyphenated summary for the filename: `YYYYMMDD-brief-summary-(conversation|synthesis).md` where `YYYYMMDD` is the creation date in UTC (e.g., `20251124`), and `brief-summary` is 1–6 words slugified (lowercase, hyphens only). Use date-only stamps (no hours/minutes).
-- Timestamp source: prefer calling the repository's Model Context Protocol (time MCP) to generate a canonical creation date for consistency across MCP actions. If the time MCP is unavailable, use the system UTC date as a fallback (`date -u +%Y%m%d`).
- Content & frontmatter: each file should include YAML frontmatter with at least these keys:
	- `created`: the creation date (YYYYMMDD, do not change on later edits)
	- `conversation_id`: the base filename (e.g., `20251124T164530Z-initial-setup`)
	- `summary`: short sentence (1–2 lines) describing the conversation or synthesis
	- `commit`: short commit SHA the conversation/synthesis relates to
	- `safe-to-push`: `false` by default unless the content is confirmed for remote sharing
	- `updated`: (optional) a list of UTC dates (YYYYMMDD) when the file was modified. Do not use this to change the filename or created date.

- Preservation rule: filenames must retain the creation date and slug. When the conversation or synthesis is edited, do not rename the file (this includes the Copilot chat history listing name for the conversation). Instead, add an `updated:` entry in the frontmatter and append a short note with the change in the file body.

- Example filename pair:
	- `context/20251124T164530Z-initial-setup-conversation.md`
	- `context/20251124T164530Z-initial-setup-synthesis.md`

- Example script snippet (shell) for generating the files (Pseudo/optional automation):

```bash
# preferred: use time MCP to generate canonical UTC timestamp; if not available fallback to date
timestamp=$(npx mcp_time_get_current_time --timezone UTC --format YYYYMMDD 2>/dev/null || date -u +%Y%m%d)
summary="initial-setup" # short summary used to form file slug; sanitize as needed
slug=$(echo "$summary" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\{2,\}/-/g' | sed 's/^\-\|\-$//g')
base="${timestamp}-${slug}"
convo="context/${base}-conversation.md"
synth="context/${base}-synthesis.md"

# conversation transcript
cat > "$convo" <<EOF
---
	created: $timestamp
conversation_id: $base
summary: "Short conversation description"
commit: $(git rev-parse --short HEAD || echo "<pending>")
safe-to-push: false
---
# Conversation transcript
...
EOF

# synthesis
cat > "$synth" <<EOF
---
	created: $timestamp
conversation_id: $base
summary: "Short synthesis summary"
commit: $(git rev-parse --short HEAD || echo "<pending>")
safe-to-push: false
---
# Synthesis
...
EOF

# stage for commit
git add "$convo" "$synth"
```

- Validation rules for humans and bots:
	- ensure `conversation_id` matches for both files
	- ensure `created` timestamp is identical in both files and not changed on later edits
	- include a one-line summary in the filename (slug) and frontmatter `summary`
	- remember that updates to content do not change filename or created timestamp; record changes under `updated` in frontmatter instead


## Workflow

### Starting New Work
```bash
# Update develop branch
git checkout develop
git pull origin develop

# Create feature branch
git checkout -b feature/your-feature-name
```

### Making Changes
```bash
# Stage changes
git add <files>

# Commit with descriptive message
git commit -m "feat(scope): description"

# Push to remote
git push origin feature/your-feature-name
```

### Merging Work

#### Feature → Develop
```bash
# Update your branch with latest develop
git checkout feature/your-feature-name
git pull origin develop
git rebase develop

# Merge to develop
git checkout develop
git merge --no-ff feature/your-feature-name
git push origin develop

# Delete feature branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

#### Develop → Main (Release)
```bash
# Ensure develop is ready
git checkout develop
git pull origin develop

# Merge to main
git checkout main
git merge --no-ff develop
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin main --tags
```

## Release Process

### Version Numbering (Semantic Versioning)
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps
1. Ensure all features are merged to `develop`
2. Update version numbers in relevant files
3. Update `README.md` and documentation
4. Merge `develop` to `main`
5. Create annotated tag: `git tag -a v1.0.0 -m "Release v1.0.0"`
6. Push tags: `git push origin --tags`
7. Create GitHub release with changelog
8. Merge `main` back to `develop` if any hotfixes were applied

### Hotfix Process
```bash
# Create hotfix branch from main
git checkout main
git checkout -b hotfix/critical-fix

# Make fix and commit
git add .
git commit -m "fix: critical security issue"

# Merge to both main and develop
git checkout main
git merge --no-ff hotfix/critical-fix
git tag -a v1.0.1 -m "Hotfix v1.0.1"
git push origin main --tags

git checkout develop
git merge --no-ff hotfix/critical-fix
git push origin develop

# Delete hotfix branch
git branch -d hotfix/critical-fix
```

## Push Policy

### Before Pushing
- ✅ Code runs without errors
- ✅ Tests pass (if applicable)
- ✅ Code is formatted properly
- ✅ Commit messages follow conventions
- ✅ No sensitive data (API keys, passwords, etc.)

### Force Push Policy
- ⚠️ **NEVER** force push to `main` or `develop`
- ⚠️ Only force push to feature branches if necessary
- ⚠️ Communicate with team before force pushing shared branches

## Pull Request Guidelines

### Creating PRs
- Use descriptive PR titles
- Fill out PR template (if available)
- Link related issues
- Add reviewers
- Mark as draft if work in progress

### PR Description Should Include
- What changed and why
- How to test the changes
- Screenshots/demos if UI changes
- Breaking changes (if any)

### Pull request template

Use this template when opening pull requests.

#### Description
- Brief description of the change

#### Type of change
- Bugfix
- New feature
- Documentation
- Other

#### Checklist
- [ ] I have read the CONTRIBUTING.md and signed off my commits (DCO)
- [ ] My change includes tests or documentation updates if applicable
- [ ] I added a clear description of the change

Signed-off-by: JFG Gouteron <punkyard@grrlz.net>

### Merging PRs
- Require at least one approval
- All CI checks must pass
- Resolve all conversations
- Use "Squash and merge" for feature branches
- Use "Merge commit" for develop → main

## Best Practices

1. **Pull before push** - Always pull latest changes before pushing
2. **Small commits** - Make small, focused commits
3. **Meaningful names** - Use descriptive branch and commit names
4. **Regular commits** - Commit early and often
5. **Clean history** - Rebase feature branches before merging
6. **Tag releases** - Always tag release commits
7. **Document changes** - Keep changelog updated
8. **Code review** - All code should be reviewed before merging to main

## Common Commands Quick Reference

```bash
# Check status
git status

# View commit history
git log --oneline --graph

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git checkout -- <file>

# Update branch with remote
git pull --rebase origin develop

# View differences
git diff

# Stash changes temporarily
git stash
git stash pop
```

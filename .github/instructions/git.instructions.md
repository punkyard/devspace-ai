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

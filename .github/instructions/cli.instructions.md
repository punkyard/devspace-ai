# 🔐 Copilot CLI allowlist / denylist guidance

Keep a curated `--allow-tool` pattern for Copilot CLI to reduce risk. Examples:

- **safe:** `shell(npm run test:*)`, `shell(git status)`, `shell(node -v)`
- **deny:** `shell(rm -rf *)`, `shell(curl https://...)` (unless explicitly approved)

## ✅ Recommended globs (canonical list, edit this file to change)

- `shell(npm run test:*)`
- `shell(git status)`
- `shell(node -v)`
- **deny:** `shell(rm -rf *)`
- **deny:** `shell(curl http*)`

## 🛡️ Safe command scaffolding (zsh)

When Copilot proposes commands, it will show them in a minimal zsh block for approval:

```zsh
node -v
npm -v
```

**Copilot will run after your explicit approval.** Always review the commands before confirming.

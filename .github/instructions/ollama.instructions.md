---
description: "install and use Ollama locally on macOS for an optional local LLM; keep it simple and offline-friendly"
---
# Ollama — local LLM (optional)

## prerequisites

- macOS (Intel or Apple Silicon)
- Homebrew recommended (but not required)

## install options (macOS)

- via Homebrew:
  - `brew install --cask ollama`

Copilot flow in this repo uses a script that supports a dry run first, then live run after approval.

## use the installer script (preferred here)

- dry run (no changes):
  - `zsh .github/scripts/ollama-install.sh --dry-run`
- live run (after approval):
  - `zsh .github/scripts/ollama-install.sh`

What the script does:
- installs Ollama (Homebrew cask if available; otherwise official script)
- verifies `ollama --version`
- pulls a small model (default: `tinyllama`), configurable via `MODEL=...`

Example to pull a different model:
- `MODEL="mistral" zsh .github/scripts/ollama-install.sh`

## choose the model in chat

- Copilot will ask if you want to use a local LLM
- small and fast default: `tinyllama` (good for basic tasks and privacy)
- if your Mac is from 2020 or newer and has enough RAM/CPU, consider `qwen2.5-coder:3b` for better coding quality
- famous hosted models (Claude, GPT) are more powerful but not local; they run via GitHub Copilot’s cloud and may use tokens

using in VS Code chat:
- to chat directly with a local model, install a VS Code extension that supports Ollama (e.g., “Continue” by Continue Dev)
- select the Ollama provider and choose the pulled model (e.g., `tinyllama` or `qwen2.5-coder:3b`)
- this is optional; Copilot itself can still use its hosted models while you keep Ollama for local/offline tests

## notes

- pulling models downloads hundreds of MB; ensure you have disk space and bandwidth
- no API keys are needed for Ollama
- you can list models with `ollama list` and remove with `ollama rm <model>`
 - you can run `ollama run <model>` to test locally in a terminal before using it in an editor

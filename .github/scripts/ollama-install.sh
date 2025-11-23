#!/usr/bin/env zsh
# Install Ollama on macOS and pull a small model (default: tinyllama)
# - idempotent where possible
# - supports --dry-run to print actions without changes
# - configurable MODEL env var (default: tinyllama)

set -euo pipefail
trap 'echo "[ollama-setup] error on line $LINENO; aborting" >&2' ERR

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=true
fi

run() {
  if $DRY_RUN; then
    echo "+ $@"
  else
    eval "$@"
  fi
}

log() { echo "[ollama-setup] $1"; }

MODEL=${MODEL:-tinyllama}

# 1) Install Ollama if missing
if ! command -v ollama >/dev/null 2>&1; then
  log "ollama not found; attempting install..."
  if command -v brew >/dev/null 2>&1; then
    log "installing via Homebrew cask"
    run "brew install --cask ollama"
  else
    log "installing via official script"
    run "curl -fsSL https://ollama.com/install.sh | sh"
  fi
else
  log "ollama already installed"
fi

# 2) Verify version
if $DRY_RUN; then
  echo "+ ollama --version"
else
  ollama --version || true
fi

# 3) Pull model
log "pulling model: $MODEL (this may take time and disk space)"
if $DRY_RUN; then
  echo "+ ollama pull $MODEL"
else
  ollama pull "$MODEL"
fi

log "done. you can run: ollama list"

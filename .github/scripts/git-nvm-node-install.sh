#!/usr/bin/env zsh
# Install Git, NVM (Node Version Manager) and Node.js 22 on macOS (zsh)
# - idempotent: skips steps when already installed
# - safe: exits on errors; does not export secrets
# - supports dry-run: pass --dry-run to only print actions

set -euo pipefail

trap 'echo "[node-setup] error on line $LINENO; aborting" >&2' ERR

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

log() { echo "[node-setup] $1"; }

info_git() {
  echo "[node-setup] git is used for version control and to connect your identity (name/email) to commits"
}

# 0) Ensure Git is installed; configure if user/email provided
info_git
if ! command -v git >/dev/null 2>&1; then
  log "git not found; attempting install via Homebrew..."
  if command -v brew >/dev/null 2>&1; then
    run "brew install git"
  else
    log "Homebrew not found. Please install Homebrew first (see README), then re-run this script."
  fi
else
  log "git already installed"
fi

# optional: configure git identity if environment variables are provided
if [[ -n "${GIT_USER_NAME:-}" && -n "${GIT_USER_EMAIL:-}" ]]; then
  if $DRY_RUN; then
    echo "+ git config --global user.name \"$GIT_USER_NAME\""
    echo "+ git config --global user.email \"$GIT_USER_EMAIL\""
  else
    git config --global user.name "$GIT_USER_NAME"
    git config --global user.email "$GIT_USER_EMAIL"
    log "configured git user.name and user.email"
  fi
else
  log "skipping git config (set GIT_USER_NAME and GIT_USER_EMAIL to configure)"
fi

# 1) Install NVM if missing
if ! command -v nvm >/dev/null 2>&1; then
  log "nvm not found; attempting install..."
  # First try Homebrew layout if brew exists
  if command -v brew >/dev/null 2>&1 && [[ -d "/opt/homebrew/opt/nvm" || -d "/usr/local/opt/nvm" ]]; then
    log "detected Homebrew nvm installation; sourcing it"
  else
    log "installing nvm via official script"
    run "curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash"
  fi
else
  log "nvm already installed"
fi

# 2) Source NVM for this shell session
export NVM_DIR="$HOME/.nvm"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  $DRY_RUN || . "$NVM_DIR/nvm.sh"
elif [ -s "/opt/homebrew/opt/nvm/nvm.sh" ]; then
  NVM_DIR="/opt/homebrew/opt/nvm"
  $DRY_RUN || . "/opt/homebrew/opt/nvm/nvm.sh"
elif [ -s "/usr/local/opt/nvm/nvm.sh" ]; then
  NVM_DIR="/usr/local/opt/nvm"
  $DRY_RUN || . "/usr/local/opt/nvm/nvm.sh"
else
  if $DRY_RUN; then
    log "would source nvm: $NVM_DIR/nvm.sh (or Homebrew paths)"
  else
    log "error: could not find nvm.sh after install; ensure network and retry"
    exit 1
  fi
fi

# 3) Install Node.js 22 and set as default
if $DRY_RUN; then
  log "would install and select Node.js 22"
  echo "+ nvm install 22"
  echo "+ nvm alias default 22"
  echo "+ nvm use 22"
else
  if ! nvm ls 22 >/dev/null 2>&1; then
    log "installing Node.js 22 (this may take a moment)..."
    run "nvm install 22"
  else
    log "Node.js 22 already installed"
  fi

  log "setting default Node.js to 22"
  run "nvm alias default 22"
  run "nvm use 22"
fi

# 4) Print versions
log "verifying versions..."
if $DRY_RUN; then
  echo "+ node -v"
  echo "+ npm -v"
else
  node -v || true
  npm -v || true
fi

log "done. open a new terminal or 'source ~/.zshrc' if nvm is not recognized in new shells."

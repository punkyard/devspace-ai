#!/usr/bin/env bash
set -euo pipefail

echo "Installing git hooks (git config core.hooksPath .githooks)"
git config core.hooksPath .githooks
echo "Installed. To revert: git config --unset core.hooksPath"

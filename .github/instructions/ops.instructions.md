---
applyTo: '**'
description: "Ops and admin instructions for Copilot Metrics and safe pushes"
---
# 🔧 Ops instructions (admin)

This file explains admin operations such as Copilot Metrics API usage and token scopes.

## ✅ First push checklist

Before pushing code to a remote repository, confirm:

**Branch naming:**

- feature/<short-name>, fix/<short-name>, chore/<short-name>

**Commit message style:**

- imperative mood, short subject (≤ 72 chars)
- lowercase bullet points in body
- reference issue id if relevant (e.g., "fixes #42")

**Push safety:**

- no secrets (API keys, tokens, passwords)
- no personal data
- session files only if they have `safe-to-push: true` in frontmatter

## 🔒 When to set safe-to-push: true

- default is `safe-to-push: false` for all session notes in `/context/`
- flip to `true` only when:
  - the file contains no credentials, no personal data
  - you intend to share or publish the session notes
- explicitly set this at the end of a session you want to push

## 📊 Copilot Metrics API

- **endpoint:** `GET /orgs/{org}/copilot/metrics`
- **required scopes:** `manage_billing:copilot`, `read:org`, or `read:enterprise` depending on token type
- **note:** the organization must enable Copilot metrics and meet minimum usage thresholds

Do NOT run metrics queries without an appropriate token and explicit permission.

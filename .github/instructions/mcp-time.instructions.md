---
applyTo: '**/*'
description: "Time MCP server install and usage notes; use for canonical timestamps"
---
# ⏰ Time MCP server — install and usage

The Time MCP server provides canonical UTC timestamps for consistent date/time operations across sessions and automation.

## 🎯 Purpose

- generate ISO 8601 timestamps for session notes, conversation files, and synthesis files
- convert times between timezones
- get current time in any timezone
- ensure consistent timestamping across Copilot actions and scripts

## 📦 Installation

The Time MCP server is installed via `uvx` (Python package runner) and defined in `.vscode/mcp.json`.

**Command:**
```bash
uvx mcp-server-time --local-timezone Europe/Paris
```

**No API key required** — the time server runs locally and does not need authentication.

## 🔧 Configuration in `.vscode/mcp.json`

```json
{
  "servers": {
    "time": {
      "command": "uvx",
      "args": ["mcp-server-time", "--local-timezone", "Europe/Paris"]
    }
  }
}
```

**Note:** Adjust `--local-timezone` to your preferred timezone (e.g., `America/New_York`, `Asia/Tokyo`).

## 🛠️ Available tools

### `mcp_time_get_current_time`
Get the current time in a specific timezone.

**Parameters:**
- `timezone` (string): IANA timezone name (e.g., `Europe/Paris`, `America/New_York`, `UTC`)

**Example:**
```javascript
// Get current time in Paris
mcp_time_get_current_time({ timezone: "Europe/Paris" })
// Returns: { timezone: "Europe/Paris", datetime: "2025-11-26T05:30:00+01:00", day_of_week: "Wednesday", is_dst: false }
```

### `mcp_time_convert_time`
Convert a time from one timezone to another.

**Parameters:**
- `source_timezone` (string): Source IANA timezone
- `time` (string): Time in 24-hour format (HH:MM)
- `target_timezone` (string): Target IANA timezone

**Example:**
```javascript
// Convert 14:30 Paris time to New York
mcp_time_convert_time({ 
  source_timezone: "Europe/Paris", 
  time: "14:30", 
  target_timezone: "America/New_York" 
})
```

## 📝 Usage in session notes

Use the Time MCP to generate canonical timestamps for conversation and synthesis files.

**Preferred workflow:**
1. Call `mcp_time_get_current_time({ timezone: "UTC" })` to get the current UTC date
2. Extract the date portion (YYYYMMDD) from the `datetime` field
3. Use this date as the creation timestamp in session file names and frontmatter

**Example:**
```bash
# Session file naming: context/YYYYMMDD-brief-summary-conversation.md
# Frontmatter: created: YYYYMMDD
```

**Fallback:** If the Time MCP is unavailable, use `date -u +%Y%m%d` as a fallback for UTC timestamps.

## 🔄 Auto-start with VS Code

VS Code automatically starts the Time MCP server when Copilot invokes any time-related tool (no manual start required).

**To verify the server is running:**
```bash
pgrep -f mcp-server-time
```

## 🌍 Common timezones

| Timezone | IANA ID |
|----------|---------|
| Paris | `Europe/Paris` |
| New York | `America/New_York` |
| London | `Europe/London` |
| Tokyo | `Asia/Tokyo` |
| UTC | `UTC` |
| Los Angeles | `America/Los_Angeles` |
| Sydney | `Australia/Sydney` |

## 📖 Best practices

- **Always use UTC for canonical timestamps** in session notes and automation scripts
- **Use local timezone for user-facing displays** (e.g., showing current time to the user)
- **Prefer the Time MCP over system `date` commands** for consistency across platforms and sessions
- **Include timezone information** when storing or displaying times to avoid ambiguity

## 🔗 References

- Official docs: [MCP Time Server on GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/time)
- VS Code MCP integration: `.vscode/mcp.json`
- Session file naming convention: `.github/copilot-instructions.md` section G

> print "⏰ time MCP" each time you read this file

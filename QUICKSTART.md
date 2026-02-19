# Quick Start Guide

## Testing Your AI Employee

### 1. Test the File System Watcher

Open a terminal and run:

```bash
# Activate virtual environment
.venv\Scripts\activate

# Start the watcher
python filesystem_watcher.py
```

Keep this terminal open. The watcher will monitor the Inbox folder.

### 2. Drop a Test File

In another terminal or file explorer:
1. Create a simple text file (e.g., `test.txt`)
2. Drop it into `AI_Employee_Vault/Inbox/`
3. Watch the watcher terminal - you should see a log message
4. Check `AI_Employee_Vault/Needs_Action/` - you'll find `FILE_test.txt` and `FILE_test.txt.md`

### 3. Process with Claude Code

Open a new terminal in the project directory:

```bash
# Process pending tasks
claude /process-needs-action
```

Claude will:
- Read files in Needs_Action/
- Determine appropriate actions
- Update Dashboard.md
- Move completed tasks to Done/

### 4. Check the Dashboard

Open `AI_Employee_Vault/Dashboard.md` in Obsidian or any text editor to see the updated status.

## Common Commands

```bash
# Update dashboard
claude /update-dashboard

# Create a task plan
claude /create-plan "Send monthly report to team"

# Process all pending tasks
claude /process-needs-action
```

## Troubleshooting

**Watcher not detecting files:**
- Ensure you're dropping files in the correct Inbox folder
- Check file permissions
- Look for error messages in the terminal

**Claude Code not finding skills:**
- Verify `.claude/skills/` directory exists
- Check that SKILL.md files are present
- Run `claude --help` to see available skills

**Files not moving to Done:**
- Check Company_Handbook.md for approval requirements
- Some actions may require manual approval in Pending_Approval/

## Next Steps

1. Customize `Company_Handbook.md` with your rules
2. Add more watchers (Gmail, WhatsApp) for Silver Tier
3. Set up MCP servers for external actions
4. Configure scheduling for automated tasks

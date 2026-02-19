# AI Employee - Bronze Tier

A local-first Personal AI Employee built with Claude Code and Obsidian for autonomous task management.

## Overview

This project implements the Bronze Tier of the Personal AI Employee Hackathon. It provides:
- Obsidian vault for knowledge management
- File system watcher for automatic task detection
- Claude Code integration via Agent Skills
- Human-in-the-loop approval workflow

## Prerequisites

- Python 3.13+
- UV package manager
- Claude Code CLI
- Obsidian (optional, for GUI)

## Setup Instructions

### 1. Install Dependencies

```bash
# Install Python dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings (optional)
```

### 3. Verify Vault Structure

The following folders exist in `AI_Employee_Vault/`:
- Inbox/ - Drop files here for processing
- Needs_Action/ - Pending tasks
- Done/ - Completed tasks
- Plans/ - Task plans
- Logs/ - Action logs
- Pending_Approval/ - Tasks awaiting approval
- Approved/ - Approved actions
- Rejected/ - Rejected actions

### 4. Start the File System Watcher

```bash
# Activate virtual environment (Windows)
.venv\Scripts\activate

# Run the watcher
python filesystem_watcher.py
```

The watcher will monitor the `Inbox/` folder for new files.

## Using Claude Code Skills

### Process Pending Tasks

```bash
claude /process-needs-action
```

This will:
1. Read all files in Needs_Action/
2. Determine appropriate actions
3. Update Dashboard
4. Move completed tasks to Done/

### Update Dashboard

```bash
claude /update-dashboard
```

Updates Dashboard.md with current stats and recent activity.

### Create Task Plan

```bash
claude /create-plan "Task description here"
```

Creates a structured plan for complex tasks.

## Workflow Example

1. **Drop a file** in `AI_Employee_Vault/Inbox/`
2. **Watcher detects** and creates metadata in `Needs_Action/`
3. **Run Claude**: `claude /process-needs-action`
4. **Claude processes** the task according to Company_Handbook.md
5. **Review Dashboard** to see updated status
6. **Approve if needed** by moving files from Pending_Approval/ to Approved/

## Project Structure

```
Personal-AI-Employee/
├── .claude/
│   └── skills/           # Claude Code Agent Skills
├── AI_Employee_Vault/    # Obsidian vault
│   ├── Dashboard.md      # Main dashboard
│   ├── Company_Handbook.md  # Rules and guidelines
│   ├── Inbox/            # Drop files here
│   ├── Needs_Action/     # Pending tasks
│   ├── Done/             # Completed tasks
│   └── ...
├── base_watcher.py       # Base watcher class
├── filesystem_watcher.py # File system monitoring
├── .env                  # Environment configuration
└── pyproject.toml        # Python dependencies
```

## Bronze Tier Checklist

- [x] Obsidian vault with Dashboard.md and Company_Handbook.md
- [x] One working Watcher script (file system monitoring)
- [x] Claude Code successfully reading from and writing to the vault
- [x] Basic folder structure: /Inbox, /Needs_Action, /Done
- [x] All AI functionality implemented as Agent Skills

## Security Notes

- Keep `.env` file secure (already in .gitignore)
- Review all actions in Pending_Approval/ before approving
- Check logs regularly in /Logs folder
- Never commit sensitive credentials

## Next Steps (Silver Tier)

- Add Gmail watcher
- Implement MCP servers for external actions
- Add scheduling via cron/Task Scheduler
- Enhance approval workflow

## Resources

- [Hackathon Document](./Personal%20AI%20Employee%20Hackathon%200_%20Building%20Autonomous%20FTEs%20in%202026.md)
- [Claude Code Documentation](https://agentfactory.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows)
- [Agent Skills Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

## License

MIT

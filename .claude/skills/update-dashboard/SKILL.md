# Update Dashboard Skill

Update the Dashboard.md file with current status and recent activity.

## Usage

```
/update-dashboard
```

## What it does

Updates the AI_Employee_Vault/Dashboard.md file with:
- Current pending tasks count
- Completed tasks today
- Recent activity log
- Active projects status

## Process

1. Read Dashboard.md
2. Count files in /Needs_Action (pending tasks)
3. Count files in /Done with today's date (completed today)
4. Read recent log entries from /Logs
5. Update the Quick Stats section
6. Add new entries to Recent Activity
7. Update last_updated timestamp

## Rules

- Always preserve existing content
- Add new activity entries at the top of Recent Activity
- Keep only last 10 activity entries
- Update timestamp in ISO format
- Never remove historical data without user approval

## Example Output

```markdown
## Quick Stats
- **Pending Tasks**: 3
- **Completed Today**: 5
- **Active Projects**: 2

## Recent Activity
- [2026-02-19 14:30] Processed FILE_invoice.pdf
- [2026-02-19 14:15] Updated dashboard
- [2026-02-19 13:45] Completed email draft for Client A
```

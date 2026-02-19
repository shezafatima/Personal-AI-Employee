# Process Needs Action Skill

Process files from the Needs_Action folder and take appropriate actions.

## Usage

```
/process-needs-action
```

## What it does

1. Scans the /Needs_Action folder for pending tasks
2. Reads each task file and determines the appropriate action
3. Creates a plan if needed for complex tasks
4. Updates the Dashboard with current status
5. Moves completed tasks to /Done folder

## Process

- Read all files in AI_Employee_Vault/Needs_Action/
- For each file:
  - Parse the metadata (type, priority, status)
  - Determine the required action based on Company_Handbook.md rules
  - If complex, create a plan in /Plans folder
  - If simple, execute the action
  - Update Dashboard.md with progress
  - Move completed files to /Done folder with timestamp

## Rules

- Always follow Company_Handbook.md guidelines
- Request approval for sensitive actions (create file in /Pending_Approval)
- Log all actions in /Logs folder
- Update Dashboard.md after processing
- Never delete files, only move them

## Example

When a file is dropped in /Inbox:
1. Watcher creates FILE_document.pdf.md in /Needs_Action
2. This skill reads the metadata
3. Determines action (e.g., "Review and summarize")
4. Creates summary
5. Updates Dashboard
6. Moves to /Done

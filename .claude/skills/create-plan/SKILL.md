# Create Task Plan Skill

Create a detailed plan for complex tasks.

## Usage

```
/create-plan [task-description]
```

## What it does

Creates a structured plan file in the /Plans folder for complex tasks that require multiple steps.

## Process

1. Analyze the task requirements
2. Break down into actionable steps
3. Identify dependencies and approval requirements
4. Create a plan file in AI_Employee_Vault/Plans/
5. Reference the plan in Dashboard.md

## Plan Template

```markdown
---
created: [ISO timestamp]
status: pending
priority: [urgent/high/normal/low]
requires_approval: [true/false]
---

## Objective
[Clear statement of what needs to be accomplished]

## Steps
- [ ] Step 1: [Description]
- [ ] Step 2: [Description]
- [ ] Step 3: [Description]

## Approval Required
[List any steps that need human approval]

## Dependencies
[List any prerequisites or dependencies]

## Success Criteria
[How to know when this is complete]
```

## Rules

- Use clear, actionable language
- Flag steps requiring approval
- Include estimated complexity (simple/moderate/complex)
- Reference Company_Handbook.md for approval thresholds
- Link related files from /Needs_Action

## Example

For a task "Send invoice to Client A":
1. Verify client details
2. Calculate amount from rates
3. Generate invoice PDF
4. Draft email (requires approval)
5. Send email after approval
6. Log transaction

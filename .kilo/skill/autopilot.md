# Autopilot Skill

Automatically execute multi-step tasks without user intervention.

## Usage

Load this skill when you want Kilo to autonomously complete complex tasks:
```
kilo skill load autopilot
```

## Behavior

When autopilot is enabled:
1. **Plan first** - Break down the task into clear steps
2. **Execute sequentially** - Complete each step without pausing for confirmation
3. **Verify results** - Run tests/lints after changes
4. **Report summary** - Provide a concise completion summary

## Configuration

Set autopilot behavior in `kilo.json`:
```json
{
  "skills": {
    "autopilot": {
      "enabled": true,
      "maxSteps": 20,
      "requireApproval": ["git push", "npm publish", "rm -rf"],
      "autoTest": true,
      "autoLint": true
    }
  }
}
```

## Example Workflow

```
User: "Add a new API endpoint for user profiles"
Autopilot:
1. Search existing API routes
2. Create new route handler
3. Add validation schema
4. Write unit tests
5. Run test suite
6. Run linter
7. Summarize changes
```
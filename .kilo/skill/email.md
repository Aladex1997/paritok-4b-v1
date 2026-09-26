# Email Skill

Send emails from Kilo tasks and workflows.

## Usage

```
kilo skill load email
```

## Configuration

Add to `kilo.json`:
```json
{
  "skills": {
    "email": {
      "provider": "smtp",
      "smtp": {
        "host": "smtp.gmail.com",
        "port": 587,
        "secure": true,
        "auth": {
          "user": "your-email@gmail.com",
          "pass": "${EMAIL_PASSWORD}"
        }
      },
      "defaults": {
        "from": "your-email@gmail.com",
        "replyTo": "your-email@gmail.com"
      }
    }
  }
}
```

Supported providers: `smtp`, `sendgrid`, `mailgun`, `postmark`, `ses`

## Commands

### Send Email
```
email send --to "recipient@example.com" --subject "Task Complete" --body "The task has finished."
```

### Send with Template
```
email send --to "team@company.com" --template "task-complete" --data '{"task": "deploy", "status": "success"}'
```

### Send Results
```
email send --to "dev@company.com" --subject "Build Report" --attach "build-report.json"
```

## Templates

Create templates in `.kilo/email/templates/`:
```
.kilo/email/
├── templates/
│   ├── task-complete.md
│   ├── build-failed.md
│   └── daily-summary.md
```

Template variables: `{{task}}`, `{{status}}`, `{{timestamp}}`, `{{url}}`, `{{data}}`

## Example Task Integration

```yaml
# In a Kilo command or workflow
onComplete:
  - email:
      to: "team@company.com"
      template: "task-complete"
      data:
        task: "{{taskName}}"
        duration: "{{duration}}"
```

## Environment Variables

Use `${VAR_NAME}` in config for secrets:
- `EMAIL_PASSWORD` - SMTP password
- `SENDGRID_API_KEY` - SendGrid key
- `MAILGUN_API_KEY` - Mailgun key
# Week 3 - Monday: How each automation tool names things

This week's goal is to build **one simple automation twice**: once in **n8n** and once in **Power Automate**. Today was a learning day: n8n for beginners, the n8n free course, and Power Automate for beginners.

## The big idea

Every automation tool works the same way. **Something happens** (the trigger), then **the tool does things** (the actions), one after another. Only the words change from tool to tool.

## Same idea, different words

| Idea | n8n | Power Automate | Zapier | Make | GitHub Actions (Week 1) |
| --- | --- | --- | --- | --- | --- |
| The whole automation | Workflow | Flow (cloud flow) | Zap | Scenario | Workflow (`.yml` file) |
| What starts it | Trigger node | Trigger | Trigger | Trigger module | `on:` event |
| Each thing it does | Node | Action | Action step | Module | Step |
| A link to another app | Credential + node | Connector + connection | App + connected account | Connection | Action from the Marketplace, or a secret |
| One time it runs | Execution | Run (run history) | Task / Zap run | Operation / execution | Workflow run |
| Data passed along | Items (JSON) | Dynamic content | Fields from earlier steps | Bundles | Outputs and `env` |

## Trigger types worth knowing

- **Event trigger:** starts when something happens, like a form being submitted or an email arriving. *Scenario B uses this.*
- **Schedule trigger:** starts at a set time, like every weekday at 4pm. *(This is how my interns' daily update reminder works.)*
- **Manual trigger:** starts when you click a button. Useful for testing.
- **Webhook:** starts when another system sends a web request to a URL.

## How each tool feels at first look

- **n8n:** you build on a canvas, connecting nodes left to right. After each run you can click any node and see exactly what data went in and out. It can be self-hosted for free or used on n8n Cloud.
- **Power Automate:** you build top to bottom in a list of steps. It connects easily to Microsoft 365 apps (Forms, Excel, Teams, Outlook, SharePoint) using your work sign-in. Appnable's internal automations run on it.
- **Zapier / Make:** both are hosted. Zapier is the simplest (a straight list of steps), and Make looks like n8n's canvas.

## How this links to Week 1

My Week 1 GitHub Actions pipeline was already a rule-based automation. **Event:** a blog draft is pushed. **Jobs and steps:** run the SEO checker, then wait for approval, then publish. **Condition:** stop if a check fails. Week 3 is the same pattern with a different trigger and different apps.

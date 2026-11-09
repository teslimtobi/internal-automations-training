# internal-automations-training
Deliverables and notes for the 8-week internal automations training program.

## Daily checkpoint log

| Week | Day | Checkpoint | Status | Deliverable |
| --- | --- | --- | --- | --- |
| 1 | Mon | 4 parts of every workflow (trigger, steps, decisions, output) | Done | [monday-process-mapping.md](week-1/monday-process-mapping.md) |
| 1 | Tue | Scenario A actors, tools and steps | Done (revised after 1:1 feedback) | [tuesday-scenario-a-breakdown.md](week-1/tuesday-scenario-a-breakdown.md) |
| 1 | Wed | Scenario A swimlane flowchart in Lucidchart | Done (revised after 1:1 feedback) | [wednesday-swimlane-mapping.md](week-1/wednesday-swimlane-mapping.md) |
| 1 | Thu | Gaps in red, SOP comparison, 3 questions for Ada/Kemi | Done | [thursday-gaps-and-questions.md](week-1/thursday-gaps-and-questions.md) |
| 1 | Fri | CI/CD flowchart + ownership comparison (Appnable blog draft pipeline in GitHub Actions) | Done | [friday-cicd-pipeline.md](week-1/friday-cicd-pipeline.md) · [checklist issue #1](https://github.com/teslimtobi/internal-automations-training/issues/1) · [pipeline runs](https://github.com/teslimtobi/internal-automations-training/actions) |
| 2 | Mon | Learn BPMN basics (swimlanes, gateways, events) and how to write process docs / SOPs | Done | [monday-bpmn-and-sop-notes.md](week-2/monday-bpmn-and-sop-notes.md) |
| 2 | Tue | Scenario A trigger, roles and steps in order (SOP structure) | Done | [scenario-a-as-is-document.md](week-2/scenario-a-as-is-document.md) |
| 2 | Wed | Decisions (BPMN gateways) and flagged assumptions | Done | [scenario-a-as-is-document.md](week-2/scenario-a-as-is-document.md) |
| 2 | Thu | Pain points with frequency and cost estimates | Done | [scenario-a-as-is-document.md](week-2/scenario-a-as-is-document.md) |
| 2 | Fri | Tested as a new hire, fixed guesses, checked against Asana guide (as-is document v1.0) | Done | [friday-new-hire-test.md](week-2/friday-new-hire-test.md) |
| 3 | Mon | How n8n, Power Automate, Zapier and Make name triggers and actions | Done | [monday-tool-notes.md](week-3/monday-tool-notes.md) |
| 3 | Tue | Scenario B flow mapped in 3 boxes (form, tracker row, alert) | Done | [flow-map.png](week-3/flow-map.png) |
| 3 | Wed | Scenario B built in n8n, one successful run | Done | [week-3 README](week-3/README.md) · [workflow JSON](week-3/n8n/scenario-b-lead-workflow.json) |
| 3 | Thu | Same flow in Power Automate | Guide done, test run pending | [power-automate-build-guide.md](week-3/power-automate-build-guide.md) |
| 3 | Fri | Make skimmed, 5-line tool comparison, self-check | Done | [friday-tool-comparison.md](week-3/friday-tool-comparison.md) |

## Revision note (Week 1 feedback)
In the first version I rated Contract Intake, Folder & Channel setup and Repo Provisioning as "Operational" because each had a named owner. That was wrong: having an owner does not make a step reliable. The 9-day delay in the scenario came from the folder never being created, which traces back to Ada having to *remember* to tell Kemi. The flowchart, slides and Tuesday breakdown now rate every step by risk and show this as the root cause.

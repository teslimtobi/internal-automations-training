# Week 4 - Monday: Conditionals, branching and error handling (notes)

This week's goal: make the Scenario B lead flow handle **more than the happy path**. It should branch on the input, skip spam and duplicates, and **tell someone when it fails**.

Resources: n8n error handling (video and docs), Zapier Paths conditional logic. I'm building in **Power Automate**, so for each idea I've noted the Power Automate equivalent.

## 1. The key ideas

| Idea | What it means | n8n | Zapier | Power Automate |
| --- | --- | --- | --- | --- |
| **Condition (if/else)** | Check something, then take one of two paths | IF node | Filter / Paths | **Condition** action (If yes / If no) |
| **Branch (paths)** | More than one route, depending on the input | Switch node | Paths | Condition, or **Switch** |
| **Filter** | Stop the run early if the input isn't wanted | IF node, then nothing | Filter step | Condition + **Terminate** |
| **Error handling** | What happens when a step fails | Error Workflow / "On error" setting | Zap error alerts | **Scope** ("try") + action that runs only **if the scope fails** ("Configure run after") |
| **Alert** | Tell a person something failed, with details | Send Email / Slack node in the error workflow | Email by Zapier | Teams message or Outlook email in the "catch" step |

**Try / catch in Power Automate:** put the main steps in a **Scope** (the "try"). Add a step after it that is set to run **only if the scope has failed or timed out** (the "catch"). That step sends the alert with a link to the failed run.

## 2. Three ways my Scenario B flow could fail today

| # | How it could fail | What would happen today (Week 3 flow) | Week 4 fix |
| --- | --- | --- | --- |
| 1 | **Empty or wrong-format field.** The budget is left blank, or contains text, and the flow tries to treat it as a number. | The comparison step errors, the run fails, and **nobody is told**. | Treat a blank budget as 0, and use the failure alert for anything else unexpected. |
| 2 | **A service is down or changed.** Excel can't be reached, or the tracker file or table is renamed or moved. | "Add a row" fails, the lead never reaches the tracker, and **nobody is told**. | Failure alert (catch step) with a link to the failed run. |
| 3 | **Bad input that isn't an error.** Spam submissions, or the same person submitting twice. | Spam is added to the tracker and alerts go out. A duplicate gets a second row and a second alert (the "two different replies" problem in the scenario). | Spam filter and duplicate check before the row is added. |

## 3. The Week 4 flow, in plain words

1. A lead submits the form → get the answers.
2. **Try:**
   1. **Spam?** If the message contains a link or obvious spam words → stop quietly.
   2. **Duplicate?** If the email is already in the tracker → stop quietly.
   3. Add the row to the tracker.
   4. **Big lead?** If the budget is over $10,000 **or** the message mentions "retainer" → alert the **founder**. **Otherwise** → alert the **general sales channel**.
3. **Catch** (only if something in "Try" failed): send a **failure alert** saying what failed, with a link to the run.

> **What I actually built (Thu):** instead of wrapping everything in a Scope, I set the Failure alert to run after *Big lead check* **has failed, is skipped or has timed out**. When any earlier step fails, every later step is skipped, so this catches failures anywhere in the flow with one setting.

For the test build, both "founder" and "sales" alerts go to my own Teams chat with the Flow bot, with the intended recipient written at the top. No real person is messaged.

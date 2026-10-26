# Week 1 - Thursday Checkpoint: Gaps, SOP Comparison and Questions (Scenario A)

## 1. Gaps marked in red on the flowchart

Lucidchart: https://lucid.app/lucidchart/4df7fc73-7688-4c3e-bbd2-0f843be51d44/edit?invitationId=inv_8e5d735a-b462-4216-9cd6-41f7c5959a0a

| # | Gap | Type | Where on the chart |
| --- | --- | --- | --- |
| 1 | Sales forwards the contract to Ada | Handoff that relies on memory | Sales lane, red border |
| 2 | Ada tells Kemi a client has signed | Handoff that relies on memory | Ada's lane, red border + "Does Ada remember?" decision |
| 3 | Kemi creates the SharePoint folder and Teams channel | Owned step nobody checks | Kemi's lane, red border |
| 4 | Welcome email + kickoff form sent by "whoever remembers" | No owner | Kemi's lane, dashed border |
| 5 | SharePoint tracker updated to "Onboarding" | No owner | Kemi's lane, red border |
| 6 | Someone checks the inbox and forwards the kickoff form | No owner, relies on memory | Kemi's lane, decision with red border |

**Where the 9-day delay came from:** gap 2 leads to gap 3. If Ada forgets to tell Kemi, the folder is never created and nothing after it can start. The flowchart shows this as the red "ROOT CAUSE" wait state under the "Does Ada remember to tell Kemi?" decision.

## 2. SOP check

**Search:** I searched Appnable's SharePoint, Teams and Outlook files for "client onboarding", "SOP", "kickoff" and "onboarding process" (26 October 2026).

**Finding:** there is **no documented client onboarding SOP**. That helps explain the scenario: with nothing written down, nobody owns the handoffs, so steps depend on memory.

**What I compared against instead:** Appnable's one well-documented internal process that I work with: the **Appnable Blog Writing process** (Marketing's *Appnable Blog Writing Guidelines* and pre-publish checklist, run through the Appnable Blog Writing workflow: keyword research → approval → writing → checklist → reviews → publish).

### Scenario A vs the Appnable Blog Writing SOP

| What a good process needs | Blog Writing SOP | Scenario A onboarding |
| --- | --- | --- |
| **Written down** | Yes: a guidelines PDF, a checklist and a set workflow | No: nothing documented; it lives in people's heads |
| **Clear trigger** | Topic request → keyword research starts | Contract arrives by email, sometimes to Sales, sometimes to Ada |
| **Fixed order of steps** | Research → approval → write → check → review → publish | Loose; the welcome email and tracker update happen "whenever" |
| **Owner for each step** | Author writes; Marketing reviews; an engineer/SME checks technical claims; web admin adds FAQs | Ada and Kemi own some steps; the welcome email, tracker and inbox check have no owner |
| **Approval gate before work continues** | Writing can't start until topics are approved | None: nothing stops the process when a step is missed |
| **Definition of "done"** | "If a draft fails one checklist item, it is not ready to publish" | None: no one confirms the folder, email or repo exist |
| **Check that each step happened** | 17-item pre-publish checklist + automated checker + two reviews | No checks at all |
| **Record of progress** | Each primary keyword logged in the content tracker | Client tracker meant to say "Onboarding", but nobody owns it |
| **What happens when something is missed** | It's caught at the checklist or review stage | Nothing: the client waits (9 days last month) |

### What Scenario A could borrow from the Blog Writing SOP

1. **A written checklist** for every new client: contract received → Kemi notified → folder and channel created → welcome email sent → tracker updated → form returned → repo created. Nothing is "done" until every box is ticked.
2. **A named owner for every step,** especially the three unowned ones (welcome email, tracker, inbox).
3. **A gate:** the welcome email can't go out until the folder exists, just as writing can't start until topics are approved.
4. **One tracker with an owner,** like the content tracker, so anyone can see where each client is.

### Where the Blog Writing SOP has gaps too

To be fair, it isn't perfect either. Owners are named by role ("Marketing", "SME") rather than by person; there are no deadlines between stages; and the FAQ page the checklist links to doesn't exist yet. Even a documented process needs named people and time limits.

## 3. Three questions I'd ask Ada and Kemi

1. **To Ada:** "When a signed contract arrives, how do you tell Kemi (email, Teams or in person), and what happens if you're off that day or the contract went to Sales first?"
2. **To Kemi:** "Is there any way for you to find out a new client has signed if Ada doesn't tell you? And once you've created the folder and channel, how does anyone know it's done?"
3. **To both:** "Whose inbox do completed kickoff forms land in, who is meant to send the welcome email and update the tracker, and has anyone ever been asked to own those steps?"

**Why these three:** question 1 targets the root cause of the 9-day delay, question 2 tests whether there's any backup when the handoff fails, and question 3 covers all three unowned steps at once.

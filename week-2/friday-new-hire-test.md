# Week 2 - Friday: Testing the As-Is Document as a New Hire

**Task:** leave the document for a few hours, then follow it step by step as if I were Kemi on her first day. Fix every spot where I had to guess, and check it against what Asana's guide says a good process document includes.

**Document tested:** [scenario-a-as-is-document.md](scenario-a-as-is-document.md) (version 0.3 → 1.0)

## 1. Walking through it as Kemi on her first day

| Where I got stuck | What I had to guess | Fix made in version 1.0 |
| --- | --- | --- |
| Step 4: "Ada tells Kemi" | How Ada tells me, and where I should look | Added assumption **A1** (no set method: email, Teams or in person) and the question to confirm it |
| Step 5: folder and channel | Whether I make the folder or the channel first | Added assumption **A3** and marked it as a **parallel** gateway (G3) |
| Step 6: welcome email | Whether it's my job to send it | Made it clear the step has **no owner** ("whoever remembers") and added **A4** |
| Step 7: kickoff form | What the form is and where the answers go | Added **A5** and **A6** (form link in the email; answers come back to an inbox) |
| Tracker update | When the status should change to "Onboarding" | Added **A8**, and showed the step as unowned in the steps table |
| Ada is off | What I do if nobody tells me | Added a **section 10: Exceptions**, which wasn't in version 0.3 |
| The words "gateway" and "as-is" | What they mean | Added a short explanation at the top and above the decisions table |
| End of the process | When I'm "done" | Added a clear **End** line under the steps and in Scope |

## 2. Checked against Asana's guide to process documentation

| What a good process document includes (Asana) | In my document? |
| --- | --- |
| Clear, simple language a newcomer can follow | ✅ Tested as a new hire; jargon explained |
| Goals, scope and boundaries | ✅ Sections 1–2 |
| Trigger | ✅ Section 3 |
| Inputs and outputs | ✅ Section 5 |
| Steps in order, each with one owner | ✅ Section 7. Unowned steps are shown as **unassigned**, because this is the as-is |
| Stakeholders and roles | ✅ Section 4 |
| A flowchart or visual | ✅ Section 12 (Lucidchart link) |
| Exceptions | ✅ Section 10 (added on Friday) |
| A named document owner | ⚠️ Not assigned. Flagged as assumption A10 |
| A review schedule | ✅ Header table |
| A central place to store it | ✅ My GitHub training repo for now |

## 3. Self-check before the 1:1

**Does the doc describe what happens today, not what should happen?**
Yes. Unowned steps are written as unowned ("whoever remembers", "nobody"), the decisions show that most of them depend on memory, and nothing has been fixed in the document. Improvements are kept out of it on purpose.

**Could I point to the single step I'd automate first, and say why?**
**Step 4: Ada telling Kemi (gateway G2).** It's the root cause of the 9-day delay, and when it fails everything after it stops. It's also easy to automate with tools Northwind already has. When a signed contract arrives in a shared Outlook inbox, a Power Automate flow could notify Kemi in Teams and create the SharePoint folder and Teams channel automatically, so nobody has to remember.

## 4. Talking points for the 10-minute walkthrough (no slides)

1. **What it is (1 min):** an as-is document for client onboarding. It describes what happens today, not what should.
2. **Trigger, roles and steps (3 min):** the signed contract arrives; 5 people plus 3 unowned jobs; 9 steps in order.
3. **Decisions (2 min):** six gateways, four of which depend on someone remembering.
4. **Assumptions (1 min):** ten things the story doesn't say, each with how to confirm it.
5. **Pain points (2 min):** the 9-day delay, the form stuck half the time, the unowned tracker, with frequency and cost.
6. **What I'd automate first (1 min):** the Ada → Kemi handoff, and why.

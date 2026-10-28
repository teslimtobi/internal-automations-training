# Week 2 - Monday: BPMN basics and how to write an SOP (notes)

This week's goal is to write an **"as-is" document** for Scenario A: how client onboarding at Northwind *actually* works today, clear enough that a new hire could follow it without asking anyone. Today is a learning day, so these are my notes from the readings, with Scenario A examples.

## 1. BPMN basics (only swimlanes, gateways and events)

BPMN (Business Process Model and Notation) is the standard way to draw a process. I already used most of these ideas in my Week 1 flowchart.

| BPMN part | What it means | Symbol | Scenario A example |
| --- | --- | --- | --- |
| **Pool** | One whole participant or organisation | Big box around the lanes | Northwind Studio |
| **Lane (swimlane)** | One person, role or team inside the pool | One row | Client, Sales, Ada (Accounts), Kemi (Ops), Dev Lead |
| **Start event** | What starts the process | Thin circle | Client signs the contract |
| **End event** | Where the process finishes | Thick (bold) circle | Project ready for Dev (GitHub repo created) |
| **Intermediate event** | Something that happens or is waited for in the middle | Double circle (clock = timer, envelope = message) | Waiting for the kickoff form to come back |
| **Task (activity)** | A piece of work someone does | Rounded rectangle | Kemi creates the SharePoint folder |
| **Gateway** | A decision point where the flow splits or joins | Diamond | "Does Ada remember to tell Kemi?" |
| **Sequence flow** | The order of steps | Solid arrow | Ada receives contract → Ada notifies Kemi |

**Gateway types (the ones worth knowing):**

- **Exclusive (XOR)**: only **one** path is taken. Example: the contract goes to Sales **or** straight to Ada.
- **Parallel (AND)**: **all** paths happen at the same time. Example: Kemi could create the folder **and** the Teams channel together.
- **Inclusive (OR)**: **one or more** paths can happen, depending on conditions.
- **Event-based**: the path depends on **what happens next**, such as a reply arriving or a time limit passing. Example: the kickoff form comes back, **or** a week passes with no reply.

**What I'd change in my Week 1 chart to match BPMN properly:** my green "pills" should be BPMN **start/end events** (circles), and the wait states ("form sits in inbox") are closer to **intermediate timer events**.

## 2. What process documentation is (Asana's guide)

Process documentation is a living document that sets out the **steps, roles and resources** needed to run a process from start to finish. It's the single source of truth, so knowledge isn't stuck in one person's head. That's exactly Scenario A's problem.

**Asana's steps for writing it, and what each means for Scenario A:**

1. **Scope the process**: what it's for and why it matters. *(Get new clients from signed contract to kickoff quickly.)*
2. **Define boundaries**: where it starts and ends. *(Starts: contract signed. Ends: GitHub repo ready for Dev.)*
3. **Inputs and outputs**: what goes in and what comes out. *(In: signed contract. Out: folder, Teams channel, completed kickoff form, repo, updated tracker.)*
4. **Identify the steps**: find the trigger, list the steps in order, and give **each step one owner**. *(This is where the 3 unowned steps show up.)*
5. **Connect with stakeholders**: who is responsible, with deliverables and timelines.
6. **Add a flowchart**: use swimlanes for a process with several people. *(My Week 1 chart.)*
7. **Note exceptions**: what happens off the normal path. *(Contract goes to Sales first; Ada is off sick.)*
8. **Test it**: follow it, fix what's unclear, then store it somewhere central. *(This is Friday's task.)*

**A good process document also has:** plain language a newcomer can follow, a named owner for the document, a review date, and a way to flag anything unclear.

## 3. How to write an SOP

An SOP (standard operating procedure) is a step-by-step guide to doing a task the same way every time.

**Steps to write one:**

1. Define the **purpose**: which process it covers.
2. Know the **audience**, and write so they understand it. *(A new hire at Northwind.)*
3. **Gather information** from the people who do the work. *(My 3 questions for Ada and Kemi.)*
4. **Choose a format**:
   - **Simple step-by-step**: short, simple tasks
   - **Hierarchical** (steps with sub-steps): longer or more detailed processes
   - **Flowchart**: processes with decisions and different paths
   - **Checklist**: steps you tick off
5. **Write it.**
6. **Review it**, and do a trial run with the people involved.
7. **Publish it** somewhere easy to find, and update it when the process changes.

**For Scenario A I'll use hierarchical steps plus my flowchart**, because there are five people, several decisions and wait states.

## 4. The outline I'll use for the as-is document (Tuesday onwards)

1. **Title, owner, date, version**
2. **Purpose**: why this process exists
3. **Scope and boundaries**: where it starts and ends, and what's not included
4. **Trigger**: the event that starts it
5. **Roles**: who does what (Client, Sales, Ada, Kemi, Dev Lead)
6. **Inputs and outputs**
7. **Steps in order**: who, what, which tool *(Tuesday)*
8. **Decisions**: what gets decided, by whom, based on what *(Wednesday)*
9. **Assumptions**: anything the story doesn't say, flagged clearly *(Wednesday)*
10. **Exceptions**: what happens off the normal path
11. **Pain points**: the 9-day delay, the form stuck in an inbox, the unowned tracker, with how often and what it costs *(Thursday)*
12. **Flowchart**: link to the Week 1 swimlane chart

## 5. From the video (SOP documentation tutorial)

- *(add 2 or 3 takeaways after watching)*

## 6. Things I'm unsure about

- **As-is vs to-be:** I have to describe what happens *today*, including the bad parts, and not fix it in the document. I need to be careful not to write the improved version by mistake.
- **Gateway type for "Does Ada remember?":** is it really a decision (gateway) or a missing step? It's not a choice anyone makes. It's just whether she remembers.
- **Wait states:** should "form sits in inbox" be drawn as an intermediate timer event or written up as a pain point? Probably both.
- **Owner of the document:** an SOP needs an owner, but onboarding has no clear owner. Should I note that as an assumption?

## Sources

- [Asana: Process documentation guide](https://asana.com/resources/process-documentation)
- [Process Street: BPMN tutorial](https://www.process.st/bpmn-tutorial/)
- [Mailchimp: How to write an SOP](https://mailchimp.com/resources/how-to-write-an-sop/)
- Trainee guide links: BPMN basics, Asana's guide to process documentation, How to write an SOP, SOP documentation tutorial (video)

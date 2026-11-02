# Northwind Studio: New Client Onboarding (As-Is Process Document)

| | |
| --- | --- |
| **Document** | As-is process for new client onboarding (Scenario A) |
| **Version** | 1.0 (tested and corrected on Friday, Week 2) |
| **Written by** | Teslim Tobi, Internal Automations Trainee |
| **Document owner** | Not assigned yet (see assumption A10) |
| **Last updated** | Week 2 |
| **Review** | After any change to the process, or every 3 months |
| **Flowchart** | [Scenario A swimlane flowchart (Lucidchart)](https://lucid.app/lucidchart/4df7fc73-7688-4c3e-bbd2-0f843be51d44/edit?invitationId=inv_8e5d735a-b462-4216-9cd6-41f7c5959a0a) |

> **This is an "as-is" document.** It describes what *actually* happens today, including the parts that go wrong. It does not describe how the process *should* work. Anything the original story doesn't say is written as an **assumption** and flagged like this: **(A1)**.

**Source:** the Scenario A story in the Internal Automations Training guide:

> "When a client signs, Ada in accounts gets the signed contract by email, usually in Outlook, sometimes forwarded from sales. She's supposed to tell Kemi in ops, who creates a SharePoint folder and a Teams channel for the project. Then someone, honestly whoever remembers, sends the welcome email with the kickoff form. The dev lead sets up a GitHub repo once the kickoff form comes back, but half the time the form sits in someone's inbox. The client tracker on SharePoint is meant to be updated to 'Onboarding' but nobody owns that. Last month a client waited 9 days for their kickoff because the folder was never made."

---

## 1. Purpose

This process gets a new client from **signed contract** to **ready to start work**: a project folder, a Teams channel, a kickoff form returned by the client, and a GitHub repo for the developers.

## 2. Scope and boundaries

- **Starts when:** a client signs the contract.
- **Ends when:** the Dev Lead has set up the project's GitHub repo.
- **Not included:** selling to the client and agreeing the contract (before), and the kickoff meeting and project work itself (after).

## 3. Trigger

**A signed contract arrives by email in Outlook.** It usually goes straight to Ada in Accounts, and sometimes goes to Sales first, who forward it to Ada.

## 4. Roles

| Role | Person | What they do in this process |
| --- | --- | --- |
| Client | The new client | Signs the contract; fills in and returns the kickoff form |
| Sales | Sales team | Sometimes receives the signed contract and forwards it to Ada |
| Accounts | **Ada** | Receives the signed contract; is *supposed* to tell Kemi |
| Operations | **Kemi** | Creates the SharePoint project folder and the Teams channel |
| Development | **Dev Lead** | Sets up the GitHub repo once the kickoff form comes back |
| *Unassigned* | "Whoever remembers" | Sends the welcome email with the kickoff form |
| *Unassigned* | Nobody | Updates the client tracker to "Onboarding" |
| *Unassigned* | "Someone" | Notices the returned kickoff form and passes it on (A6) |

## 5. Inputs and outputs

| Inputs (what's needed) | Outputs (what's produced) |
| --- | --- |
| Signed contract (email attachment) | SharePoint project folder |
| Client contact details (from the contract email) (A2) | Teams project channel |
| Welcome email and kickoff form link (A5) | Welcome email sent to the client |
| Completed kickoff form from the client | GitHub repo set up by the Dev Lead |
| | Client tracker set to "Onboarding" (often missed) |

## 6. Tools

| Tool | Used for |
| --- | --- |
| Microsoft Outlook | Receiving the contract, forwarding it, the welcome email and the returned form |
| Microsoft SharePoint | The project folder, and the client tracker |
| Microsoft Teams | The project channel |
| Kickoff form | Collects project details from the client (A5) |
| GitHub | The project's code repository |

## 7. Steps in order (what happens today)

Each step shows **who** does it, **what** they do, **which tool**, and **what starts it**.

| # | Who | What happens | Tool | What starts it |
| --- | --- | --- | --- | --- |
| 1 | Client | Signs the contract and emails it back | Outlook | Contract agreed |
| 2 | Sales *(sometimes)* | If the contract came to Sales, they forward it to Ada | Outlook | Contract lands in a Sales inbox |
| 3 | Ada | Receives the signed contract | Outlook | Email from the client or Sales |
| 4 | Ada | Tells Kemi that a new client has signed (A1) | Not fixed (A1) | **Nothing.** Ada has to remember |
| 5 | Kemi | Creates the SharePoint project folder and the Teams channel (A3) | SharePoint, Teams | Ada telling her. If she isn't told, it doesn't happen |
| 6 | "Whoever remembers" | Sends the welcome email with the kickoff form to the client (A4) | Outlook | **Nothing.** Someone has to remember |
| 7 | Client | Fills in and returns the kickoff form (A5) | Kickoff form / email | Welcome email |
| 8 | "Someone" | Notices the returned form and passes it to the Dev Lead (A6) | Outlook | **Nothing.** Someone has to check the inbox |
| 9 | Dev Lead | Sets up the project's GitHub repo | GitHub | Receiving the kickoff form |
| – | Nobody | *Meant to* update the client tracker to "Onboarding" (A8) | SharePoint | **Nothing.** Nobody owns it |

**End:** the GitHub repo exists and the project is ready to start.

## 8. Decisions (BPMN gateways)

A **gateway** is a point where the flow splits depending on an answer. For each one: what gets decided, by whom, and based on what.

| # | Decision | Who decides | Based on what | Gateway type | Paths |
| --- | --- | --- | --- | --- | --- |
| G1 | Where does the signed contract arrive? | The client (by who they email) | Which address the client uses | **Exclusive** (one path only) | → Ada directly, or → Sales, who forward it |
| G2 | Is Kemi told about the new client? | Nobody decides. It depends on Ada remembering | Ada's memory; no reminder or checklist | **Exclusive** | Yes → Kemi creates folder and channel. No → **nothing happens; the client waits** (root cause of the 9-day delay) |
| G3 | Folder and channel created | Kemi | Being told by Ada | **Parallel** (both happen) (A3) | → SharePoint folder **and** Teams channel |
| G4 | Does anyone send the welcome email? | Nobody decides. "Whoever remembers" | Someone's memory | **Exclusive** | Yes → client receives the form. No → client hears nothing |
| G5 | Is the returned form noticed? | Nobody decides. Whoever checks the inbox | Whether someone happens to check | **Event-based** (whichever happens first) | Noticed → passed to Dev Lead. Not noticed → form sits in the inbox (about half the time) |
| G6 | Is the tracker updated? | Nobody owns it | Nothing | **Exclusive** | Usually no → tracker shows the wrong status |

**What this shows:** four of the six decisions (G2, G4, G5, G6) aren't really decisions at all. They depend on someone remembering or happening to check. That's why the process breaks.

## 9. Assumptions (things the story doesn't say)

| # | Assumption | Why I assumed it | How to confirm |
| --- | --- | --- | --- |
| A1 | Ada tells Kemi informally (email, Teams message or in person). There's no set method | The story says "she's supposed to tell Kemi" but not how | Ask Ada (question 1) |
| A2 | Client contact details come from the contract email | They're needed for the welcome email; no other source is mentioned | Ask Ada |
| A3 | Kemi creates the folder and the channel at the same time, in either order | The story lists them together | Ask Kemi |
| A4 | The welcome email is usually sent by Ada or Kemi, from their own Outlook | "Whoever remembers" suggests one of the people already involved | Ask both (question 3) |
| A5 | The kickoff form is a link in the welcome email, and the client's answers come back to an inbox | The story says the form "sits in someone's inbox" | Ask both |
| A6 | The returned form lands in the inbox of whoever sent the welcome email, not the Dev Lead's | The Dev Lead only acts "once the form comes back", and it gets stuck in "someone's" inbox | Ask the Dev Lead |
| A7 | The kickoff can't happen until the folder exists | The story says a client waited 9 days "because the folder was never made" | Ask Kemi |
| A8 | The tracker should be set to "Onboarding" once the contract is signed | "Onboarding" suggests the stage right after signing | Ask whoever reads the tracker |
| A9 | Northwind signs about **4 new clients a month** | Not stated; used only for the cost estimates in section 11 | Check the client tracker |
| A10 | Nobody owns this process as a whole | No owner is mentioned for the overall process | Ask the agency lead |

## 10. Exceptions (when things go off the normal path)

| Exception | What happens today |
| --- | --- |
| Contract goes to Sales instead of Ada | Sales has to forward it. If they don't, Ada never sees it and nothing starts |
| Ada is off sick or on leave | Nobody else knows to tell Kemi (A1). The process stops until Ada is back |
| Kemi is never told | No folder or channel is made, the kickoff can't happen (A7), and the client waits. This caused the 9-day delay |
| Nobody sends the welcome email | The client never gets the kickoff form, so the Dev Lead never gets it either |
| Kickoff form sits in an inbox | The Dev Lead can't set up the repo until someone notices (about half the time) |

## 11. Pain points

Frequencies come from the story where it gives them. Everything else is an **estimate**, based on assumption **A9** (about 4 new clients a month).

| # | Pain point | How often | What it costs |
| --- | --- | --- | --- |
| P1 | **Folder never made because Kemi wasn't told** (G2) | Happened at least once last month (stated). Estimate: about 1 in 4 clients | **9 days** of client waiting before kickoff (stated). A poor first impression; project start pushed back about 2 weeks; staff time chasing it, est. 1–2 hours |
| P2 | **Kickoff form sits in an inbox** (G5) | **About half the time** (stated). Estimate: about 2 clients a month | Repo setup delayed, est. 1–3 days each; the Dev Lead blocked; est. 2–6 days lost a month in total |
| P3 | **Nobody owns the client tracker** (G6) | Every client (no owner, so it's never reliable) | Nobody can see where a client is without asking around. Est. 15–30 minutes of chasing per client, and problems like P1 aren't spotted early |
| P4 | **Welcome email depends on whoever remembers** (G4) | Not stated. Estimate: occasionally missed | The client hears nothing after signing, and everything after it waits |
| P5 | **Two ways in for the contract** (G1) | "Sometimes" (stated) | An extra handoff (Sales → Ada) that can be missed, adding delay before anything starts |

**Biggest pain point:** P1. One missed message (Ada → Kemi) stops everything, and nobody notices until the client chases.

## 12. Flowchart

The full swimlane flowchart, with these gaps marked in red, is here: [Scenario A swimlane flowchart (Lucidchart)](https://lucid.app/lucidchart/4df7fc73-7688-4c3e-bbd2-0f843be51d44/edit?invitationId=inv_8e5d735a-b462-4216-9cd6-41f7c5959a0a).

## 13. Version history

| Version | Day | Change |
| --- | --- | --- |
| 0.1 | Tuesday | Purpose, scope, trigger, roles, inputs and outputs, tools, steps in order |
| 0.2 | Wednesday | Decisions (BPMN gateways), assumptions A1–A10, exceptions |
| 0.3 | Thursday | Pain points P1–P5 with frequency and cost estimates |
| 1.0 | Friday | Tested as if I were Kemi on her first day; fixed every spot where I had to guess (see the Friday test file) |

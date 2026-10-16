# Week 1 - Wednesday Checkpoint: Scenario A Swimlane Flowchart

## Diagram Link
- **Lucidchart Flowchart**: [View Scenario A As-Is Swimlane Diagram](https://lucid.app/lucidchart/4df7fc73-7688-4c3e-bbd2-0f843be51d44/edit?invitationId=inv_8e5d735a-b462-4216-9cd6-41f7c5959a0a)

## Workflow Architecture Summary
- **Swimlanes (Actors)**:
  1. Client
  2. Sales
  3. Ada (Accounts)
  4. Kemi (Ops)
  5. Dev Lead

- **Decision Points (Gateways)**:
  1. *Contract Delivery Route*: Client sends directly to Ada vs. forwarded through Sales.
  2. *Kickoff Trigger*: Does someone remember to send the welcome email and form? (Unassigned).
  3. *Form Handoff*: Does someone notice the returned form in the inbox and forward it to Dev?

- **Wait States & Bottlenecks (Marked in Orange/Red)**:
  1. *Ops Notification Delay*: Waiting on manual email handoff between Ada and Kemi.
  2. *Welcome Email Bottleneck*: Process stalls until "whoever remembers" sends the form (root cause of the 9-day delay).
  3. *Inbox Stagnation*: Completed kickoff forms sitting unread in general inboxes, delaying GitHub repo setup.

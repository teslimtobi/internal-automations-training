# Week 1 - Wednesday Checkpoint: Scenario A Swimlane Flowchart

**Lucidchart (view link):** https://lucid.app/lucidchart/4df7fc73-7688-4c3e-bbd2-0f843be51d44/edit?invitationId=inv_8e5d735a-b462-4216-9cd6-41f7c5959a0a

## Swimlanes (one per person)
Client · Sales · Ada (Accounts) · Kemi (Ops) · Dev Lead

## Key to shapes
| Shape | Meaning |
| --- | --- |
| Green pill | Start / end |
| Blue box | Normal step |
| Yellow diamond | Decision point |
| Red box | Wait state (work is stuck) |
| Red border | Gap: step relies on memory and nobody checks it happened |
| Dashed border | Step has no owner |

## Flow (trigger → steps → decisions → output)
1. **Trigger:** Client signs contract.
2. **Decision 1:** Who does the client email the contract to? → Sales (who forward it) or directly to Ada.
3. Ada receives the signed contract in Outlook.
4. **Decision 2 (new):** Does Ada remember to tell Kemi?
   - **No → Wait state (root cause):** Kemi is never told, so the SharePoint folder and Teams channel are never created. This is what caused the 9-day delay.
   - **Yes →** Ada notifies Kemi (red border: done from memory, no system).
5. Kemi creates the SharePoint folder and Teams channel (red border: only happens if she is told; nobody checks).
6. **Decision 3:** Does someone remember to send the welcome email?
   - **No → Wait state:** client gets no welcome email or kickoff form.
   - **Yes →** "Whoever remembers" sends the welcome email + kickoff form (dashed: no owner).
7. Update SharePoint tracker to "Onboarding" (red border: unowned gap).
8. Client completes and submits the kickoff form.
9. **Wait state:** form sits in an inbox that is unmonitored half the time.
10. **Decision 4:** Does someone check the inbox and forward the form to the Dev Lead?
    - **No → Wait state:** form sits idle, project delayed.
    - **Yes →** Dev Lead receives the form.
11. Dev Lead creates and configures the GitHub repository.
12. **Output:** Project onboarding complete / ready for dev.

## Totals
- 4 decision points
- 4 wait states
- 4 gap steps (red/dashed border): Ada → Kemi notification, folder & channel setup, welcome email, tracker update

## What changed after 1:1 feedback
- Removed the idea that owned steps are "operational". Every handoff in this process depends on someone remembering.
- Added Decision 2 and its wait state so the 9-day delay is traced to its real cause: the folder never being created.
- Moved the "9 days" label from the welcome-email branch to the folder branch.

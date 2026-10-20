# Week 1 - Tuesday Checkpoint: As-Is Workflow Breakdown (Scenario A)

## 1. Actors & Roles
- **Client**: Signs the contract and submits the project kickoff form.
- **Sales**: Forwards the signed contract to Accounts when received.
- **Ada (Accounts)**: Receives the signed contract via Outlook and is *supposed* to notify Ops (no system, relies on memory).
- **Kemi (Ops)**: Sets up the SharePoint project folder and Teams channel, but only once Ada tells her.
- **Unassigned / "Whoever remembers"**: Responsible for emailing the kickoff form to the client.
- **Dev Lead**: Configures the GitHub repository once the kickoff form arrives.
- **Tracker Owner (Unassigned)**: Supposed to update the SharePoint tracker status to "Onboarding".

## 2. Tools & Platforms
- **Microsoft Outlook**: Email intake for contracts, internal forwards, and client kickoff correspondence.
- **Microsoft SharePoint (Folders)**: Project file and asset storage.
- **Microsoft SharePoint (Tracker)**: Status tracking spreadsheet/list for client progression.
- **Microsoft Teams**: Communication channels for internal project collaboration.
- **Kickoff Form**: External intake form sent to the client.
- **GitHub**: Project code repository setup.

## 3. As-Is Sequential Workflow Steps
1. **Trigger**: Client signs the contract.
2. **Contract Intake**: Ada receives the signed contract in Outlook (either directly or forwarded from Sales).
3. **Handoff to Ops (memory-based)**: Ada is supposed to notify Kemi in Operations. Nothing reminds her or checks that she did.
4. **Workspace Creation**: Kemi creates a project folder in SharePoint and a project channel in Teams, only if she was told.
5. **Tracker Update (Unowned)**: The SharePoint client tracker is supposed to be updated to "Onboarding".
6. **Welcome Email Sent (Unowned)**: "Whoever remembers" sends the welcome email containing the kickoff form link.
7. **Form Completion**: Client completes and submits the kickoff form.
8. **Form Handoff (Gap)**: The kickoff form response lands in an inbox and waits for someone to notice and alert the Dev Lead.
9. **Output**: The Dev Lead provisions the project's GitHub repository.

## 4. Key Bottlenecks & Gaps Identified

| Step | Owner | Risk | Why |
| --- | --- | --- | --- |
| 2. Contract Intake | Ada | Medium | No single inbox: the contract can go to Sales or Ada |
| 3. Handoff to Ops | Ada | High | Relies on Ada remembering to tell Kemi |
| 4. Workspace Creation | Kemi | Critical | Root cause of the 9-day delay: the folder was never made |
| 5. Tracker Update | Nobody | High | Unowned, so the tracker goes stale |
| 6. Welcome Email | Nobody | High | Unowned, depends on "whoever remembers" |
| 8. Form Handoff | Nobody | High | Inbox unmonitored about half the time |
| 9. Repo Provisioning | Dev Lead | Medium | Blocked while the form sits in an inbox |

- **Correction:** an earlier version blamed the 9-day delay on steps 5 and 6 and rated owned steps as "Operational". The scenario says the delay happened "because the folder was never made", which is step 4, and step 4 only happens if step 3 (Ada remembering) happens. **Having a named owner does not make a step reliable** when nothing triggers or checks it.
- **Unmonitored Inboxes**: Step 8 relies on manual inbox checks, leaving kickoff data stranded and delaying repo creation.

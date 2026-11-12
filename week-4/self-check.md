# Week 4 - Self-check answers

## What happens if the input is empty? Twice as large? In a different format?

- **Empty:**
  - Name, Email and Message are required on the form, so they can't be blank.
  - A blank **Budget** is treated as 0 and goes to sales (tested with Jo Small).
  - A blank or odd **Message** is fine: `string()` and `toLower()` handle it.
  - If a required value were somehow missing and a step failed, the failure alert would fire.
- **Twice as large:**
  - **A bigger budget** (e.g. $30,000) just takes the founder path.
  - **A message twice as long** is fine: Teams and Excel accept long text.
  - **Twice as many leads** is fine too: each submission is its own run. The duplicate check reads the whole tracker, so a very large tracker would make that step slower. Filtering by email (not reading every row) keeps it fast.
- **Different format:**
  - **A budget typed as "$12,000" or "12k"** is blocked by the form's Number restriction. If it got through, `float()` would fail and the failure alert would fire.
  - **An email with different capitals** (`Riley.Big@…`) would slip past the duplicate check. That's a known gap, noted in the break log.

## Who finds out when it fails, and how quickly?

- **Who:** the flow owner (me, in the test build) gets a **Teams message from the Flow bot** headed "FAILURE ALERT". It shows the status of each main step and has a link to the failed run. In a real build the alert would go to the automation owner or a shared ops channel, not one person.
- **How quickly:** within **seconds** of the failure. In the break test the whole run, including the alert, took about 4 seconds. The run itself starts when the form trigger checks for new responses, usually within a minute of submission.
- **Before Week 4:** nobody found out. A failed run just sat in the run history until someone happened to look.

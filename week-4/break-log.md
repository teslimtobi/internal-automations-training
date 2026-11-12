# Week 4 - Friday: Break log

I broke the flow three ways on purpose, then checked that each one was caught. All tests used test leads only (`@example.test`).

| # | What I broke | How I broke it | What happened | Caught? | Fix / what I learned |
| --- | --- | --- | --- | --- | --- |
| 1 | **A step that talks to another service fails** (like a renamed column or table in the tracker) | Changed the tracker lookup's filter from `Email eq '…'` to `Emial eq '…'`, saved, and submitted a test lead (*Break Test*) | *Find same email in tracker* failed with **BadRequest**. The next steps (Duplicate check, Add a row, Big lead check) were **skipped**. The **Failure alert ran** and posted to Teams with each step's status and a link to the run. | ✅ Yes, by the failure alert | Changed the filter back to `Email`, saved, and confirmed the flow runs normally. **Lesson:** "Run after → is skipped" is what makes the alert catch failures *anywhere* earlier in the flow, not just in the step right before it. |
| 2 | **Empty input** | Submitted a lead (*Jo Small*) with the Budget left blank | The budget was treated as **0**. The lead went down the **sales** path and the run succeeded. | ✅ Yes, handled in the branch | The `if(empty(budget),'0',budget)` guard stops a blank budget from crashing the `> 10000` comparison. Without it, `float('')` would fail the run. |
| 3 | **The same person submits twice** | Submitted *Riley Big* (`riley.big@example.test`) a second time | *Find same email in tracker* found 1 row. *Duplicate check* was **True**, so the flow stopped (Succeeded) in 0.8 s. No second row, no second alert. | ✅ Yes, by the duplicate check | Working as designed. I also used `trim()` on the email so a space before or after the address doesn't make a duplicate look new. |

**Extra check: spam.** A message with "SEO services" and an `http://` link stopped at *Spam check* in 0.4 s, before anything was added to the tracker.

## Things I'd improve next

- **Run status:** add *Terminate (Failed)* after the Failure alert, so failed runs show red in the run history and not "Succeeded".
- **Upper or lower case in emails:** the duplicate filter compares exact text. `Riley.Big@…` and `riley.big@…` would count as two leads. Fix: save emails in lower case in the tracker, and compare in lower case.
- **Spam words:** the word list is short and simple. It could block a real lead who pastes their website link. A real build should flag those leads for review instead of dropping them.

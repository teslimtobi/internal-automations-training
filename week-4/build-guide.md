# Week 4 - Tue to Thu: Building the branch, filters and failure alert (step-by-step)

Starting point: the Week 3 flow (Form → Get response details → Add a row → Teams alert). Open it in **make.powerautomate.com → My flows → Edit**. Rename it to `Week 4 - Scenario B lead routing with error handling`.

> **Tip:** click **Save** after every part. The designer sometimes loses unsaved work if the page reloads.

**How to enter an expression:** click in a box → click the **fx** icon → type the expression → **Add**.

**Field IDs:** `outputs('Get_response_details')?['body/<id>']` is how an expression reads a form answer. You can find each ID in the *Code view* tab of the *Add a row* step.

---

## Tuesday: the big-lead branch (if/else)

1. Click **+** under *Add a row into a table* → **Add an action** → **Condition**. Rename it `Big lead check`.
2. Left box (fx):
   ```
   or(greater(float(if(empty(<Budget>),'0',<Budget>)),10000),contains(toLower(string(<Message>)),'retainer'))
   ```
   Operator: **is equal to**. Right box: `true`.
   - `if(empty(...),'0',...)` turns a blank budget into 0, so it can't crash the comparison.
   - `toLower` makes "Retainer" and "RETAINER" match too.
3. **True** branch → **Post message in a chat or channel** (Teams). Post as **Flow bot**, Post in **Chat with Flow bot**, Recipient: your own email. Rename it `Alert founder (big lead)`. Message (fx):
   `concat('FOUNDER ALERT (test) - BIG LEAD: ', <Name>, ' (', <Company>, ') | Email: ', <Email>, ' | Budget: $', <Budget>, ' | Message: ', <Message>, ' | Please reply within 24 hours.')`
4. **False** branch → the same action, renamed `Alert sales channel (normal lead)`, with a message starting `SALES CHANNEL ALERT (test) - New lead: `.

## Wednesday: spam filter and duplicate check

**Spam filter** (goes *before* the row is added):

1. Click **+** between *Get response details* and *Add a row* → **Condition** → rename `Spam check`.
2. Left (fx):
   ```
   or(contains(toLower(string(<Message>)),'http'),contains(toLower(string(<Message>)),'www.'),contains(toLower(string(<Message>)),'crypto'),contains(toLower(string(<Message>)),'seo services'),contains(toLower(string(<Message>)),'casino'))
   ```
   is equal to `true`.
3. **True** branch → **Terminate** → Status **Succeeded** → rename `Stop - spam`.
   *Why Succeeded?* Spam isn't an error. We want the run to end quietly, not to set off the failure alert.

**Duplicate check:**

4. **+** under *Spam check* → Excel Online (Business) **List rows present in a table**. Use the same file and the `Leads` table. Rename it `Find same email in tracker`.
5. **Advanced parameters → Filter Query**: type `Email eq '`, insert the fx expression `trim(string(<Email>))`, then type `'`.
6. **+** → **Condition** → rename `Duplicate check`. Left (fx): `greater(length(outputs('Find_same_email_in_tracker')?['body/value']),0)` is equal to `true`.
7. **True** branch → **Terminate**, Status **Succeeded**, rename `Stop - duplicate`.

## Thursday: the failure alert (try/catch)

1. Take the last Teams action (after *Big lead check*) and rename it `Failure alert`.
2. Message (fx):
   ```
   concat('FAILURE ALERT (test): the Scenario B lead flow failed. Get response details: ', actions('Get_response_details')?['status'], ' | Add row to tracker: ', actions('Add_a_row_into_a_table')?['status'], ' | Big lead check: ', actions('Big_lead_check')?['status'], ' | Open the failed run: https://make.powerautomate.com/environments/', workflow()?['tags']?['environmentName'], '/flows/', workflow()?['name'], '/runs/', workflow()?['run']?['name'])
   ```
   The message lists the status of each main step (Succeeded / Failed / Skipped) and links straight to the run.
3. **Settings → Run after → Big lead check:** tick **has failed**, **is skipped** and **has timed out**, then **untick is successful**.
   - *Why "is skipped"?* When any earlier step fails, every step after it is **skipped**. So *Big lead check* ends up skipped (or failed), and that triggers the alert. On a normal run *Big lead check* succeeds, so the alert is skipped.
4. **Save.**

> **Note:** a run that fails but sends the alert shows as **Succeeded** in the run history, because the "catch" step worked. Open the run to see the red step. In a real build, add a **Terminate (Failed)** after the Failure alert so the run history shows it as failed.

## Testing

Submit test leads through the form's **Preview**, then open **My flows → the flow → 28-day run history** and click each run. See the [README](README.md) for the five tests and their screenshots.

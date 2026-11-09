# Week 3 - Thursday: Building the same flow in Power Automate (step-by-step guide)

This builds exactly the same 3-box flow as my n8n version, but in Microsoft 365:

**Microsoft Form submitted → add a row to an Excel tracker → post a Teams alert**

Use **test data only** (made-up names and emails such as `sam.tester@example.test`). The Teams alert goes to a chat with the Flow bot, which only you can see, so nobody else gets spammed.

**Time needed:** about 30–40 minutes.

---

## Part A: Make the test form (Microsoft Forms)

1. Go to **forms.office.com** and sign in with your Appnable account.
2. Click **New Form**. Title: `Northwind Studio - Contact us (TEST)`.
3. Add these 5 questions (click **+ Add new** for each one):

| # | Question | Type | Required? |
| --- | --- | --- | --- |
| 1 | Name | Text | Yes |
| 2 | Email | Text | Yes |
| 3 | Company | Text | No |
| 4 | Budget (USD) | Text → click **…** → **Restrictions** → **Number** | No |
| 5 | Message | Text → turn on **Long answer** | Yes |

4. That's it. Forms saves automatically.

## Part B: Make the test leads tracker (Excel in OneDrive)

1. Go to **OneDrive** (office.com → OneDrive) → **+ Add new** → **Excel workbook**.
2. Rename it to `Leads Tracker (TEST)` (click the name at the top).
3. In row 1, type these headers in cells A1 to G1:
   `Submitted at` · `Name` · `Email` · `Company` · `Budget (USD)` · `Message` · `Status`
4. Select **A1:G1** → **Insert** → **Table** → tick **My table has headers** → **OK**.
5. Click inside the table → **Table Design** tab → change **Table Name** to `Leads` and press Enter.

> **Why a table?** Power Automate can only add rows to Excel data that is formatted as a **table**. This is the most common beginner mistake.

## Part C: Build the flow (Power Automate)

1. Go to **make.powerautomate.com** → **+ Create** → **Automated cloud flow**.
2. Flow name: `Week 3 - Scenario B lead to tracker and alert`.
3. In the trigger search box type **Forms** → pick **When a new response is submitted** → **Create**.
4. Click the trigger card → **Form Id** → choose **Northwind Studio - Contact us (TEST)**.

**Step 2: get the answers**

5. Click **+** under the trigger → **Add an action** → search **Get response details** (Microsoft Forms).
6. **Form Id:** the same form. **Response Id:** click in the box → the **lightning icon** (dynamic content) → **Response Id**.

> **Why two Forms steps?** The trigger only says "someone submitted". The *Get response details* step fetches what they actually typed.

**Step 3: add the row to Excel**

7. **+** → **Add an action** → search **Add a row into a table** (Excel Online (Business)).
8. Fill in:
   - **Location:** OneDrive for Business
   - **Document Library:** OneDrive
   - **File:** click the folder icon → `Leads Tracker (TEST).xlsx`
   - **Table:** `Leads`
9. The 7 columns now appear. Fill each one using the lightning icon (dynamic content from *Get response details*):

| Excel column | Put this in it |
| --- | --- |
| Submitted at | **Submission time** |
| Name | **Name** |
| Email | **Email** |
| Company | **Company** |
| Budget (USD) | **Budget (USD)** |
| Message | **Message** |
| Status | type the word `New` |

**Step 4: post the Teams alert**

10. **+** → **Add an action** → search **Post message in a chat or channel** (Microsoft Teams).
11. **Post as:** Flow bot · **Post in:** Chat with Flow bot · **Recipient:** your own email.
12. **Message:** type the text below, inserting the dynamic content where shown in [brackets]:

```
New website lead: [Name] ([Company])
Email: [Email]
Budget: $[Budget (USD)]
Message: [Message]
Please reply within 24 hours.
```

13. Click **Save** (top right).

## Part D: Test it and take the screenshots

1. Click **Test** → **Manually** → **Test**. The flow now waits.
2. Open your form → **Preview** → fill it in with test data, for example:
   - Name: `Sam Tester` · Email: `sam.tester@example.test` · Company: `Brightside Bakery (test)` · Budget: `12000`
   - Message: `We need a new website with online ordering, and we're interested in a monthly retainer.`
3. Click **Submit**. Within about a minute the flow runs.
4. Back in Power Automate, every step should show a **green tick** and the page says **Your flow ran successfully**.

**Take these 3 screenshots** (Windows: `Win + Shift + S`, Mac: `Cmd + Shift + 4`):

- [ ] **The run page** with the green ticks. This is the required screenshot for the trainee guide.
- [ ] **The Excel tracker** showing the new row.
- [ ] **The Teams message** from the Flow bot.

Send them to me and I'll add them to GitHub and the trainee guide.

## If something goes wrong

| What you see | Usual cause | Fix |
| --- | --- | --- |
| Flow never starts | Test started after you submitted | Click **Test** again, then submit a new response |
| Excel step fails: "No table was found" | Data isn't formatted as a table | Redo Part B, step 4 |
| Excel columns don't appear | Wrong file or table picked | Re-select **File** and **Table** |
| Budget step fails | Budget answer isn't a number | Add the Number restriction in the form, or leave Budget blank |
| Teams step fails | Recipient email typed wrong | Use your full Appnable email |

## How this matches the n8n build

| Box | n8n | Power Automate |
| --- | --- | --- |
| 1. Trigger | n8n Form Trigger | Microsoft Forms: *When a new response is submitted* (+ *Get response details*) |
| 2. Add row to tracker | Data Table: *Insert row* | Excel Online: *Add a row into a table* |
| 3. Alert | Send Email (test inbox) | Teams: *Post message in a chat or channel* |

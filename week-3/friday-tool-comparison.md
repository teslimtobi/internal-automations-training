# Week 3 - Friday: Comparing the tools

On Friday I skimmed **Make.com for beginners** for a third view. Make builds on a canvas like n8n (it calls the automation a *scenario* and each step a *module*), is hosted like Zapier, and charges per operation.

## 5-line comparison

1. **Easier in n8n:** the form comes built in, the whole flow sits on one canvas, and after a run I can click any node to see exactly what data went in and out. That makes it very easy to learn and debug.
2. **Harder in n8n:** I had to host it myself, which meant installing it and matching the right Node.js version. Connecting it to Microsoft 365 would also need an app registration, so for testing I used n8n's own data table and a test email inbox instead of Excel and Teams.
3. **Easier in Power Automate:** Forms, Excel and Teams all connect with my Appnable sign-in. There's nothing to install or host, and the run history shows a green tick on every step.
4. **Harder in Power Automate:** it needs an extra *Get response details* step after the form trigger, the Excel data has to be formatted as a table first, and the designer is slower to click through than n8n's canvas.
5. **My pick for this flow:** **Power Automate**, because the form, the tracker and the alert all live in Microsoft 365, which is where Northwind's (and Appnable's) trackers already are. I'd pick n8n when a flow has to connect many different non-Microsoft apps, or needs custom logic and self-hosting.

> **Note:** lines 3 and 4 are based on the build guide and my earlier Power Automate work on the interns' daily update flow. I'll update them after my Week 3 Power Automate test run if anything turns out differently.

## Self-check answers

**What is the trigger, and what exactly starts it?**
A **form submission event**. In n8n, it's the n8n Form Trigger firing when someone presses *Submit* on the test contact form. In Power Automate, it's *When a new response is submitted* on the Microsoft Form. Nothing runs on a timer: one submission means exactly one run.

**How is this like the GitHub Actions workflows you built before?**
It's the same rule-based pattern: an **event** starts it, then **steps** run in a fixed order, and each step uses the output of the one before. In GitHub Actions, *a blog draft is pushed* triggered *run the SEO check → wait for approval → publish*. Here, *a lead submits the form* triggers *add a row → send an alert*. In both, the run history shows each step passing or failing.

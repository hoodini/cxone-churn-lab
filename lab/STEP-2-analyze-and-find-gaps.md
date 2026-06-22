# Step 2 — Analyze the data and find the gaps

> **Goal:** Have Claude read the customer file from top to bottom, find the problems hiding in it, and explain why customers are leaving.
> **Time:** ~15 min  ·  **You'll need:** the file `data/nice_cxone_churn.csv` open with Claude (using the same chat you started in Step 1 is perfect — or a new one, see below).

## 🎯 What you're doing
In Step 1 you got a first feel for the data. Now you go deeper. You're asking Claude to act like a senior data analyst: catch every flaw in the file, measure how many customers are leaving (that number is called the **churn rate** — the share of customers who quit), and explain *why* they leave.

This is the heart of the lab. Everything you build later — the web page, the product idea, the deck — stands on what you learn here. You don't need any data background. You just paste one prompt and read what comes back.

## ✅ Before you start
- [ ] You finished **Step 1**, so Claude has already taken a first look at the file.
- [ ] The file `data/nice_cxone_churn.csv` is available to Claude in this chat. (A "chat" is one running conversation with Claude. If you're still in the same conversation as Step 1, you're all set. If you closed it and opened a fresh one, you'll need to give Claude the file again — see the reminder under the prompt below.)
- [ ] You have a few minutes. This answer will be longer than Step 1 — that's expected and good. You won't have to read every line.

## 📋 The prompt — copy this into Claude
Copy the entire gray block below, exactly as it is, and paste it into the message box where you type to Claude. Then send it.
```text
Now act as a senior data analyst and analyze nice_cxone_churn.csv in depth. I want four things,
with the actual numbers behind every claim:

1. DATA QUALITY — Find every problem in the data: missing values, blanks, impossible values
   (e.g. usage above 100%, negative tenure), duplicates, and suspicious outliers. For each one,
   tell me how many rows are affected and how you'd clean or handle it.

2. THE BIG PICTURE — What's the overall churn rate? Then break churn down by segment, by region,
   by industry, and by contract type. Call out where it's surprisingly high or low.

3. CHURN DRIVERS — Which columns most separate the customers who churned from the ones who stayed?
   Rank the top drivers and show the difference in numbers for each.

4. ANOMALIES & SURPRISES — Find anything counterintuitive. In particular: are there customers who
   look healthy on the surface but still left? Does the churn_risk_score column actually agree with
   who really churned — and where does it get it wrong?

Finish with the 3 most important, non-obvious insights a NiCE manager should know, in plain English.
Treat this as synthetic data, so describe the relationships you find as patterns in THIS dataset.
```
**Reminder — how to give Claude the file (only needed if it can't see it yet):**
- **In Claude.ai (the website or app):** click the paperclip icon near the message box and upload `nice_cxone_churn.csv` from where you saved it.
- **In Claude Code (the terminal tool):** you don't attach anything — just make sure `nice_cxone_churn.csv` is inside your project folder. Claude can already see the files there.

Not sure which one you're using? If you're in a web browser or the desktop app, it's Claude.ai. If you're typing commands in a black terminal window, it's Claude Code.

## 👀 What you should expect back
A good answer is organized into the four numbered sections you asked for, with real numbers behind each claim. You don't need to verify the math — just skim and look for these signs that Claude did the job well:

- **Data problems caught and counted** — a short list of flaws, each with how many rows it affects: a few "impossible" rows (like more active seats than the customer is licensed for, or negative tenure), a few customers with a satisfaction score of 0 (which almost always means "not recorded," not a real zero), a couple of blank regions or industries, one wildly large revenue number, and one customer that appears twice (a duplicate).
- **An overall churn rate of roughly one in five** — about 21% of customers have left.
- **Big differences between groups** — expect one region to leave at roughly double the rate of the others, and smaller customers to leave far more often than large ones.
- **Clear reasons for leaving, ranked** — things like barely-used seats ("shelfware"), usage dropping over time, month-to-month contracts, and not using Enlighten AI should stand out, each with numbers behind it.
- **A "looks healthy but left anyway" surprise** — a small group of big accounts that seemed fine (happy, almost no complaints) but were quietly using the product less and less.
- **A check on the risk score** — Claude should test whether the `churn_risk_score` column actually matched who really left, and point out where it got it wrong.
- **Three plain-English takeaways** at the end that a manager could act on tomorrow.

If your numbers come out a little different from the ones above, don't worry — small wording differences in how Claude counts are normal. The patterns are what matter.

## 💡 Make it better (optional follow-ups)
Already got a good answer? Paste any of these as your *next* message to dig deeper. (You don't need to re-attach the file — Claude still has it from a moment ago.)
```text
Show me the 10 customers the risk score got most wrong — looked low-risk but churned. List their key numbers in a table.
```
```text
For the region with the highest churn, dig into WHY. Is it really the region, or is something else going on underneath?
```
```text
Turn your top 3 insights into a one-paragraph summary I could read aloud to a manager in 30 seconds.
```

## 🧯 If something goes wrong
- **Claude says it can't see the file.** Give it the file again: use the paperclip to re-upload `nice_cxone_churn.csv` (Claude.ai), or confirm the file is sitting in your project folder (Claude Code). Then paste the prompt once more.
- **The answer is huge and overwhelming.** That's normal — but you can shrink it. Reply: "Give me a short summary first — just the headlines — then I'll ask for detail on the parts I care about."
- **The numbers look off, or Claude seems to be guessing.** Reply: "Recompute directly from the CSV and show the row counts you used." (In Claude Code, Claude can run a small program over the file; in Claude.ai it reads the file directly. Either way this nudges it to count instead of estimate.)
- **You want the answer again, done differently.** Just ask in plain words: "Redo section 3 as a ranked table," or "Explain that like I'm completely new to data." You can always nudge — nothing breaks.
- **Claude added a disclaimer about made-up data.** That's fine, and expected — this data *is* synthetic (invented) on purpose. The patterns are still real *inside this file*, which is exactly what we're studying.

## ➡️ Next
Now that you know the story hiding in the data, head to **[STEP-3-build-landing-page.md](STEP-3-build-landing-page.md)** to turn these insights into something people can see.

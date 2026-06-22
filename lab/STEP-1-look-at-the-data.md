# Step 1 — Look at the data

> **Goal:** Understand what's inside the customer file before you analyze anything.
> **Time:** ~5 min  ·  **You'll need:** the file `data/nice_cxone_churn.csv` (it lives in this lab's `data` folder) and Claude open in front of you

## 🎯 What you're doing
You're about to meet your data for the first time. The file is a **CSV** — just a plain spreadsheet (rows and columns) saved as text. Before hunting for insights, you want the basics: how big is this file, what's in each column, and what one row actually represents. This is exactly what a careful analyst does first — you never analyze a file you don't understand. Think of it as reading the label before you cook.

> **Heads-up, so nothing surprises you:** this data is **synthetic** — it's made-up, realistic-looking practice data, not real NiCE customers. And one word you'll see a lot is **churn**, which just means a customer left / cancelled. That's all it means.

## ✅ Before you start
- [ ] You have the file `data/nice_cxone_churn.csv` ready (it's in this lab's `data` folder). You don't need to open it yourself — Claude will read it for you.
- [ ] You have Claude open. Two ways to use it, pick whichever you have:
  - **Claude.ai** — open [claude.ai](https://claude.ai) in your browser and start a new chat. (You'll *attach* the file, explained in the prompt section below.)
  - **Claude Code** — the version that runs in a terminal inside this lab's project folder. (It reads the file straight from the folder, no attaching needed.)
  - Not sure which you have? If it's a website in your browser, it's Claude.ai. Either one works for this whole lab.
- [ ] Nothing from a previous step is needed — this is the very first step.

## 📋 The prompt — copy this into Claude
Select everything inside the grey box below (from `I'm sharing` down to the last line), copy it, and paste it into Claude as your message. Don't change anything — the wording is doing real work.
```text
I'm sharing a CSV file called nice_cxone_churn.csv. It's a (synthetic) customer dataset for
NiCE CXone, the cloud contact-center platform — each row is one customer company, and the data
covers their contract, product usage, support history, and whether they churned (left) or are
still active.

Before any analysis, just help me understand what I'm looking at:
1. How many rows and how many columns are there?
2. List every column with a short, plain-English explanation of what it means.
3. Show me 5 example rows in a readable table.
4. In one sentence, what does a single row represent?

Don't look for patterns or insights yet — I only want to understand the shape of the data.
Explain it like I'm new to data analysis.
```
**Attaching the file (this is the part beginners trip on):**
- **In Claude.ai:** before you hit send, click the **paperclip icon** (📎) near the message box, then find and pick `data/nice_cxone_churn.csv`. "Attaching" just means handing the file to Claude so it can read it. Then send your message.
- **In Claude Code:** you don't attach anything. Just make sure the file is in the `data` folder (it already is) and send the prompt — Claude can open the file itself.

## 👀 What you should expect back
A calm, organized "here's what you've got" answer — no charts, no conclusions yet. Look for:
- A row and column count: around **1,001 rows** and **40 columns**. (One row is a duplicate on purpose — that's a planted detail for later, not a mistake on your end. Claude may or may not flag it here; either is fine.)
- A clear list of all 40 columns, each with a one-line plain-English meaning (for example, `arr_usd` = the yearly money the customer pays, `churned` = whether they left).
- A small, readable table of **5 example rows** so you can see real values, not just column names.
- A one-sentence answer that **one row = one NiCE CXone customer company**.
- A mix of column types: company details (industry, region, segment), money (`arr_usd`), product usage (`active_seats`, `seat_utilization`), and health signals (`avg_csat`, `health_score`, `churn_risk_score`).
- A friendly tone that explains terms instead of assuming you know them.

Don't worry about understanding every column yet — right now you just want to feel like you know the *shape* of the file. That's the whole goal of this step.

## 💡 Make it better (optional follow-ups)
Want to go a little deeper? Send any of these as your next message (no need to re-attach the file in the same conversation):
```text
Group the 40 columns into a few simple categories (like "who the customer is", "money", "product usage", "support", "health") so it's easier to hold in my head.
```
```text
Pick the 8 columns you think matter most for understanding churn, and tell me why each one matters — in plain English.
```
```text
Show me 3 example rows of customers who churned and 3 who are still active, side by side, so I can see the difference.
```

## 🧯 If something goes wrong
- **Claude says it can't see the file.** Re-attach it. In Claude.ai, click the paperclip (📎) and re-select `nice_cxone_churn.csv`. In Claude Code, confirm the file is really in the `data` folder.
- **The answer is huge and overwhelming.** Reply: "Can you give me a shorter version — just the row count, column count, and one row's meaning?"
- **You want it explained more simply.** Reply: "Explain that again like I've never seen a spreadsheet before."
- **The column count looks off** (you saw a number other than 40). Reply: "Count the columns again carefully and list them numbered 1 to 40." Small counting slips happen; asking it to recount usually fixes them — you didn't do anything wrong.
- **Claude.ai and Claude Code give slightly different-looking answers.** That's normal — the prompt works in both. Claude Code reads the file from the folder; Claude.ai needs the file attached in each new conversation.

## ➡️ Next
Head to **STEP-2-analyze-and-find-gaps.md** to start finding patterns — and the gaps hiding in the data.

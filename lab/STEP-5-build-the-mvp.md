# Step 5 — Build the MVP prototype (minimal, fake data)

> **Goal:** Turn your MVP idea from Step 4 into a real, clickable web page you can open and demo.
> **Time:** ~10 min  ·  **You'll need:** the MVP idea Claude wrote up in Step 4 (keep that same chat window open).

## 🎯 What you're doing
So far you've found patterns in the data and shaped an idea. Now you turn that idea into something you can actually click. You'll ask Claude to build a small working web page — a "prototype," which just means a rough first version meant to show the idea, not a finished product. It uses made-up numbers but looks and behaves like the real thing. This is the moment the idea stops being words and becomes a thing you can show people.

You don't need to write any code yourself. Claude writes it; you copy a prompt, paste it, and open the file it gives back.

## ✅ Before you start
- Stay in the **same Claude chat** you used in Step 4, so Claude still remembers your MVP idea. ("Chat" = the same conversation window; don't open a new one.) If you did start a new chat, scroll up in Step 4, copy the MVP description Claude wrote, and paste it into the new chat first so it has the context.
- You do **not** need the CSV (the spreadsheet file) for this step. The prototype uses made-up sample data on purpose — nothing real, nothing private, so you can share it freely.
- Pick a folder on your computer where you'll save the file (your Desktop or Documents is fine). You'll save it with a name like `prototype.html` — the `.html` ending is what makes your computer open it as a web page.

## 📋 The prompt — copy this into Claude
Click inside the gray box below, copy the whole thing, and paste it into Claude as your next message — right after the Step 4 conversation.
```text
Now build a working prototype of that MVP as a single self-contained HTML file (inline CSS and
JavaScript, no backend, no real data — use a small amount of hardcoded mock data that you make up).

Keep it as minimal as possible: the smallest version that demonstrates the core idea end-to-end
and feels real to click through. If the MVP is an early-warning "customer health radar," then show
a dashboard of mock accounts with a smarter health score that also reacts to declining usage,
clearly flag the "silent at-risk" accounts that an old satisfaction-only score would miss, and let
me click an account to see why it's at risk and one recommended action.

Modern, clean, professional UI. It must work by just double-clicking the file. Put a short comment
at the very top of the file stating what it is and that all the data is fake sample data.
Give me the finished HTML file.
```
(The words "HTML," "CSS," and "JavaScript" are just the building blocks of any web page. You don't need to understand them — Claude handles all of it.)

## 👀 What you should expect back
Claude will reply with one block of code (or a file you can download) plus a short note on how to open it. Don't be put off by the wall of code — you never have to read or touch it. When you open the page in your web browser, expect something like:
- A clean **dashboard** (a single screen that shows everything at a glance) listing a handful of made-up customer accounts — with company names, dollar figures, and a health number for each.
- A **health score that's smarter than the old one**: it turns red not just when a customer is unhappy, but when their usage is quietly dropping. (This mirrors a real pattern in the lab data — declining usage is an early warning the old scores miss.)
- One or two **"silent at-risk" accounts** flagged on purpose — the ones that look fine on the surface (happy, no complaints) but are sliding underneath. These are the most interesting ones to point at in your demo.
- **Clickable accounts**: click one and a panel opens showing *why* it's at risk and *one* recommended action to take.
- A **modern, professional look** — real colors, spacing, and layout, not a plain wall of text.
- Everything runs from **one file you can double-click**, with no install and no internet needed, and a note at the top of the code reminding you the data is fake.

If you got all of that, you're done — head to the Next step. The follow-ups below are optional.

## 💡 Make it better (optional follow-ups)
Want to push it further? Paste any of these into the **same chat** (one at a time), then re-open the new file Claude gives you.
```text
Add a small summary bar at the top showing total accounts, how many are at risk, and total money at risk.
```
```text
Make the silent at-risk accounts stand out more — add a clear badge and sort them to the top of the list.
```
```text
Add one mock "early-warning" chart per account showing usage trending down over the last few weeks.
```

## 🧯 If something goes wrong
- **Claude gave me code but I don't know what to do with it.** Reply: "Save this as a file I can download, and tell me exactly how to open it." (If you're using Claude Code on your computer, the file is usually saved into your folder already — look for `prototype.html` and double-click it.)
- **I have the code but no file yet.** In the chat (Claude.ai) version, look for a **Download** button near the code, or copy all the code, paste it into a plain text editor (TextEdit on Mac, Notepad on Windows), and save it with a name ending in `.html`. Then double-click that file.
- **I double-clicked and it looks broken or blank.** Tell Claude exactly what you see and say: "It opened blank in my browser. Please fix it so it works by just double-clicking, all in one file." Usually a small piece got cut off and Claude will resend it whole.
- **The page looks plain or has almost no data.** Reply: "Add more mock accounts and make the design more modern and colorful." Claude will rebuild it richer.
- **I want a different look.** Just describe it in plain words: "Make it dark mode," or "Make it look like a NiCE product." Claude will redo the styling.
- **It behaves differently in Claude.ai vs Claude Code — is that normal?** Yes. In Claude.ai (the website) you copy or download the code; in Claude Code (on your computer) the file is written straight into your folder. Either way you end up with one HTML file to double-click.

## ➡️ Next
Open **STEP-6-management-deck.md** to turn your prototype and findings into a short management deck.

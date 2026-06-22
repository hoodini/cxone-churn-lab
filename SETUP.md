# 🚀 Setup — start here (about 5 minutes)

Welcome! This page gets you ready in a few minutes. No experience needed. Read it once, follow the steps, and you'll be off.

---

## 🤔 What is this?

This is a hands-on lab where **you use Claude to take a customer dataset all the way from raw numbers to a real result** — first you understand the data, then you find the insights hiding inside it, then you turn one of those insights into a product idea, build a quick prototype, and finish with a polished management deck you could actually present. You'll do it all with a **fake (synthetic) NiCE CXone customer dataset** — it's completely made up, contains no real customers or real NiCE numbers, and is totally safe to share, copy, and experiment with. Claude does the heavy lifting; you just copy, paste, and watch it come together.

---

## 🧰 What you need

Just **one thing: a Claude account.** If you don't have one yet, go to [claude.ai](https://claude.ai) and sign up — it's free to start.

There are **two easy ways** to do this lab. Pick the one that fits you:

- **Option 1 — Claude.ai in your browser (EASIEST — recommended for beginners). 👈**
  - This is just the Claude website, like any other site you visit.
  - You hand the data file to Claude using the **📎 paperclip** button (we'll show you exactly how).
  - If you've never used Claude before, **choose this one.** Nothing to install.

- **Option 2 — Claude Code / Claude desktop (for people comfortable with a terminal).**
  - This runs on your computer and works inside the lab's folder.
  - You don't attach anything — the data file just **sits in the folder and Claude reads it directly**.
  - Pick this only if a terminal/command line feels comfortable to you.

> **Not sure which you have?** If it's a website open in your browser, it's **Claude.ai** — go with Option 1. Either option works for the entire lab, start to finish.

---

## 📥 Get the files

You need a copy of this lab on your computer. Two ways:

- **The easy way (no tools needed):**
  1. On the lab's **GitHub page**, click the green **`< > Code`** button (top-right of the file list).
  2. Choose **Download ZIP**.
  3. Find the downloaded ZIP and **unzip it** (double-click it on most computers). You'll get a folder with all the lab files inside.

- **The git way (if you already use git):**
  ```bash
  git clone <the-repo-url>
  ```

Either way, the one file that matters most lives here:

> 📊 **`data/nice_cxone_churn.csv`** — this is THE dataset. You'll use it in the first couple of steps.

---

## 📎 How to attach the CSV to Claude

This is the part beginners worry about — it's genuinely easy. Use the method that matches your option above:

- **Claude.ai (browser):** In your chat, click the **📎 paperclip** icon near the message box, find and select **`data/nice_cxone_churn.csv`**, then send your message. "Attaching" just means handing the file to Claude so it can read it. (Tip: if you start a brand-new chat later, you may need to attach it again.)

- **Claude Code / desktop:** **You don't attach anything.** As long as the file is in the `data` folder (it already is), just send your prompt — Claude reads the file straight from the folder.

---

## 🧭 How the lab works

- The lab is **6 steps**, in the **`lab/` folder**. Do them **in order** — each one builds on the one before it.
- Every step is a short page with a **prompt you copy and paste into Claude.** That's the whole pattern: copy, paste, read what comes back.
- All the prompts are **also collected in one place** at **`prompts/ALL_PROMPTS.md`**, if you'd rather grab them from a single page.
- **Keep your chat going.** Because the steps build on each other, stay in the *same conversation* with Claude so it remembers what you did earlier.

---

## ⏱️ How long it takes

About **60–90 minutes** end to end. But there's no pressure — **you can stop after any step** and still have something finished and shareable to show for it.

---

## 🔒 A note on the data

The dataset is **100% synthetic — completely made up.** Any pattern you discover is a **designed teaching example**, not a real NiCE business fact. That's the point: it gives you something interesting to find while you learn the workflow. It's **safe to share, safe to break, and safe to experiment with** — go ahead and play.

---

## ✅ Ready?

**Start with [`lab/STEP-1-look-at-the-data.md`](lab/STEP-1-look-at-the-data.md).**

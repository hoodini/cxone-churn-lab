# Step 3 — Build a stunning landing page from the data

> **Goal:** Turn your churn insights into a beautiful web page — a single file you could put on screen in front of executives.
> **Time:** ~10 min  ·  **You'll need:** the same Claude chat (conversation) you used in Step 2, still open, so Claude remembers the numbers it found.

## 🎯 What you're doing
In Step 2, Claude dug into the data and found the story. Now you'll ask it to *show* that story as a polished web page — a single file that opens in your web browser when you double-click it, no internet upload and no website needed. There's no coding and no design tools here. You describe what you want in plain English, and Claude writes the whole thing for you.

A quick note before you start, so nothing surprises you: **what you get back depends on which Claude you're using.**
- **Claude.ai** (in your web browser) often shows the finished page *live* in a preview panel on the right — great for a quick look. You can also download it as a file.
- **Claude Code** (the version that runs in a terminal/folder on your computer) saves a real file into your project folder that you open in your browser.
Either way, the end result is the same: one file that is *your* web page. We'll point out the difference again whenever it matters.

## ✅ Before you start
- Keep the **same chat (conversation) from Step 2 open.** A "chat" is one continuous thread with Claude — Claude only remembers things you discussed *in that same thread*. It needs to remember the numbers it found in Step 2 (the overall churn rate, the top drivers, the "silent churners").
- If you accidentally closed that chat, no problem — open Step 2 again, paste its prompt and re-attach the CSV file (`data/nice_cxone_churn.csv`) the way you did before, let the analysis finish, then come back here.
- Make sure Step 2 actually finished and showed you real numbers (you should have seen percentages, not just a description of what it *plans* to do). This step turns those numbers into the page.

## 📋 The prompt — copy this into Claude
Copy the whole grey block below and paste it into the same chat, right under your Step 2 results. (To copy, drag-select the text, or use the copy button if your screen shows one.) Then press Enter / Send.

```text
Build me a single, self-contained HTML file (one file: inline CSS and JavaScript, no build step,
works by double-clicking it) that presents the key insights from nice_cxone_churn.csv as a
stunning, modern, executive "data story" web page.

Include:
- A bold hero section with the single headline finding and the overall churn number.
- The top churn drivers shown as clean, labeled charts.
- The breakdown of churn by segment and by region.
- A standout callout for the "silent churners" — high-value customers who left while looking
  healthy, because the current risk score missed them.
- A short "what we should do about it" section at the end.

Make it beautiful: a polished dark theme, big readable typography, smooth scrolling, animated
number counters, and real chart visualizations (you can load a charting library like Chart.js
from a CDN). Use the actual numbers from the analysis so the values are correct. It should look
like something I'd be proud to put on screen in front of executives. Give me the finished HTML file.
```

> New words in that prompt, in plain English: an **HTML file** is just a web page saved as a file on your computer. **"Self-contained"** / **"single file"** means everything (text, styling, charts) lives in that one file, so you can share it or open it on its own. **Chart.js from a CDN** is a free, ready-made charting tool Claude pulls in from the internet — which is why the charts need you to be online to show up.

## 👀 What you should expect back
Claude will write a complete web page and hand it to you. (In Claude.ai you may also see it render live in a preview panel; in Claude Code it's saved as a file in your folder — see "If something goes wrong" for how to open it.) A good result will include:

- A big, bold opening (often called the **"hero"** — the large banner at the very top) showing one headline finding and the **overall churn rate of about 21%**, often counting up on screen.
- Clean, labeled charts — likely bars or donuts — for the **top churn drivers**.
- A **churn-by-segment** view showing the pattern that smaller customers tend to leave more (SMB around 28%, down to Enterprise around 7%). *Segment just means customer size: SMB = small business, Mid-Market = medium, Enterprise = large.*
- A **churn-by-region** view that makes APAC stand out (roughly double the rest, near 36%). *APAC = the Asia-Pacific region.*
- A highlighted **"silent churners"** callout — the handful of healthy-looking, high-value accounts the risk score missed. This is meant to be the emotional punch of the page.
- A short, plain-English **"what we should do about it"** section at the end.
- Smooth scrolling, a dark background, and numbers that animate as you scroll — it should *feel* finished.

Don't worry if your exact percentages differ by a point or two from the examples above — Claude is reading the real data, so small differences are normal and fine.

## 💡 Make it better (optional follow-ups)
Totally optional. Paste any of these into the **same chat** to push the page further, then re-open the file to see the change.

```text
The colors feel a bit flat. Use NiCE brand colors and add a subtle accent gradient to the hero.
```

```text
Add a small "data note" footer admitting this is synthetic (made-up) data and listing the 1,001 rows and 40 columns we analyzed.
```

```text
Make a second version optimized to look great on a phone screen, then tell me which one to use when.
```

## 🧯 If something goes wrong
- **"Claude gave me a wall of code — how do I actually see the page?"** That code *is* the page. You just need to save it as a file ending in `.html` and double-click it; it opens in your web browser. In **Claude.ai**: use the download button on the code (or in the preview panel), or ask "save this as a file I can download." In **Claude Code**: type "save this as churn-story.html in my folder" and it creates the file for you — then find `churn-story.html` in the folder and double-click it.
- **"The charts are empty or blank."** The page borrows its charting tool from the internet, so it needs you to be online. Check your connection, then refresh the page (Cmd+R on Mac, Ctrl+R on Windows). If they still don't show, paste back: "the charts aren't showing — please fix the Chart.js loading."
- **"The numbers look wrong or made up."** Tell Claude: "use the exact numbers from your Step 2 analysis above, not estimates." If you opened a brand-new chat, Claude has lost those numbers — go back and re-run Step 2 first (the numbers live in that thread, not in Claude's permanent memory).
- **"It looks plain, not like the description."** Just ask: "make it more polished — bigger type, more spacing, smoother animations." You can keep refining as many times as you like; each request builds on the last.
- **Still stuck on Claude.ai vs Claude Code?** In **Claude.ai** the page may render live in a preview panel — handy for a glance — and you download it to keep it. In **Claude Code** Claude writes a real `.html` file into your folder that you open in your browser. Either way, the file is yours to keep, share, and open offline (the text and layout work offline; only the charts need internet).

## ➡️ Next
Next up: open **STEP-4-competitors-and-mvp.md** to turn this story into a real product idea.

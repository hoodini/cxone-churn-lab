# Step 4 — Compare with competitors and propose an MVP

> **Goal:** Use what the data told us to size up the competition, then pitch one small product idea that fights churn.
> **Time:** ~15 min  ·  **You'll need:** nothing to download — just Claude open in front of you (the chat from Step 2 is handy but not required).

## 🎯 What you're doing
So far you found *why* customers leave. Now you turn that into a plan. You'll ask Claude to look at NiCE CXone's rivals — the other companies that sell contact-center software — see what each one does to keep customers from leaving, and then propose ONE small feature NiCE could build. "MVP" stands for **Minimum Viable Product** — the smallest version of an idea that still delivers real value. Small on purpose, so a team could actually build it.

No data file this time. This step is about thinking, not the spreadsheet.

## ✅ Before you start
- **You don't need to remember anything from Step 2.** The three findings you discovered there (unused seats, the APAC region churning more, and the "silent" customers the risk score misses) are already written into the prompt below. You'll just copy and paste — no retyping.
- **Turn on web search if your Claude has it (optional).** In Claude.ai, look for a small **web / search toggle or globe icon** near the box where you type your message, and switch it on. Not sure if you have it, or don't see it? No problem — skip this. Claude will still answer using what it already knows; just treat any specific competitor details as a starting point you'd double-check later.
- **One reminder:** the numbers in our data are made up for this lab, so the "findings" are real *in this dataset* but aren't actual NiCE facts. That's fine — the skill you're practicing is the thinking.

## 📋 The prompt — copy this into Claude
Start a **new message** to Claude (just like sending a new chat). Copy the entire block below — every line, top to bottom — and paste it in, then send it. It's long on purpose; that's normal. If your Claude shows a small **copy icon** in the corner of the box when you hover over it, that's the easy way to grab all of it.
```text
Based on what we found in NiCE CXone's data, I want to turn insight into action. Our key findings:
- Low product adoption / unused seats ("shelfware") is a top driver of churn.
- A region (APAC in the data) churns far more, and the real cause is an onboarding gap, not geography.
- A group of high-value "silent" customers churn while looking healthy, because the current
  churn-risk score ignores declining usage.

First, research NiCE CXone's main competitors in the contact-center / CCaaS market — for example
Genesys, Five9, Talkdesk, Amazon Connect, Cisco, 8x8, Twilio Flex. For each, what do they offer
around customer health, churn prevention, adoption, and proactive customer success? What are
customers praising or complaining about?

Then tell me:
- Where is NiCE ahead, and where is it behind these competitors on keeping customers?
- Based on the competitive picture AND our data findings, propose ONE focused MVP feature NiCE
  should build to reduce churn.

Describe the MVP in one tight paragraph: what it is, who it's for, the single problem it solves,
and why it would win. Keep it realistic and as minimal as possible — the smallest thing that
delivers the value.
```
*(Quick translation: "CCaaS" just means Contact Center as a Service — cloud software for running a customer support center. "Customer success" is the team whose job is keeping customers happy so they renew. You don't need to know these to run the prompt — Claude does the work.)*

## 👀 What you should expect back
A good answer reads like a quick competitive briefing, then lands on one clear idea. You'll probably see:
- A short rundown of each competitor (Genesys, Five9, Talkdesk, and others) covering what they do around keeping customers — not just a list of features.
- Honest two-sided framing: where NiCE looks strong (its Enlighten AI is a natural strength to point to) and where rivals may be ahead.
- A clear link back to your three findings, especially the **"silent churner" blind spot** — the idea that today's risk score misses customers whose usage is quietly dropping off.
- **ONE focused MVP, not five.** If Claude lists several, that's your cue to push it to pick one (see the follow-ups below).
- A tight one-paragraph pitch that names what it is, who it's for, the single problem it solves, and why it would win.
- Realistic scope — an MVP that feels buildable in weeks, not a multi-year platform.

Don't worry if it doesn't match this list exactly. As long as you got a competitor read plus one small, sensible idea, you're in good shape.

## 💡 Make it better (optional follow-ups)
Pick one, type it as your next message (a normal reply in the same chat), and send it.
```text
Pick just ONE MVP and explain why it beats the others in one paragraph.
```
```text
Rewrite the MVP pitch for a busy executive: 4 sentences, plain language, no jargon.
```
```text
What would the very first version look like, and what would we deliberately leave out of v1?
```

## 🧯 If something goes wrong
- **Claude says it can't search the web.** Totally fine. Reply: "No web access is fine — use what you know and flag anything I should double-check." Treat any competitor claims as a draft to verify, not gospel.
- **The answer is huge and hard to read.** Reply: "Summarize this in 10 bullets, then the MVP in one paragraph."
- **It proposed five features, not one.** Reply: "Choose the single best one and drop the rest."
- **It made up details about a competitor.** Reply: "Mark anything you're unsure about as 'needs verification' and don't state guesses as facts."
- **Your answer looks different from a teammate's.** That's normal — Claude varies its wording every time, and Claude.ai and Claude Code can phrase things differently. The *shape* of the answer is what matters, not the exact words.

## ➡️ Next
Now build it: open `STEP-5-build-the-mvp.md`.

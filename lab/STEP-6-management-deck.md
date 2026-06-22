# Step 6 — Create the management deck (NiCE brand)

> **Goal:** Turn everything you found into a short, on-brand slide deck that asks NiCE leadership to back your idea.
> **Time:** ~15 min  ·  **You'll need:** the outputs from Steps 2–5 (the clean data, the findings, the "silent churner" surprise, and the MVP idea), all in the **same Claude chat** you've been using. Best case: the `nice-brand` skill installed. No skill? You'll use `reference/NICE_BRAND_CHEATSHEET.md` instead — the steps below show you exactly how.

## 🎯 What you're doing
This is the finale. You've done the analysis — now you tell the story to the people who can say "yes." Claude builds a polished, on-brand presentation that walks leadership from "here's what we found" to "here's what we should do." You stop being someone who looked at a spreadsheet and become someone with a recommendation.

You don't need to design anything yourself. You paste one prompt, and Claude writes the whole deck for you.

## ✅ Before you start
- [ ] **Use the same chat as Steps 2–5.** Scroll up — if you can still see your earlier work in this conversation, Claude still remembers it and you're good. (Starting a fresh chat? See the fix at the bottom of this page.)
- [ ] Quickly remind yourself of the four things this deck will lean on, in case Claude asks:
  - the **headline churn findings** (your numbers from Step 2),
  - the **"silent churners"** — healthy-looking, high-value accounts that quietly stopped using the product and left anyway (Step 2),
  - the **onboarding-gap story** behind your worst region — i.e. the region churns more because fewer customers there finished onboarding, *not* because of where it is (Step 2),
  - and the **MVP idea** you shaped in Step 4 (and maybe prototyped in Step 5).
- [ ] Decide which path you're on:
  - **Path A — you have the `nice-brand` skill installed.** Easiest. Claude uses the real NiCE logos, fonts, colors, and templates for you.
  - **Path B — you do NOT have the skill.** No problem. You'll open one short file, copy a brand "brief" out of it, and paste it in front of the prompt. Your deck will still look unmistakably NiCE.
- [ ] **Not sure which you have? Just try Path A.** If Claude replies that it can't find a skill called `nice-brand`, switch to Path B. Nothing breaks either way.

## 📋 The prompt — copy this into Claude

> **How to "copy this into Claude":** select all the text inside the gray box below, copy it, click in the message box at the bottom of your Claude chat, paste, and press Enter. That's it.

### Path A — you have the `nice-brand` skill
Copy this whole block and paste it into Claude as one message.
```text
Use the nice-brand skill to create a management presentation deck for NiCE leadership.

The story: in one short workshop we took our NiCE CXone customer data, analyzed it with AI, and
found churn insights worth acting on. Walk leadership through it and ask for buy-in.

Cover, one idea per slide:
1. Title + the one-line message.
2. What we did (analyzed our customer data with AI in an afternoon).
3. The headline churn findings, with the real numbers.
4. The blind spot: "silent" high-value customers our current risk score misses.
5. The onboarding-gap finding behind the high-churn region.
6. The competitive gap vs other CCaaS vendors.
7. The MVP we propose — what it is and who it helps.
8. The ask: why we should invest, and the expected payoff.
9. Close on a confident recommendation.

Keep it fully on-brand and lead with outcomes, then the numbers.
```

### Path B — you do NOT have the skill
You'll send **one message** that has two parts stacked together: the brand brief first, then the prompt.

1. Open the file `reference/NICE_BRAND_CHEATSHEET.md` (it's in the lab folder you downloaded — open it in any text editor, or just have Claude read it).
2. Find the section titled **"One-paragraph brief you can paste to Claude"** and copy that paragraph.
3. Paste that paragraph into your Claude message box.
4. Then paste the block below **right underneath it**, in the same message, and press Enter.

```text
Using the brand brief above, create a single self-contained HTML slide deck for NiCE leadership.
One HTML file, no external files, in the NiCE brand colors: charcoal #21212b as the dominant
background, NiCE blue #3694fc as the main accent, warm white #f2f0eb for panels. Use the
Be Vietnam Pro font, sentence case everywhere (never ALL CAPS or Title Case), and one idea per
slide. Spell the company NiCE and the product NiCE CXone. Close on the line "Create a NiCE world."

The story: in one short workshop we took our NiCE CXone customer data, analyzed it with AI, and
found churn insights worth acting on. Walk leadership through it and ask for buy-in.

Cover, one idea per slide:
1. Title + the one-line message.
2. What we did (analyzed our customer data with AI in an afternoon).
3. The headline churn findings, with the real numbers.
4. The blind spot: "silent" high-value customers our current risk score misses.
5. The onboarding-gap finding behind the high-churn region.
6. The competitive gap vs other CCaaS vendors.
7. The MVP we propose — what it is and who it helps.
8. The ask: why we should invest, and the expected payoff.
9. Close on a confident recommendation.

Lead with outcomes, then the numbers.
```

## 👀 What you should expect back
A 9-slide deck, one idea per slide, that reads like a confident story — not a wall of charts. Don't worry if your exact wording or numbers differ a little; Claude is telling *your* data's story, so small differences are normal. Look for:

- A short, punchy title slide with a single one-line message (something like "We can cut churn by acting on what the data already knows").
- The headline numbers stated plainly — your overall churn rate sat around 21%, and customers using NiCE's AI churned far less than those without it.
- A standout slide on the **silent churners** — a small group of healthy-looking, high-value Enterprise accounts whose usage was quietly collapsing while the risk score said they were fine. This is the slide leadership will remember.
- The onboarding-gap story tied to the high-churn region — framed as a fixable cause, not "that region is just bad."
- A clean MVP slide that says what you'd build, who it helps, and why it's small enough to start now.
- An "ask" slide with a clear payoff, and a confident closing line.
- On-brand styling: charcoal background, NiCE blue accents, sentence-case headlines, correct "NiCE CXone" spelling. On Path B, Claude hands you **one HTML file** — save it and double-click it to open the deck in your web browser.

## 💡 Make it better (optional follow-ups)
These are extras. Send any of them as a new message in the same chat, after the deck is built.

Add one strong number to the ask slide.
```text
On the "ask" slide, add one rough payoff estimate: if we recovered even a quarter of the at-risk ARR, what would that be? Show your math simply.
```

Tighten the opening for a CFO.
```text
Rewrite slide 1's one-line message three different ways — one for a CFO, one for a product leader, one for the CEO. Keep each under 12 words.
```

Get a script to go with the slides.
```text
Write a 30-second spoken intro I can say out loud before slide 1, in a warm, confident tone.
```

## 🧯 If something goes wrong
- **"Claude can't find the nice-brand skill."** That's fine — switch to Path B. Open `reference/NICE_BRAND_CHEATSHEET.md`, copy the "One-paragraph brief you can paste to Claude," paste it into your message, then paste the Path B prompt right under it and send.
- **You started a fresh chat, or the deck forgot your numbers (or invented new ones).** Claude only remembers what's in the current conversation. Paste your key results from Steps 2–5 back into the chat — the churn numbers, the silent-churner detail, the onboarding-gap finding, and your MVP idea — then say: "rebuild the deck using these exact numbers."
- **It's not on-brand (wrong colors, ALL CAPS, or it spells the name "Nice" or "NICE").** Reply: "Fix the brand: charcoal #21212b background, NiCE blue #3694fc accents, sentence case only, and spell it 'NiCE CXone'."
- **The HTML deck (Path B) won't open or looks broken.** Reply: "Give me the full deck as one self-contained HTML file with everything inline, no external links." Then save Claude's answer as a file named `deck.html` and double-click it to open in your browser.
- **You want a different feel.** Just ask — "make it punchier," "fewer words per slide," or "more confident on the close." You can iterate as many times as you like; it never costs you anything to try again.

## ➡️ Next
That's it — you took raw data, cleaned it, found a real insight, shaped an MVP, and pitched it to leadership. That's the whole loop, start to finish. Head back to [`README.md`](../README.md) for a recap and ideas on what to try next. Create a NiCE world.

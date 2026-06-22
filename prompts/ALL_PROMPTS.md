# 📋 All prompts in one place

Every copy-paste prompt for the lab, in order. Each is self-contained. Copy the whole grey
block, paste it into Claude, and **attach `data/nice_cxone_churn.csv`** the first time (Steps 1–2).

> Tip: in **Claude.ai** click the 📎 paperclip to upload the CSV. In **Claude Code** just put the
> file in your folder and mention its name — Claude can open it itself.

---

## Step 1 — Look at the data

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

---

## Step 2 — Analyze the data and find the gaps

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

---

## Step 3 — Build a stunning landing page from the data

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

---

## Step 4 — Compare with competitors and propose an MVP

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

---

## Step 5 — Build the MVP prototype (minimal, fake data)

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

---

## Step 6 — Create the management deck (NiCE brand)

**If you have the `nice-brand` skill installed:**

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

**If you do NOT have the skill:** paste the brand brief from
[`reference/NICE_BRAND_CHEATSHEET.md`](../reference/NICE_BRAND_CHEATSHEET.md) along with the same
slide outline, and ask Claude for a single self-contained HTML slide deck in those brand colors,
fonts, and tone.

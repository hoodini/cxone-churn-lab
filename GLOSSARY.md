# Glossary

A friendly, plain-English cheat sheet for everyone in the data + AI workshop. No prior knowledge needed — each term gets a sentence or two. Terms are grouped by topic, and roughly alphabetical within each group.

---

## The Big Idea: Churn

**Churn** — When a customer stops doing business with you (cancels, doesn't renew, or walks away). It's the opposite of keeping a customer happy and on board.

**Churned vs Active** — A simple label for each customer: "active" means they're still a paying customer right now, "churned" means they've already left. Most of our analysis is about spotting which active customers are at risk of becoming churned.

**Churn rate** — The percentage of customers who leave over a set period (say, a year). If 100 customers start the year and 8 cancel, that's an 8% churn rate.

**Churn risk score** — A number (often 0 to 100, or low/medium/high) that estimates how likely a specific customer is to leave soon. Higher score means more worry — it's an early warning, not a certainty.

**Health score** — A single number that sums up how well a customer is doing overall, blending signals like usage, support tickets, and satisfaction. A high health score is good news; a low one is a red flag (and usually pushes the churn risk score up).

---

## NiCE & Contact Centers

**NiCE CXone** — NiCE's cloud platform for running customer service and contact centers. It's the main product the customers in our dataset are using. (Note: the older "Mpower" name is retired — it's just NiCE CXone now.)

**CCaaS** — Short for "Contact Center as a Service." It means the contact center software runs in the cloud as a subscription, instead of being installed and maintained on the company's own servers. NiCE CXone is a CCaaS product.

**Contact center** — The team and technology a company uses to handle customer interactions — phone calls, chats, emails, social messages. Think of it as the modern, multi-channel version of a call center.

**Agent (contact-center agent)** — A person who works in the contact center and actually talks to customers (answers calls, replies to chats, etc.). Not to be confused with an "AI agent" — here it means a human employee.

**Enlighten AI / NiCE AI Models** — NiCE's built-in artificial intelligence that helps contact centers (for example, by analyzing conversations, coaching agents, or automating tasks). It was branded "Enlighten" and is now called "NiCE AI Models" in current branding — our dataset still uses the older "Enlighten" label, so you'll see both.

---

## Seats & Usage

**Seat / Licensed seat / Active seat** — A "seat" is one paid spot for one user (usually one agent). A *licensed seat* is one the customer is paying for; an *active seat* is one actually being used. Paying for 100 but only using 60 means 40 licensed seats are sitting idle.

**Seat utilization** — The share of paid seats that are actually being used (active seats ÷ licensed seats). Low utilization is a warning sign — the customer may feel they're overpaying and start questioning the contract.

**Shelfware** — Software (or seats) a customer paid for but isn't using — it's just "sitting on the shelf." Shelfware is a classic churn risk because customers don't renew things they never got value from.

**Adoption** — How much and how well a customer actually uses the product's features. Strong adoption means they've woven it into their daily work; weak adoption means they bought it but barely touch it.

---

## Money & Contracts

**ARR** — "Annual Recurring Revenue": the predictable subscription money a customer brings in over a year. It's a favorite way to size up how valuable a customer is.

**MRR** — "Monthly Recurring Revenue": the same idea as ARR but measured per month. Roughly, ARR ÷ 12 = MRR.

**Contract type (Monthly / Annual / Multi-Year)** — How long the customer has committed to pay. *Monthly* is the easiest to cancel (higher churn risk), *Annual* locks in a year, and *Multi-Year* commits to several years (lowest churn risk, but a bigger deal to lose).

**Segment (SMB / Mid-Market / Enterprise)** — How we group customers by size. *SMB* = small and medium businesses, *Mid-Market* = mid-sized companies, *Enterprise* = the largest organizations. Each segment tends to behave and churn differently.

---

## Customer Success & Satisfaction

**CSAT** — "Customer Satisfaction" score, usually from a quick survey like "How happy were you with this interaction?" It's typically a percentage or a 1–5 rating; higher is better.

**NPS** — "Net Promoter Score," based on one question: "How likely are you to recommend us?" (0–10). It ranges from -100 to +100 and signals overall loyalty — a low NPS often hints at future churn.

**CSM (Customer Success Manager)** — The person at the vendor whose job is to keep a customer successful and happy so they renew and grow. They watch health scores and step in when churn risk rises.

**QBR** — "Quarterly Business Review": a regular (usually every three months) meeting between the vendor and the customer to review progress, results, and plans. It's a key moment to catch problems before they become churn.

**Onboarding** — The early stage where a new customer gets set up, trained, and running on the product. Good onboarding sets the tone — a rough start often leads to churn later.

**Time to value** — How long it takes a new customer to get real benefit from the product after buying it. Shorter is better; long time-to-value frustrates customers and raises churn risk.

---

## Data & AI Terms

**Data quality** — How clean, accurate, complete, and trustworthy your dataset is. Bad data quality (typos, gaps, duplicates) leads to bad conclusions — "garbage in, garbage out."

**Missing value** — A blank or empty spot in the data where a number or label should be (for example, a customer with no CSAT score recorded). We have to decide whether to fill, ignore, or flag these.

**Outlier** — A data point that sits far outside the normal range — like one customer paying 50x more than everyone else. Outliers can be real, or they can be mistakes, so they're worth a closer look.

**Anomaly** — Something in the data that doesn't fit the expected pattern and looks suspicious or surprising. Anomalies can reveal errors, fraud, or genuinely unusual behavior worth investigating.

**Synthetic data** — Made-up data that's generated to look and behave like real data, without being tied to actual customers. We use it to learn and experiment safely, without exposing anyone's private information.

**MVP** — "Minimum Viable Product": the simplest version of something that still works and proves the idea. In a workshop, your MVP is a basic-but-functional first build, not a polished final product.

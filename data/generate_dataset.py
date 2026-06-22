#!/usr/bin/env python3
"""
NiCE CXone — Synthetic Customer Churn Dataset Generator
=======================================================

Builds a realistic B2B SaaS (CCaaS / contact-center-as-a-service) customer base
for the NiCE CXone platform, with churn modelled as a logistic function of
weighted business drivers PLUS a set of deliberately planted patterns and
anomalies for a discovery workshop.

stdlib only. Deterministic (seeded) so the dataset is reproducible.

Run:  python3 generate_dataset.py
Out:  nice_cxone_churn.csv
"""

import csv
import math
import random
from datetime import date, timedelta

SEED = 20260622
random.seed(SEED)

N_ACCOUNTS = 1000
TODAY = date(2026, 6, 22)

# ----------------------------------------------------------------------------
# Reference dimensions
# ----------------------------------------------------------------------------

REGIONS = {
    # region: (weight, countries, planted_churn_modifier)
    "North America": (0.40, ["United States", "Canada"], 0.0),
    "EMEA":          (0.27, ["United Kingdom", "Germany", "France", "Israel", "UAE", "South Africa"], 0.0),
    "APAC":          (0.20, ["Australia", "India", "Singapore", "Japan", "Philippines"], 0.85),  # PLANTED: APAC churns more
    "LATAM":         (0.13, ["Brazil", "Mexico", "Argentina"], 0.15),
}

INDUSTRIES = {
    # industry: (weight, planted_churn_modifier)
    "Financial Services": (0.16, -0.30),   # sticky, regulated, deep integrations
    "Healthcare":         (0.12, -0.20),
    "Retail":             (0.15,  0.45),    # PLANTED: seasonal seat downsizing -> churn
    "Hospitality":        (0.08,  0.50),    # PLANTED: seasonal
    "Telecom":            (0.10,  0.05),
    "Technology / SaaS":  (0.14, -0.10),
    "Insurance":          (0.09, -0.15),
    "Travel":             (0.06,  0.35),
    "Utilities":          (0.05, -0.10),
    "Public Sector":      (0.05, -0.25),
}

SEGMENTS = {
    # segment: (weight, employee_range, seat_range, arr_per_seat_range, base_churn_mod)
    "SMB":         (0.45, (20, 300),     (8, 60),    (900, 1500),  0.35),
    "Mid-Market":  (0.38, (300, 3000),   (50, 400),  (800, 1300),  0.0),
    "Enterprise":  (0.17, (3000, 90000), (300, 4000),(700, 1100), -0.45),
}

CXONE_MODULES = [
    "ACD (Omnichannel Routing)",
    "IVR / Voice",
    "Workforce Management (WFM)",
    "Quality Management",
    "Interaction Analytics",
    "Digital Channels (Chat/Email/Social)",
    "Feedback Management",
    "Enlighten AI (Copilot / Autopilot)",
    "Performance Management",
    "Recording & Compliance",
]

CSMS = [
    "Dana Levi", "Marcus Reed", "Priya Nair", "Tom Fischer", "Sofia Marin",
    "Kenji Watanabe", "Aisha Khan", "Liam O'Brien", "Noa Cohen", "Diego Alvarez",
    "Unassigned",  # PLANTED: Unassigned book of business churns more
]
# PLANTED: one CSM with a quietly bad book (operational insight)
WEAK_CSM = "Tom Fischer"

COMPANY_PREFIX = [
    "Apex", "Northwind", "Vertex", "Summit", "Meridian", "Cobalt", "Lumen",
    "Pioneer", "Harbor", "Brightline", "Cascade", "Ironwood", "Sterling",
    "Beacon", "Quantum", "Evergreen", "Crimson", "Atlas", "Catalyst", "Nimbus",
    "Granite", "Pinnacle", "Horizon", "Sable", "Maple", "Solstice", "Vantage",
    "Keystone", "Onyx", "Aurora", "Falcon", "Delta", "Sequoia", "Tidewater",
]
COMPANY_SUFFIX = [
    "Holdings", "Group", "Retail Co", "Financial", "Health Systems", "Logistics",
    "Communications", "Solutions", "Industries", "Partners", "Bank", "Airlines",
    "Insurance", "Hospitality", "Networks", "Energy", "Labs", "Stores",
    "Telecom", "Services", "Brands", "Mutual", "Resorts", "Digital",
]

CHURN_REASONS = [
    "Price / budget cuts",
    "Switched to competitor",
    "Low adoption / shelfware",
    "Poor support experience",
    "Reliability / outages",
    "Seasonal seat downsizing",
    "M&A / consolidation",
    "Champion left",
]

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def weighted_choice(d):
    """d: {key: (weight, ...)} or {key: weight}. Returns a key by weight."""
    keys = list(d.keys())
    weights = [v[0] if isinstance(v, tuple) else v for v in d.values()]
    return random.choices(keys, weights=weights, k=1)[0]

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def logistic(z):
    return 1.0 / (1.0 + math.exp(-z))

def rnd(a, b, nd=2):
    return round(random.uniform(a, b), nd)

# ----------------------------------------------------------------------------
# Generate one account
# ----------------------------------------------------------------------------

def make_account(i):
    acct = {}
    acct["account_id"] = f"CX-{100000 + i}"
    acct["company_name"] = f"{random.choice(COMPANY_PREFIX)} {random.choice(COMPANY_SUFFIX)}"

    region = weighted_choice(REGIONS)
    _, countries, region_mod = REGIONS[region]
    acct["region"] = region
    acct["country"] = random.choice(countries)

    industry = weighted_choice(INDUSTRIES)
    _, industry_mod = INDUSTRIES[industry]
    acct["industry"] = industry

    segment = weighted_choice(SEGMENTS)
    _, emp_range, seat_range, arr_per_seat, seg_mod = SEGMENTS[segment]
    acct["segment"] = segment
    acct["employees"] = random.randint(*emp_range)

    # Contract
    contract_type = random.choices(
        ["Monthly", "Annual", "Multi-Year"],
        weights=[0.18, 0.55, 0.27] if segment != "Enterprise" else [0.05, 0.45, 0.50],
        k=1,
    )[0]
    acct["contract_type"] = contract_type

    # Tenure & dates
    max_tenure = {"Monthly": 30, "Annual": 60, "Multi-Year": 84}[contract_type]
    tenure = random.randint(2, max_tenure)
    start = TODAY - timedelta(days=int(tenure * 30.4))
    acct["contract_start_date"] = start.isoformat()
    acct["tenure_months"] = tenure

    # Seats & ARR
    licensed = random.randint(*seat_range)
    # Utilization centered ~0.72 but heavy left tail (shelfware risk)
    util = clamp(random.gauss(0.72, 0.18), 0.05, 1.0)
    active = max(1, round(licensed * util))
    acct["licensed_seats"] = licensed
    acct["active_seats"] = active
    acct["seat_utilization"] = round(active / licensed, 3)
    per_seat = random.uniform(*arr_per_seat)
    acct["arr_usd"] = int(round(licensed * per_seat, -2))

    # Module adoption — Enterprise/FinServ adopt more; SMB fewer
    base_modules = {"SMB": 2.4, "Mid-Market": 3.6, "Enterprise": 5.2}[segment]
    n_modules = clamp(int(round(random.gauss(base_modules, 1.6))), 1, len(CXONE_MODULES))
    modules = random.sample(CXONE_MODULES, n_modules)
    acct["modules_adopted"] = n_modules
    acct["modules_list"] = "; ".join(sorted(modules))
    uses_enlighten = "Enlighten AI (Copilot / Autopilot)" in modules
    acct["uses_enlighten_ai"] = "Yes" if uses_enlighten else "No"
    acct["digital_channels_enabled"] = "Yes" if "Digital Channels (Chat/Email/Social)" in modules else "No"

    # Engagement / usage
    acct["monthly_interactions"] = int(active * random.uniform(180, 650))
    acct["digital_channel_share_pct"] = rnd(2, 65, 1) if acct["digital_channels_enabled"] == "Yes" else rnd(0, 8, 1)
    acct["avg_login_freq_per_week"] = rnd(0.3, 6.5, 1)
    # usage trend: most flat/slightly up, some declining
    acct["usage_trend_pct"] = round(random.gauss(2, 14), 1)

    # Onboarding — PLANTED: APAC has worse onboarding completion (the real cause of APAC churn)
    onboard_p = 0.86
    if region == "APAC":
        onboard_p = 0.58
    if segment == "SMB":
        onboard_p -= 0.08
    acct["onboarding_completed"] = "Yes" if random.random() < onboard_p else "No"
    acct["time_to_value_days"] = random.randint(18, 70) if acct["onboarding_completed"] == "Yes" else random.randint(70, 200)

    # CSM coverage — Enterprise rarely unassigned
    if segment == "Enterprise":
        csm = random.choice([c for c in CSMS if c != "Unassigned"])
    else:
        csm = random.choices(CSMS, weights=[8]*10 + [14], k=1)[0]  # Unassigned over-weighted for non-Ent
    acct["csm_assigned"] = csm
    acct["qbrs_last_12m"] = 0 if csm == "Unassigned" else random.choices([0,1,2,3,4], weights=[2,3,4,3,2])[0]

    # Support / reliability
    acct["support_tickets_90d"] = max(0, int(random.gauss(11, 7)))
    acct["critical_incidents_12m"] = random.choices([0,1,2,3,4], weights=[55,25,12,5,3])[0]
    acct["avg_csat"] = round(clamp(random.gauss(4.0, 0.6), 1.0, 5.0), 2)
    acct["nps_last"] = random.randint(0, 10)

    # Commercial
    acct["discount_pct"] = rnd(0, 35, 1)
    # price increase at renewal — a chunk got hit with >15%
    pi = random.choices([0, random.uniform(2,8), random.uniform(8,15), random.uniform(15,28)],
                        weights=[40, 30, 18, 12], k=1)[0]
    acct["price_increase_at_renewal_pct"] = round(pi, 1)
    acct["days_payment_overdue"] = random.choices([0, random.randint(1,15), random.randint(16,45), random.randint(46,120)],
                                                  weights=[68, 17, 9, 6], k=1)[0]
    acct["expansion_arr_usd"] = int(round(acct["arr_usd"] * random.choice([0,0,0,0.05,0.1,0.2,-0.1]), -2))

    # ------------------------------------------------------------------
    # PLANTED PATTERN: "silent enterprise churners"
    # High CSAT, low tickets (look healthy on surface) but usage collapsing.
    # ~9% of Enterprise. The current risk model (below) will MISS them.
    # ------------------------------------------------------------------
    silent = False
    if segment == "Enterprise" and random.random() < 0.09:
        silent = True
        acct["avg_csat"] = round(clamp(random.gauss(4.4, 0.3), 3.8, 5.0), 2)
        acct["support_tickets_90d"] = random.randint(0, 4)
        acct["usage_trend_pct"] = round(random.uniform(-58, -28), 1)
        acct["avg_login_freq_per_week"] = rnd(0.3, 1.6, 1)
        acct["seat_utilization"] = round(clamp(random.gauss(0.38, 0.08), 0.1, 0.6), 3)
        acct["active_seats"] = max(1, round(licensed * acct["seat_utilization"]))
    acct["_silent_churner"] = silent  # internal flag, dropped before CSV

    # ------------------------------------------------------------------
    # Churn probability (logistic over standardized drivers)
    # ------------------------------------------------------------------
    z = -2.05  # intercept tuned for ~20% overall churn
    z += (0.70 - acct["seat_utilization"]) * 2.6
    z += (3.6 - acct["avg_csat"]) * 0.55
    z += (acct["support_tickets_90d"] - 11) / 9.0 * 0.45
    z += (3 - acct["modules_adopted"]) * 0.28
    z += -acct["usage_trend_pct"] / 22.0
    z += {"Monthly": 0.85, "Annual": 0.0, "Multi-Year": -0.75}[contract_type]
    z += -0.6 if uses_enlighten else 0.0
    z += 0.7 if acct["onboarding_completed"] == "No" else 0.0
    z += 0.5 if acct["qbrs_last_12m"] == 0 else (-0.1 * acct["qbrs_last_12m"])
    z += 0.25 * acct["critical_incidents_12m"]
    z += 0.55 if acct["days_payment_overdue"] > 30 else 0.0
    z += (0.85 if segment == "SMB" else 0.5) if acct["price_increase_at_renewal_pct"] > 15 else 0.0
    z += 0.6 if csm == "Unassigned" else 0.0
    z += 0.5 if csm == WEAK_CSM else 0.0
    z += -0.04 * acct["qbrs_last_12m"]
    z += 0.45 if tenure < 12 else (-0.4 if tenure > 40 else 0.0)
    z += region_mod
    z += industry_mod
    z += seg_mod
    if silent:
        z += 2.4  # they really do leave
    z += random.gauss(0, 0.55)  # irreducible noise

    p_churn = logistic(z)
    churned = random.random() < p_churn
    acct["status"] = "Churned" if churned else "Active"
    acct["churned"] = 1 if churned else 0

    if churned:
        # churn happened sometime in the tenure window, weighted toward recent
        days_ago = random.randint(5, min(540, int(tenure * 30.4)))
        churn_dt = TODAY - timedelta(days=days_ago)
        acct["churn_date"] = churn_dt.isoformat()
        # reason driven by dominant signal
        if silent:
            reason = "Low adoption / shelfware"
        elif acct["price_increase_at_renewal_pct"] > 15:
            reason = "Price / budget cuts"
        elif acct["critical_incidents_12m"] >= 2:
            reason = "Reliability / outages"
        elif acct["support_tickets_90d"] > 18 or acct["avg_csat"] < 3.2:
            reason = "Poor support experience"
        elif acct["seat_utilization"] < 0.4:
            reason = "Low adoption / shelfware"
        elif industry in ("Retail", "Hospitality", "Travel") and random.random() < 0.5:
            reason = "Seasonal seat downsizing"
        else:
            reason = random.choice(CHURN_REASONS)
        acct["churn_reason"] = reason
    else:
        acct["churn_date"] = ""
        acct["churn_reason"] = ""

    # ------------------------------------------------------------------
    # churn_risk_score (0-100): the platform's CURRENT risk model.
    # NOTE: by design it keys off satisfaction/support/tenure/commercial
    # signals but IGNORES behavioural usage decay -> it under-scores the
    # silent enterprise churners. That blind spot is a planted insight.
    # ------------------------------------------------------------------
    r = 18.0
    r += (0.70 - acct["seat_utilization"]) * 35
    r += (3.8 - acct["avg_csat"]) * 9
    r += acct["support_tickets_90d"] * 0.9
    r += 14 if acct["onboarding_completed"] == "No" else 0
    r += 10 if contract_type == "Monthly" else 0
    r += 8 if acct["days_payment_overdue"] > 30 else 0
    r += 8 if acct["price_increase_at_renewal_pct"] > 15 else 0
    r += 6 * acct["critical_incidents_12m"]
    r += 9 if csm == "Unassigned" else 0
    r += random.gauss(0, 6)
    acct["churn_risk_score"] = int(clamp(round(r), 1, 99))

    # health score = inverse-ish, also blind to usage decay (mirror of risk)
    acct["health_score"] = int(clamp(round(100 - acct["churn_risk_score"] + random.gauss(0, 5)), 1, 100))

    return acct


# ----------------------------------------------------------------------------
# Build dataset
# ----------------------------------------------------------------------------

accounts = [make_account(i) for i in range(N_ACCOUNTS)]

# ----------------------------------------------------------------------------
# Inject deliberate DATA-QUALITY anomalies (for cleaning / anomaly-detection
# part of the workshop). Recorded in FACILITATOR_NOTES.md.
# ----------------------------------------------------------------------------
def pick(n):
    return random.sample(range(N_ACCOUNTS), n)

for idx in pick(3):  # impossible utilization (active > licensed)
    accounts[idx]["active_seats"] = accounts[idx]["licensed_seats"] + random.randint(5, 40)
    accounts[idx]["seat_utilization"] = round(accounts[idx]["active_seats"] / accounts[idx]["licensed_seats"], 3)

for idx in pick(2):  # negative / impossible tenure
    accounts[idx]["tenure_months"] = -random.randint(1, 6)

for idx in pick(4):  # CSAT recorded as 0 == missing coded as zero
    accounts[idx]["avg_csat"] = 0

for idx in pick(3):  # blank region
    accounts[idx]["region"] = ""

for idx in pick(2):  # blank industry
    accounts[idx]["industry"] = ""

for idx in pick(2):  # ARR = 0 (billing gap)
    accounts[idx]["arr_usd"] = 0

for idx in pick(1):  # absurd ARR outlier
    accounts[idx]["arr_usd"] = 99999999

for idx in pick(1):  # future contract start date
    accounts[idx]["contract_start_date"] = (TODAY + timedelta(days=120)).isoformat()

# one exact duplicate account_id (deduping exercise)
dup = dict(accounts[random.randrange(N_ACCOUNTS)])
accounts.append(dup)

# ----------------------------------------------------------------------------
# Write CSV
# ----------------------------------------------------------------------------
FIELDS = [
    "account_id", "company_name", "industry", "region", "country", "segment",
    "employees", "contract_start_date", "tenure_months", "contract_type",
    "arr_usd", "licensed_seats", "active_seats", "seat_utilization",
    "modules_adopted", "modules_list", "uses_enlighten_ai", "digital_channels_enabled",
    "digital_channel_share_pct", "monthly_interactions", "usage_trend_pct",
    "avg_login_freq_per_week", "onboarding_completed", "time_to_value_days",
    "csm_assigned", "qbrs_last_12m", "support_tickets_90d", "critical_incidents_12m",
    "avg_csat", "nps_last", "discount_pct", "price_increase_at_renewal_pct",
    "days_payment_overdue", "expansion_arr_usd", "health_score", "churn_risk_score",
    "status", "churned", "churn_date", "churn_reason",
]

out_path = "/Users/yuvai/Desktop/nice-cxone-churn-workshop/nice_cxone_churn.csv"
with open(out_path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
    w.writeheader()
    for a in accounts:
        w.writerow(a)

# ----------------------------------------------------------------------------
# Print a quick sanity summary
# ----------------------------------------------------------------------------
real = [a for a in accounts]
churn_rate = sum(a["churned"] for a in real) / len(real)
print(f"Rows written: {len(real)}  ->  {out_path}")
print(f"Overall churn rate: {churn_rate:.1%}")

def rate_by(key):
    from collections import defaultdict
    agg = defaultdict(lambda: [0, 0])
    for a in real:
        k = a[key] or "(blank)"
        agg[k][0] += a["churned"]
        agg[k][1] += 1
    return {k: v[0] / v[1] for k, v in sorted(agg.items())}

print("\nChurn by region:")
for k, v in rate_by("region").items():
    print(f"  {k:<16} {v:.1%}")
print("\nChurn by segment:")
for k, v in rate_by("segment").items():
    print(f"  {k:<16} {v:.1%}")
print("\nChurn by contract_type:")
for k, v in rate_by("contract_type").items():
    print(f"  {k:<16} {v:.1%}")

silent = [a for a in real if a.get("_silent_churner")]
silent_churned = sum(a["churned"] for a in silent)
if silent:
    print(f"\nSilent enterprise churners planted: {len(silent)} | churned: {silent_churned} "
          f"| their avg risk_score: {sum(a['churn_risk_score'] for a in silent)/len(silent):.0f} "
          f"(vs overall {sum(a['churn_risk_score'] for a in real)/len(real):.0f})")

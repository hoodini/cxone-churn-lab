# NiCE CXone — Customer Churn Dataset · Data Dictionary

**File:** `nice_cxone_churn.csv` · **Rows:** 1,001 · **Columns:** 40
**Grain:** one row = one NiCE CXone customer account (a company running its contact centre on the platform).
**As-of date:** 2026-06-22. **Synthetic** — no real customers. Reproducible from `generate_dataset.py` (seed 20260622).

This is a blended book of business: ~79% **Active** accounts (each carries a live `churn_risk_score`) and ~21% historical **Churned** accounts (each labelled with a `churn_date` and `churn_reason`). That mix is what makes it useful: learn *why* customers left from the churned set, then act on the at-risk actives.

> Hand this file to Claude alongside the CSV. A model given column definitions reasons about the data; a model given only raw CSV guesses.

---

## Account & firmographics
| Column | Type | Meaning |
|---|---|---|
| `account_id` | string | Unique account key (`CX-1000xx`). *(One duplicate exists on purpose — see anomalies.)* |
| `company_name` | string | Synthetic company name. |
| `industry` | category | Vertical: Financial Services, Healthcare, Retail, Hospitality, Telecom, Technology / SaaS, Insurance, Travel, Utilities, Public Sector. |
| `region` | category | North America, EMEA, APAC, LATAM. |
| `country` | string | Country within the region. |
| `segment` | category | SMB · Mid-Market · Enterprise. |
| `employees` | int | Company headcount. |

## Contract & commercial
| Column | Type | Meaning |
|---|---|---|
| `contract_start_date` | date | When the CXone contract began. |
| `tenure_months` | int | Months as a customer (to churn date if churned, else to as-of date). |
| `contract_type` | category | Monthly · Annual · Multi-Year. |
| `arr_usd` | int | Annual recurring revenue (USD). |
| `discount_pct` | float | Discount off list at last negotiation. |
| `price_increase_at_renewal_pct` | float | Price uplift applied at last renewal (0 = none). |
| `days_payment_overdue` | int | Days the latest invoice is/was overdue (0 = on time). |
| `expansion_arr_usd` | int | Net upsell/downsell ARR in the last year (can be negative). |

## Product adoption & usage
| Column | Type | Meaning |
|---|---|---|
| `licensed_seats` | int | Agent seats contracted. |
| `active_seats` | int | Agent seats actually used. |
| `seat_utilization` | float | `active_seats / licensed_seats` (≤ 1.0 in clean data). Low = shelfware. |
| `modules_adopted` | int | Count of CXone modules in use. |
| `modules_list` | string | Semicolon-separated module names (ACD, IVR, WFM, Quality Management, Interaction Analytics, Digital Channels, Feedback Management, **Enlighten AI**, Performance Management, Recording & Compliance). |
| `uses_enlighten_ai` | Yes/No | Whether Enlighten AI (Copilot/Autopilot) is adopted. |
| `digital_channels_enabled` | Yes/No | Chat/email/social channels live. |
| `digital_channel_share_pct` | float | Share of interactions on digital vs voice. |
| `monthly_interactions` | int | Customer interactions handled per month. |
| `usage_trend_pct` | float | Change in usage last quarter vs prior quarter (negative = declining). |
| `avg_login_freq_per_week` | float | Average agent/admin logins per week. |

## Onboarding, support & relationship
| Column | Type | Meaning |
|---|---|---|
| `onboarding_completed` | Yes/No | Whether onboarding finished. |
| `time_to_value_days` | int | Days from signature to first production value. |
| `csm_assigned` | string | Customer Success Manager (or `Unassigned`). |
| `qbrs_last_12m` | int | Quarterly business reviews held in the last year. |
| `support_tickets_90d` | int | Support tickets opened in the trailing 90 days. |
| `critical_incidents_12m` | int | Sev-1 / outage incidents experienced in 12 months. |
| `avg_csat` | float | Average CSAT, 1–5. *(A few `0` values = "not recorded", not genuine zero — see anomalies.)* |
| `nps_last` | int | Latest relationship NPS response, 0–10. |

## Scores & outcome
| Column | Type | Meaning |
|---|---|---|
| `health_score` | int 1–100 | Platform-computed account health (higher = healthier). |
| `churn_risk_score` | int 1–99 | **The platform's current risk model output** (higher = more at risk). Built from satisfaction / support / tenure / commercial signals. |
| `status` | category | Active · Churned. |
| `churned` | 0/1 | Target label. 1 = the account has left. |
| `churn_date` | date | When they left (blank for Active). |
| `churn_reason` | category | Recorded reason (blank for Active). |

---

## Suggested workshop flow
1. **Profile & clean** — shape, types, missing values, impossible values, duplicates.
2. **Find the churn drivers** — which fields separate Churned from Active? (Try `seat_utilization`, `contract_type`, `usage_trend_pct`, `onboarding_completed`, `uses_enlighten_ai`.)
3. **Segment & anomaly hunt** — churn by region / industry / segment / CSM. Where is it abnormal, and *why*?
4. **Stress-test the risk model** — does `churn_risk_score` actually predict who churned? Find where it fails.
5. **Build the app** — turn the findings into an at-risk-accounts dashboard with prioritised actions.

> Note for the analysis: this is synthetic data with engineered relationships and added noise. Treat correlations as *designed signals to discover*, not real NiCE business facts.

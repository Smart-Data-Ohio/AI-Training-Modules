# Exercise 01: Problem Type Recognition — Solution

These are reference answers. Some scenarios have defensible alternative answers — that's intentional. The reasoning matters more than the label.

---

## Scenario 1: Insurance Claim Estimation

**Problem type:** Regression

**Input features (X):** Vehicle make/model/year, damage type (collision, theft, weather), location, driver age, policy type, photos/descriptions from the initial report, historical claim data for similar incidents.

**Target (Y):** Estimated claim payout amount (a continuous dollar value).

**Why ML?** Claim costs depend on dozens of interacting factors — a fender bender on a 2024 BMW costs very differently than the same damage on a 2015 Honda. The relationships are too complex for a simple formula, and human adjusters are slow because they're essentially doing this estimation manually.

---

## Scenario 2: Fraud Detection at Scale

**Problem type:** Anomaly detection (though binary classification is also defensible)

**Input features (X):** Transaction amount, merchant category, time of day, location, device fingerprint, account age, transaction velocity (how many transactions in the last hour), distance from last transaction.

**Target (Y):** Anomalous vs. normal transaction pattern.

**Why ML?** Fraudsters change tactics constantly. Rule-based systems ("flag anything over $5,000") are easy to circumvent and generate too many false positives. ML can learn subtle patterns across many dimensions simultaneously.

**Why anomaly detection over classification?** With only 0.05% fraud rate, you have far more "normal" examples than "fraud" examples. Anomaly detection works better with highly imbalanced data because it learns "normal" rather than trying to learn both classes equally. That said, if you have good labeled fraud data, a classification model with proper class weighting works too — this is a genuinely ambiguous scenario.

---

## Scenario 3: Employee Attrition

**Problem type:** Classification (binary)

**Input features (X):** Tenure, department, salary band, last promotion date, manager satisfaction score, number of direct reports, hours worked per week, engagement survey scores, peer comparison metrics.

**Target (Y):** Will resign within 6 months (yes/no).

**Why ML?** There's no single rule that predicts attrition. A combination of factors — compensation, engagement, career trajectory, management quality — interact in complex ways. A developer making $120K might stay happily, but the same developer with the same salary and a bad manager might leave.

---

## Scenario 4: Customer Segmentation

**Problem type:** Clustering

**Input features (X):** Purchase frequency, average order value, product categories purchased, recency of last purchase, customer lifetime value, geographic region, channel preference (online vs. in-store).

**Target (Y):** There is no target — clustering discovers groups. The output is cluster assignments (e.g., "Customer A belongs to Cluster 3") that the marketing team then interprets and names ("Cluster 3 = high-value, infrequent buyers").

**Why ML?** The client explicitly said they don't have predefined segments. They want to discover structure. A human could try to segment manually, but with 200,000 customers and dozens of behavioral dimensions, no one can see the natural groupings by eye.

---

## Scenario 5: Predictive Maintenance

**Problem type:** Classification (binary)

**Input features (X):** Sensor readings (temperature, vibration, pressure, RPM), machine age, time since last maintenance, operating hours, environmental conditions, historical failure records for each machine.

**Target (Y):** Will fail within the next N days (yes/no). The "N" depends on how much lead time maintenance needs — typically 7-30 days.

**Why ML?** Machine failures are caused by subtle patterns across multiple sensors over time. A single sensor reading being "high" isn't enough — it's the combination of slightly elevated temperature AND increasing vibration AND the machine being 6 months past maintenance that signals trouble. Rules can't capture these multi-dimensional patterns.

---

## Scenario 6: Legal Document Routing

**Problem type:** Classification (multi-class)

**Input features (X):** Document text content (probably transformed into numerical features via TF-IDF or embeddings), document type (contract, filing, correspondence), sender/source, keywords, document length.

**Target (Y):** Practice area — one of: corporate, litigation, IP, employment, real estate.

**Why ML?** Documents don't always contain obvious keywords. A contract about a patent licensing deal could be IP or corporate depending on context. The paralegal is doing implicit classification using years of experience — ML can learn these same patterns from the routing history.

**Note:** This is also a scenario where an LLM might outperform a classical ML model, since document understanding is a language task. A good consulting answer would discuss both approaches.

---

## Scenario 7: Subscriber Growth Forecasting

**Problem type:** Regression (time series)

**Input features (X):** Historical subscriber counts, seasonal patterns, marketing spend, content release calendar, competitor launches, economic indicators, churn rate trends.

**Target (Y):** Predicted subscriber count for each future quarter (a continuous number).

**Why ML?** Growth depends on many interacting factors — seasonality, content releases, competitive dynamics. Simple linear extrapolation misses these patterns.

**Caveat:** If growth has been genuinely linear for years and there are no major market changes expected, you might not need ML at all. Sometimes a spreadsheet trendline is good enough. The honest answer depends on how complex the growth patterns actually are.

---

## Scenario 8: Patient Vitals Monitoring

**Problem type:** Anomaly detection

**Input features (X):** Heart rate (continuous), blood pressure (continuous), oxygen saturation (continuous), respiratory rate (continuous), historical baseline for each patient, time-series patterns.

**Target (Y):** Anomalous vitals pattern (not a specific diagnosis — just "something unusual is happening").

**Why ML?** The key phrase is "even if no single number is technically out of range." A heart rate of 85 is normal. Blood pressure of 135/85 is borderline but not alarming. But if BOTH shift upward simultaneously in a patient whose baseline is 70 and 120/75, that combination might signal deterioration. Anomaly detection captures multi-dimensional patterns that simple threshold alerts miss.

---

## Scenario 9: Delivery Time Estimation

**Problem type:** Regression

**Input features (X):** Distance, route complexity, current weather, time of day, day of week, package size/weight, vehicle type, driver experience, historical traffic patterns for the route, current traffic conditions.

**Target (Y):** Estimated delivery time in hours (a continuous number).

**Why ML?** Delivery time depends on dozens of factors that interact in complex ways. A 50-mile delivery might take 1 hour on a Sunday morning or 3 hours on a Friday afternoon in rain. Static estimates ("2 business days") don't account for these real-time conditions.

---

## Scenario 10: Loan Portfolio Risk Tiers

**Problem type:** Clustering

**Input features (X):** Loan amount, interest rate, borrower credit score, debt-to-income ratio, loan-to-value ratio, payment history, delinquency count, loan age, property type (if applicable).

**Target (Y):** No predefined target — the model discovers natural risk groupings. The risk team then examines each cluster to understand what makes it distinct (e.g., "Cluster 2 has high LTV ratios and recent delinquencies — call this 'emerging risk'").

**Why ML?** The traditional A/B/C ratings use fixed rules that may not reflect actual portfolio dynamics. Clustering finds structure that might not match the expected categories — maybe there are 4 natural groups, or maybe the traditional "B" tier actually contains two very different risk profiles.

---

## Bonus Question

**Which scenarios might NOT need ML?**

- **Scenario 7 (subscriber forecasting)** is the strongest candidate. If growth is steady and predictable, a trendline in a spreadsheet might be just as good as an ML model. Always check the simple approach first.

- **Scenario 6 (document routing)** could be partially solved with keyword rules. If 80% of litigation documents contain "court" or "filing" and 80% of IP documents contain "patent" or "trademark," a simple keyword classifier might get you 80% accuracy. ML is worth it for the remaining 20% — but sometimes 80% is good enough.

- **Scenario 2 (fraud detection)** currently uses rules. If the fraud team's domain expertise is strong and fraud patterns are stable, enhanced rules might be cheaper and more maintainable than an ML system. The case for ML is strongest when "fraudsters keep changing tactics" — which the scenario does state.

The real consulting skill is knowing when "good enough" is good enough, and when the complexity of ML is justified by the problem's complexity.

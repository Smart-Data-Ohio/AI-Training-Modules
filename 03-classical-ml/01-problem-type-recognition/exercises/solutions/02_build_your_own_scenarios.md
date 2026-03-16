# Exercise 02: Build Your Own Scenarios — Solution

These are example scenarios from realistic consulting contexts. Your scenarios will be different — the goal is to show the level of specificity and reasoning to aim for.

---

## Scenario 1

**Client description:**

"We're a Databricks customer running about 200 data pipelines nightly. Some of them fail unpredictably — could be a schema change in a source system, a resource spike, or a corrupted file. Right now we find out about failures from morning alerts, but by then the downstream dashboards are already wrong. Can you build something that warns us before a pipeline fails?"

**Problem type:** Classification (binary)

**Input features (X):** Pipeline run history (duration trends, row count trends, error frequency), source system change logs, cluster resource utilization, time of day, day of week, number of upstream dependencies, schema drift indicators, data volume deviation from moving average.

**Target (Y):** Will this pipeline run fail (yes/no) — predicted before execution or early in execution.

**Why ML?** Pipeline failures are caused by subtle combinations of factors. A 5% increase in data volume alone isn't a problem, but combined with a recent schema change in the source system and a resource-constrained cluster, it might be. Rules can catch the obvious failures ("data volume doubled"), but the subtle ones require pattern recognition across many dimensions.

---

## Scenario 2

**Client description:**

"We're a state government agency that handles 311 service requests — potholes, noise complaints, abandoned vehicles, water main issues, that kind of thing. We get about 2,000 requests a day across 15 categories. Right now, call center agents classify each request manually, but they miscategorize about 20% of the time. That means wrong department, delayed response, unhappy citizens."

**Problem type:** Classification (multi-class)

**Input features (X):** Request description text (free-form), location/neighborhood, time of submission, submission channel (phone, app, web), caller's description of urgency, historical request patterns for the location.

**Target (Y):** Service category — one of 15 categories (e.g., streets, water, sanitation, noise, zoning, etc.).

**Why ML?** A complaint about "water in my basement" could be plumbing (not the city's problem), a water main break (urgent), or storm drainage (public works). The category depends on context clues in the description that simple keyword matching misses. The 20% error rate from human agents suggests the classification is genuinely ambiguous — ML can learn from the patterns in historically correctly-classified requests.

---

## Scenario 3

**Client description:**

"We run a chain of urgent care clinics. We're trying to figure out optimal staffing levels for each location. Too many staff and we're burning money; too few and wait times spike and patients leave. We need to predict how many patients will walk in on any given day at each location."

**Problem type:** Regression

**Input features (X):** Day of week, month, local weather forecast, flu season indicators (CDC data), nearby events, school calendar (in session vs. break), historical patient volume for the location, local population demographics, nearby competitor clinic openings/closings.

**Target (Y):** Predicted patient count for a given day and location (a continuous number, or rounded to an integer).

**Why ML?** Patient volume depends on many seasonal and contextual factors. Monday volumes are different from Saturday volumes. Flu season shifts patterns. A cold snap increases volume. These interactions are too complex for a staffing spreadsheet that just uses "average for this day of week." ML can capture the multi-factor patterns that drive actual demand.

---

## Self-Check (Applied to These Examples)

- [x] Are the problem types correctly identified? Yes — classification (binary), classification (multi-class), and regression.
- [x] Are the input features specific enough? Yes — each lists concrete, collectible data fields.
- [x] Is the target clearly defined? Yes — binary label, multi-class label, and continuous number respectively.
- [x] Could you explain the "why ML?" to a non-technical client? Yes — each connects to a business pain point.
- [x] At least 2 different problem types? Yes — classification and regression.

# Problem Type Recognition

> Before you pick a tool, you need to know what kind of problem you're solving.

## Prerequisites

- Basic Python programming
- Completion of [01-Foundations](../../01-foundations/) is helpful but not required
- No math or ML background needed

## What You'll Learn

- The four core ML problem types: regression, classification, clustering, and anomaly detection
- How to recognize each one in client conversations (not textbook definitions — real language)
- The fundamental reframing that makes ML click: solving for the function, not the answer
- When a problem is NOT a machine learning problem at all
- How identifying the problem type drives every decision that follows

## The Concept

### The Reframe That Makes ML Click

In every math class you've ever taken, you were given a function and asked to find the answer:

```
f(x) = 2x + 3
What is f(5)?    → 13
```

Machine learning flips this completely. You're given a bunch of inputs and outputs, and your job is to figure out the function:

```
Inputs:  [1,  2,  3,  4,  5 ]
Outputs: [5,  7,  9,  11, 13]
What is f(x)?    → 2x + 3
```

That's the entire idea. A machine learning model is just a program that looks at examples and finds the pattern. The "learning" is the process of figuring out `f(x)`.

Here's why this matters for your work: when a client says "we want AI to predict which customers will leave," they're giving you inputs (customer data) and outputs (left or stayed). Your job is to find the function that connects them. That's ML.

### The Four Problem Types

Every ML problem falls into one of four categories. The category determines which algorithms you'll use, what data you need, and how you'll measure success. Getting this right is the highest-leverage decision in any ML project.

### Regression: "How much? How many? When?"

Regression predicts a **continuous number**. The output is on a sliding scale — it could be 42.7 or 1,247,000 or -3.14.

**The signal in client language:**
- "We want to *predict* the sale price..."
- "Can you *forecast* next quarter's revenue?"
- "How long will this ticket take to resolve?"
- "What will demand look like in December?"

**Examples:**
- Predicting house prices from square footage, bedrooms, and location
- Estimating delivery time based on route, weather, and package size
- Forecasting monthly revenue from historical trends

**What your data looks like:** A spreadsheet where each row is an example and the last column is a number you're trying to predict. The other columns are the inputs (called "features" in ML).

```
Bedrooms  Sqft    Location     Price
3         1800    Dayton       $245,000
4         2400    Columbus     $385,000
2         1100    Cincinnati   $189,000
```

**The metric question:** "How far off are we, on average?" (You'll learn the specific metrics — MAE, RMSE, R² — in the next module.)

### Classification: "Which one? Is it or isn't it?"

Classification predicts a **category**. The output is one of a known, fixed set of labels.

**The signal in client language:**
- "We want to *identify* which customers will churn"
- "Can you *flag* fraudulent transactions?"
- "Is this email spam or not?"
- "Which department should this ticket go to?"

**Two flavors:**
- **Binary classification:** Two possible outputs. Yes/no, spam/not-spam, churned/retained, disease/healthy.
- **Multi-class classification:** Three or more possible outputs. Which department? Which product category? Which priority level?

**Examples:**
- Predicting whether a patient has heart disease (binary)
- Categorizing support tickets into billing, technical, account, or general (multi-class)
- Flagging transactions as legitimate or suspicious (binary)

**What your data looks like:** Same spreadsheet format, but the last column is a label, not a number:

```
Tenure  Monthly_Charges  Contract        Churned
12      $85              month-to-month  Yes
48      $55              two-year        No
3       $92              month-to-month  Yes
```

**The metric question:** "How often are we right?" (And more subtly: "When we're wrong, which kind of wrong is it?" — you'll learn why this matters in Module 02.)

### Clustering: "What groups exist?"

Clustering finds **structure you didn't know was there**. There are no labels — you're not predicting anything. You're discovering.

**The signal in client language:**
- "We want to *understand our customer segments*..."
- "Can you *group* these documents by topic?"
- "Are there natural categories in this data?"
- "We need to *segment* our user base for targeted marketing"

The key difference from classification: in classification, you know the categories upfront (spam vs not-spam). In clustering, the model discovers the categories for you.

**Examples:**
- Grouping customers into segments based on behavior (and then naming those segments after you see them)
- Finding clusters of similar products in an inventory
- Identifying natural groupings in survey responses

**The metric question:** "Do these groups make sense?" (This is fuzzier than regression or classification — often requires human judgment.)

### Anomaly Detection: "What's weird?"

Anomaly detection finds **rare, unusual things** in data. It learns what "normal" looks like and flags anything that doesn't fit.

**The signal in client language:**
- "We need to *detect* fraudulent activity"
- "Can you *flag* unusual patterns in our server logs?"
- "Alert us when something looks *off* in the sensor data"
- "Find the *outliers* in our claims data"

**Why it's its own category:** You might think "isn't fraud detection just classification?" Sometimes it is. But anomaly detection is different because:
- Abnormal events are rare (maybe 0.1% of all data)
- Abnormal events are diverse (fraud doesn't always look the same)
- You often can't label enough examples of "abnormal" to train a classifier

So instead of learning "what does fraud look like?", you learn "what does normal look like?" and flag everything else.

**Examples:**
- Detecting network intrusions by identifying unusual traffic patterns
- Flagging manufacturing defects from sensor readings
- Identifying unusual employee expense reports

**The metric question:** "Are we catching the real anomalies without drowning in false alarms?"

### The Decision Shortcut

When a client describes a problem, run through this:

```
Do you have labeled data (examples with known answers)?
├── YES → Is the answer a number or a category?
│   ├── Number → REGRESSION
│   └── Category → CLASSIFICATION
└── NO → What are you looking for?
    ├── Groups/segments → CLUSTERING
    └── Outliers/weirdness → ANOMALY DETECTION
```

This isn't perfect — some problems are genuinely ambiguous, and some combine multiple types. But it gets you to the right answer 90% of the time, and it gives you a framework for discussing the remaining 10%.

### When It's NOT an ML Problem

Not everything needs machine learning. Sometimes the answer is:

- **A SQL query.** "Show me all customers who haven't logged in for 90 days" isn't a prediction — it's a filter.
- **A business rule.** "Flag any transaction over $10,000" doesn't need a model. That's an `if` statement.
- **A lookup table.** "Map zip codes to sales regions" is a dictionary, not a model.
- **A dashboard.** "We want to understand our sales trends" might just need a chart, not a prediction.

**Rule of thumb:** If a human can write the rules in an afternoon, you don't need ML. Machine learning shines when the pattern is too complex for a human to specify explicitly — when there are too many variables, too many interactions, or the pattern changes over time.

The ability to say "you don't need ML for this" is one of the most valuable things you can tell a client. It saves them money, reduces complexity, and builds trust.

### Problem Type Drives Everything

Once you know the problem type, a cascade of decisions falls into place:

| Decision | Regression | Classification | Clustering | Anomaly Detection |
|----------|-----------|----------------|------------|-------------------|
| Algorithms to try first | Linear regression, Random Forest | Logistic regression, Random Forest | K-means, DBSCAN | Isolation Forest, One-Class SVM |
| Data you need | Features + numeric target | Features + labeled categories | Features only (no labels) | Mostly "normal" examples |
| Success metric | MAE, RMSE, R² | Accuracy, Precision, Recall, F1 | Silhouette score, human judgment | Precision @ recall threshold |
| Client-friendly summary | "We predict X within ±Y" | "We're right Z% of the time" | "We found N natural groups" | "We flag W% of anomalies" |

You don't need to memorize this table. The point is: **the problem type is the first domino.** Get it right, and the rest of the project flows. Get it wrong, and you're building the wrong thing.

## Why This Matters for Consulting

Clients almost never use ML terminology. They say things like:

- "We want AI to analyze our customer data" — that could be any of the four types
- "We need a predictive model" — regression or classification?
- "Can you build something that catches fraud?" — classification or anomaly detection?

Your job in the first client meeting is to translate. The questions you ask to disambiguate the problem type are more valuable than the model you eventually build. Here's why:

**Correctly identifying the problem type is the highest-leverage skill in the first meeting.** If a client says "predict which customers will leave" and you build a regression model that outputs "43.7 churn score," you've built the wrong thing. They wanted classification: will this customer leave or not?

**It's also your credibility builder.** When you can say "that's a binary classification problem — we'll need labeled examples of customers who churned vs. stayed, and we'll evaluate using precision and recall because false negatives are more expensive than false positives in your case" — that's the moment the client decides you know what you're doing.

**And it protects you from scope creep.** If you agree on the problem type upfront and document it, you have a reference point when the client says "can it also do X?" You can evaluate whether X is the same problem type or a new project.

## Exercises

| # | Exercise | Format | Time |
|---|----------|--------|------|
| 01 | [Problem Type Recognition](exercises/starter/01_problem_type_recognition.md) | Classify 10 business scenarios into ML problem types | ~30 min |
| 02 | [Build Your Own Scenarios](exercises/starter/02_build_your_own_scenarios.md) | Write 3 ML problem descriptions from consulting contexts | ~30 min |

## Take It Further

- **scikit-learn's algorithm cheat sheet** — a visual flowchart for choosing algorithms based on your data: [sklearn.org/stable/machine_learning_map](https://scikit-learn.org/stable/machine_learning_map.html)
- **Google's ML Problem Framing course** — free, well-structured, goes deeper on scoping: [developers.google.com/machine-learning/problem-framing](https://developers.google.com/machine-learning/problem-framing)
- **Next module:** [02 — sklearn Essentials](../02-sklearn-essentials/) — now that you know the problem type, learn to build the solution

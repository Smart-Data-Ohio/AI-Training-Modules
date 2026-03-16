# Classical ML for Consultants

> The differentiator. Learn when a client doesn't need an LLM — and how to build what they actually need.

## Who This Is For

Developers who've completed [01-Foundations](../01-foundations/) (or have equivalent experience with AI concepts) and want to learn the other side of machine learning — the kind that runs on a laptop, costs pennies to deploy, and solves the problems that LLMs can't.

No ML experience required. You should be comfortable with Python and not afraid of a little math (we'll build intuition before we get formal).

## Why This Tier Exists

Here's a secret the AI hype cycle doesn't want you to know: most of the "AI" problems clients bring to you aren't LLM problems. They're classical ML problems.

A client says "we want AI to predict which customers will churn." That's not a language model problem — that's a classification model you can build in an afternoon with scikit-learn. It'll run for free on a single server, it won't hallucinate, and it'll give you a straight answer: this customer is 83% likely to leave.

The developers who can recognize these problems and build these solutions — quickly, cheaply, and reliably — are the ones clients keep calling back. That's what this tier teaches you.

## The Modules

Work through these in order. Each module builds on the last.

| # | Module | What You'll Learn | Time |
|---|--------|-------------------|------|
| 01 | [Problem Type Recognition](01-problem-type-recognition/) | How to identify whether a business problem is regression, classification, clustering, or anomaly detection | ~1 hour |
| 02 | [sklearn Essentials](02-sklearn-essentials/) | How to train, evaluate, and compare ML models using scikit-learn | ~3 hours |
| 03 | Neural Nets with Keras | When sklearn isn't enough — intro to neural networks *(coming soon)* | |
| 04 | Decision Framework | Classical ML vs fine-tuning vs RAG vs raw LLM — choosing the right approach *(coming soon)* | |
| 05 | Capstone: Cost Comparison | Same problem solved three ways, with full cost/performance analysis *(coming soon)* | |

**Estimated time for Modules 01–02: ~4 hours**

## The Big Idea

In school math, you're given a function and you solve for the output:

```
f(x) = 2x + 3
f(5) = ?        → 13
```

In machine learning, you flip it. You're given inputs and outputs, and you solve for the function:

```
x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 11, 13]
f(x) = ?        → 2x + 3
```

That's it. That's the whole idea. Everything in this tier is a variation on "given a bunch of examples, find the pattern." The modules teach you how to do that systematically, evaluate whether you found a good pattern, and explain it to a client who doesn't care about the math.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

The exercises use Jupyter notebooks. If you're using VS Code, the built-in notebook support works great. Otherwise:

```bash
jupyter notebook
```

## What's Next

After completing Classical ML, you'll have the foundation to:

- Take on [05-Specialized](../05-specialized/) modules (Databricks, fine-tuning, infrastructure)
- Tackle the [06-Projects](../06-projects/) capstone projects, especially the ML Pipeline Comparison
- Make informed "build vs buy" decisions when clients ask for AI features

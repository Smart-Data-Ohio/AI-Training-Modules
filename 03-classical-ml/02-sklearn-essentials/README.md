# sklearn Essentials

> The Swiss Army knife of machine learning. Learn the pattern once, and you can swap algorithms like Lego bricks.

## Prerequisites

- [Module 01: Problem Type Recognition](../01-problem-type-recognition/) — you should know the difference between regression and classification
- Basic Python — comfortable with functions, loops, and dictionaries
- Willingness to look at data (no math degree required)

## What You'll Learn

- How to explore and prepare data with pandas (enough to be dangerous)
- The sklearn pattern: `fit()`, `predict()`, `score()` — the same three steps for every algorithm
- How to train and evaluate regression models (linear regression, random forest)
- How to train and evaluate classification models (logistic regression, random forest, SVM)
- What cross-validation is and why single train/test splits lie to you
- Which metrics to use and which ones will mislead you

## The Concept

### The sklearn Pattern

Here's the best thing about scikit-learn: **every model works the same way.** Whether you're doing linear regression or a support vector machine, the code follows the same three steps:

```python
from sklearn.ensemble import RandomForestClassifier

# 1. Create the model
model = RandomForestClassifier()

# 2. Train it on your data
model.fit(X_train, y_train)

# 3. Make predictions
predictions = model.predict(X_test)
```

That's it. `fit()`, `predict()`, done. Want to try a different algorithm? Change the import and the constructor. Everything else stays the same.

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

This consistency is why sklearn is the first tool you should reach for. You can try five different algorithms in ten minutes, because the interface never changes.

### Data Preparation: The 80% Nobody Talks About

Here's a secret that experienced ML practitioners know but tutorials skip: **80% of the work is getting the data ready.** The modeling part — the part that feels like "real ML" — is often the easiest step.

Before any model can learn from your data, you need to:

**Handle missing values.** Real data has gaps. A customer didn't fill in their age. A sensor dropped a reading. You have three options:
- Drop the rows (if you have plenty of data and the missing values are random)
- Fill them in with the mean, median, or mode (if the column is important and you can't lose rows)
- Drop the column (if too many values are missing to be useful)

**Encode categorical variables.** ML models work with numbers. "Honda" and "BMW" aren't numbers. You need to convert them. The simplest approach is **one-hot encoding**: create a column for each category (Is_Honda, Is_BMW, etc.) with 1 or 0 values.

```python
# pandas makes this easy
df_encoded = pd.get_dummies(df, columns=["Make", "Colour"])
```

**Scale features (sometimes).** Some algorithms — like SVM and KNN — are sensitive to the scale of your features. If one column ranges from 0-1 and another ranges from 0-100,000, the big numbers will dominate. Scaling puts everything on the same footing.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Not every algorithm needs scaling. Tree-based models (random forest, decision trees) don't care about scale. Linear models and SVMs do. When in doubt, scale — it won't hurt tree-based models, and it might help others.

### Train/Test Split: The Most Important Rule

**Never evaluate a model on the same data you trained it on.** This is the cardinal rule of ML.

Why? Because a model can memorize training data without learning anything useful. A model that memorized every training example would score 100% on the training set and fail miserably on new data. This is called **overfitting**.

The fix is simple: split your data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

Train on 80%, test on 20%. The test set is data the model has never seen — it's your reality check.

The `random_state=42` ensures the split is the same every time you run the code. This matters for reproducibility — if your colleague runs the same code, they'll get the same results.

### Regression Metrics: "How Far Off Are We?"

When you predict a number, you need to know how far off you typically are. There are several ways to measure this:

**MAE (Mean Absolute Error)** — The average of how far off each prediction is, ignoring direction. If your MAE is $2,500 for car prices, it means your predictions are off by $2,500 on average.

```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, predictions)
```

MAE is the most intuitive metric. It's in the same units as your target (dollars, hours, etc.), and it means exactly what it sounds like.

**MSE (Mean Squared Error)** — Same idea, but it squares the errors before averaging. This means big errors get penalized way more than small ones. An error of $10,000 counts 4x more than an error of $5,000 (not 2x).

**RMSE (Root Mean Squared Error)** — The square root of MSE. This brings it back to the original units, like MAE, but with the "big errors matter more" property of MSE. RMSE is the most commonly reported metric.

```python
import numpy as np
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
```

**R² (R-squared)** — The proportion of variance your model explains. Ranges from negative infinity to 1.0.
- **1.0** = perfect predictions
- **0.0** = your model is no better than just predicting the average
- **Negative** = your model is somehow worse than predicting the average (this means something is very wrong)

```python
from sklearn.metrics import r2_score
r2 = r2_score(y_test, predictions)
```

**Which metric should you use?** For client conversations, MAE is easiest to explain ("we're off by $2,500 on average"). For model comparison, RMSE is standard. R² is good for a quick "is this model useful at all?" check.

### Classification Metrics: "How Often Are We Right?"

Classification metrics are trickier than regression metrics, because there are different ways to be wrong.

Take a medical diagnosis model. It can make two kinds of mistakes:
- **False positive:** Says a healthy person has a disease (unnecessary worry, follow-up tests)
- **False negative:** Says a sick person is healthy (missed diagnosis, delayed treatment)

These mistakes have very different consequences. That's why "accuracy" alone isn't enough.

**Accuracy** — Percentage of correct predictions. Simple, intuitive, and **dangerously misleading** for imbalanced data.

If 95% of transactions are legitimate and 5% are fraud, a model that says "not fraud" for everything gets 95% accuracy. It's also completely useless.

**Precision** — Of all the things you predicted as positive, how many actually were? "When you raise an alarm, how often are you right?"

High precision = few false alarms. Important when false alarms are expensive (spam filters, fraud alerts).

**Recall** — Of all the actual positives, how many did you catch? "Of all the real cases, how many did you find?"

High recall = few missed cases. Important when missing a case is dangerous (disease diagnosis, security threats).

**F1 Score** — The harmonic mean of precision and recall. A balanced metric when you care about both. Use this when you don't have a strong reason to prioritize one over the other.

**The precision/recall tradeoff:** You can almost always improve one at the expense of the other. A spam filter with ultra-high precision won't flag your important emails — but it'll let some spam through (lower recall). A medical screening with ultra-high recall will catch every disease case — but it'll also flag many healthy people (lower precision). The right balance depends on the domain.

**Confusion matrix** — The source of truth that shows exactly what your model is doing:

```
                Predicted: No    Predicted: Yes
Actual: No         True Neg       False Pos
Actual: Yes        False Neg      True Pos
```

```python
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
```

### Cross-Validation: Don't Trust a Single Split

A single 80/20 split has a problem: your results depend on which 20% happened to end up in the test set. You might get lucky (easy test examples) or unlucky (hard ones).

**K-fold cross-validation** fixes this by testing on every part of the data:

1. Split data into K equal parts (typically K=5)
2. Train on 4 parts, test on the 5th
3. Rotate: train on a different 4 parts, test on the remaining 1
4. Repeat until every part has been the test set
5. Average the scores

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")
```

If your model scores 90% on one split but 70% on another, the model isn't as reliable as the 90% suggested. Cross-validation gives you the honest picture.

### Choosing an Algorithm

Here's the opinionated guide that nobody writes in textbooks but everyone follows in practice:

**Start with Random Forest.** Seriously. It handles both regression and classification. It doesn't need feature scaling. It's robust to outliers. It rarely overfits badly. It gives you feature importances for free. It's almost always "good enough" to tell you whether your problem is solvable.

```python
# Regression
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Classification
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
```

**Then try the simple baseline.** Linear regression for regression, logistic regression for classification. If the simple model performs nearly as well as random forest, your data has a simple linear pattern and you should use the simpler model (easier to explain, faster to run, less likely to overfit).

**SVM if you need it.** Support Vector Machines can find complex decision boundaries, but they need scaled features and don't give you feature importances. Try them when random forest and logistic regression aren't cutting it.

**Don't hyperparameter tune until you've confirmed the problem is solvable.** If your best model gets 55% accuracy on a binary classification problem, spending three hours tuning hyperparameters won't fix it. The problem is your data or your features, not your hyperparameters. Fix the foundation first.

## Why This Matters for Consulting

sklearn models can run on a laptop, deploy for pennies, and answer questions that clients are currently paying data scientists six figures to answer. Here's why this matters for your work:

**Cost efficiency.** A random forest model in production costs nearly nothing to run. There's no API call, no per-token pricing, no rate limits. Train it once, serve predictions forever. Compare that to an LLM API that charges per request and scales linearly with volume.

**Speed.** sklearn models make predictions in milliseconds. When a client needs real-time scoring — fraud detection at transaction time, dynamic pricing, instant recommendations — classical ML is often the only viable option.

**Explainability.** When a client asks "why did the model flag this customer as high-risk?", you can point to feature importances: "tenure is short, support tickets are high, and they're on a month-to-month contract." Try explaining why GPT-4 made a particular decision.

**The "you don't need an LLM" conversation.** When a client says "we want to use AI to predict customer churn," many vendors will propose an LLM-based solution. You can propose a random forest that costs 1/100th as much, runs 1000x faster, and gives you explainable results. That's a powerful position to be in.

## Exercises

| # | Exercise | What You'll Do | Dataset | Time |
|---|----------|---------------|---------|------|
| 01 | [Data Exploration](exercises/starter/01_data_exploration.ipynb) | Load, clean, and visualize data with pandas | Car sales (missing data) + Heart disease | ~45 min |
| 02 | [Regression](exercises/starter/02_regression.ipynb) | Train and compare regression models, evaluate with MAE/RMSE/R² | Car sales | ~1 hour |
| 03 | [Classification](exercises/starter/03_classification.ipynb) | Train and compare classifiers, understand precision/recall tradeoffs | Heart disease | ~1 hour |

All exercises use Jupyter notebooks. Datasets are in [`../../resources/datasets/`](../../resources/datasets/) — see the [data dictionary](../../resources/datasets/DATA_DICTIONARY.md) for column descriptions.

## Take It Further

- **scikit-learn user guide** — the official docs are excellent, especially the narrative documentation: [scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html)
- **Kaggle Learn: Intro to Machine Learning** — free, fast, hands-on: [kaggle.com/learn/intro-to-machine-learning](https://www.kaggle.com/learn/intro-to-machine-learning)
- **Next module:** [03 — Neural Nets with Keras](../03-neural-nets-with-keras/) — when sklearn isn't enough *(coming soon)*

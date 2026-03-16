# Dataset Reference

This directory contains shared datasets used across multiple training modules. Each dataset is described below with its schema, source, and intended use.

---

## car-sales-extended.csv

**Source:** Adapted from the [KCDC 2022 ML Workshop](https://github.com/CanadaApollo6/KCDC-2022-Materials)
**Rows:** 1,000
**Use case:** Regression exercises — predicting car sale prices from vehicle attributes

| Column | Type | Description | Example Values |
|--------|------|-------------|----------------|
| Make | string | Vehicle manufacturer | Honda, BMW, Toyota, Nissan |
| Colour | string | Paint color | White, Blue, Red, Green, Black |
| Odometer (KM) | integer | Mileage in kilometers | 35431, 192714, 84714 |
| Doors | integer | Number of doors | 3, 4, 5 |
| Price | float | **Target** — sale price in dollars | 15323.0, 19943.0 |

---

## car-sales-extended-missing-data.csv

**Source:** Adapted from the [KCDC 2022 ML Workshop](https://github.com/CanadaApollo6/KCDC-2022-Materials)
**Rows:** 1,000 (with intentional missing values)
**Use case:** Data cleaning and preparation exercises

Same schema as `car-sales-extended.csv`, but with missing values (`NaN`) scattered across columns. Use this dataset to practice handling incomplete data before modeling.

---

## heart-disease.csv

**Source:** UCI Machine Learning Repository, via [KCDC 2022 ML Workshop](https://github.com/CanadaApollo6/KCDC-2022-Materials)
**Rows:** 303
**Use case:** Binary classification — predicting heart disease presence

| Column | Type | Description | Values/Range |
|--------|------|-------------|--------------|
| age | integer | Age in years | 29–77 |
| sex | integer | Biological sex | 0 = female, 1 = male |
| cp | integer | Chest pain type | 0–3 (0 = typical angina, 1 = atypical, 2 = non-anginal, 3 = asymptomatic) |
| trestbps | integer | Resting blood pressure (mm Hg) | 94–200 |
| chol | integer | Serum cholesterol (mg/dl) | 126–564 |
| fbs | integer | Fasting blood sugar > 120 mg/dl | 0 = no, 1 = yes |
| restecg | integer | Resting ECG results | 0 = normal, 1 = ST-T abnormality, 2 = left ventricular hypertrophy |
| thalach | integer | Maximum heart rate achieved | 71–202 |
| exang | integer | Exercise-induced angina | 0 = no, 1 = yes |
| oldpeak | float | ST depression induced by exercise | 0.0–6.2 |
| slope | integer | Slope of peak exercise ST segment | 0 = upsloping, 1 = flat, 2 = downsloping |
| ca | integer | Number of major vessels colored by fluoroscopy | 0–3 |
| thal | integer | Thalassemia type | 1 = normal, 2 = fixed defect, 3 = reversible defect |
| target | integer | **Target** — heart disease diagnosis | 0 = no disease, 1 = disease present |

---

## customer-churn.csv

**Source:** Synthetic (generated for this curriculum)
**Rows:** 1,000
**Use case:** Classification exercises — predicting customer churn in a telecom-style context

| Column | Type | Description | Example Values |
|--------|------|-------------|----------------|
| customer_id | string | Unique customer identifier | CUST-0001, CUST-0042 |
| tenure_months | integer | Months as a customer | 1–72 |
| monthly_charges | float | Monthly bill amount ($) | 18.00–120.00 |
| total_charges | float | Cumulative charges ($) | 18.00–9000.00 |
| contract_type | string | Contract length | month-to-month, one-year, two-year |
| internet_service | string | Internet service type | fiber_optic, dsl, none |
| num_support_tickets | integer | Support tickets filed | 0–12 |
| payment_method | string | How the customer pays | electronic_check, mailed_check, bank_transfer, credit_card |
| churned | integer | **Target** — did the customer leave? | 0 = retained, 1 = churned |

**Built-in patterns** (for exercise discovery): Month-to-month contracts, short tenure, high monthly charges, and many support tickets all correlate with higher churn probability. Overall churn rate is ~29%.

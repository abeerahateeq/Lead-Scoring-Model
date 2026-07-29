# Lead Scoring Model on Synthetic CRM Data

A rule-based lead scoring system built using synthetic CRM data to prioritize potential customers based on business-defined criteria. The project demonstrates the complete data analysis workflow, including exploratory data analysis (EDA), lead scoring, visualization, and an optional machine learning comparison.

---

## Project Overview

Sales teams often receive numerous inbound leads but have limited time to engage with every prospect. This project implements a transparent lead scoring model that evaluates each lead based on three key business factors:

- Budget
- Urgency
- Industry Fit

Each lead receives a numerical score and is categorized as:

- 🔥 Hot Lead
- 🟡 Warm Lead
- 🔵 Cold Lead

An optional Logistic Regression model is also included to compare a machine learning approach with the rule-based scoring system.

---

## Features

- Synthetic CRM dataset generated with Mockaroo
- Exploratory Data Analysis (EDA)
- Rule-based lead scoring
- Lead categorization (Hot, Warm, Cold)
- Data visualizations
- Logistic Regression classifier
- Confusion matrix visualization
- Export of scored dataset

---

## Dataset

The synthetic dataset contains the following attributes:

| Feature | Description |
|----------|-------------|
| Lead ID | Unique identifier |
| Company | Company name |
| Industry | Business sector |
| Budget | Low, Medium, High |
| Urgency | Low, Medium, High |
| Company Size | Small, Medium, Large |
| Country | Company location |
| Email | Contact email |
| Employees | Number of employees |
| Converted | Synthetic conversion label |

---

## Lead Scoring Criteria

The rule-based model assigns points using the following rubric:

| Feature | Maximum Score |
|----------|--------------:|
| Budget | 40 |
| Urgency | 30 |
| Industry Fit | 30 |
| **Total** | **100** |

### Lead Categories

| Score | Category |
|-------:|----------|
| 80–100 | 🔥 Hot Lead |
| 60–79 | 🟡 Warm Lead |
| Below 60 | 🔵 Cold Lead |

---

## Exploratory Data Analysis

The notebook performs:

- Dataset inspection
- Missing value analysis
- Category distribution analysis
- Summary statistics

---

## Visualizations

The project includes:

- Distribution of Lead Scores
- Lead Category Distribution
- Budget Distribution
- Industry Distribution
- Company Size Distribution
- Confusion Matrix (Machine Learning)

---

## Machine Learning Comparison

To complement the rule-based scoring approach, a Logistic Regression classifier predicts whether a lead is likely to convert using:

- Industry
- Budget
- Urgency
- Company Size
- Employees

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

> **Note:** The classifier is trained on a small synthetic dataset. Its purpose is to demonstrate the machine learning workflow rather than provide production-ready predictive performance.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Project Structure

```text
Lead-Scoring-Model/
│
├── Lead_Scoring.ipynb
├── lead_scoring_model.py
├── synthetic_leads.csv
├── scored_leads.csv
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/abeerahateeq/Lead-Scoring-Model.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook
```

---

## Future Improvements

- Train on real CRM datasets
- Experiment with Decision Trees, Random Forest, and XGBoost
- Optimize feature engineering
- Build an interactive Streamlit dashboard
- Deploy as a web application

---

## Business Impact

A transparent lead scoring system enables sales teams to prioritize high-value prospects, respond more quickly to urgent opportunities, and allocate resources more effectively. While this project uses synthetic data for demonstration purposes, the same workflow can be adapted to real CRM datasets with minimal changes.

---

## Author

**Abeerah Ateeq**

Software Engineering Student | AI & Data Science Enthusiast

GitHub: https://github.com/abeerahateeq

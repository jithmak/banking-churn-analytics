# Bank Customer Churn & Retention Analytics

An end-to-end data analytics project investigating customer attrition across 10,000 retail banking accounts. This project identifies core churn drivers, quantifies at-risk deposit revenue, and delivers actionable retention strategies through SQL data pipelines, Python EDA, and an interactive Streamlit dashboard.

---

## Executive Summary & Key Insights
* **Revenue Exposure:** The bank experienced an overall **20.37% churn rate** (2,037 accounts lost), resulting in **$185.59M in lost deposit capital** (24.26% of total bank deposits).
* **Geographic Concentration:** **Germany** exhibits the highest churn rate at **32.44%** (double France and Spain at ~16%), while simultaneously holding the highest average account balances ($119.7k/customer).
* **Pre-Retirement Capital Runoff:** Customers aged **46–60** represent the single highest churn bracket at **51.12%**, causing over **$75M** in deposit outflows.
* **Product Saturation Friction:** Clients with 3 or 4 products showed catastrophic churn rates of **82.71%** and **100.00%**, highlighting severe friction in multi-product onboarding or fee structures.

---

## Tech Stack
* **Cloud Data Warehouse & Querying:** Google BigQuery / SQL
* **Data Processing & EDA:** Python (`pandas`, `numpy`, `matplotlib`, `seaborn`)
* **Interactive Dashboarding:** Streamlit, Plotly Express
* **Environment Management:** macOS Zsh, Virtualenv (`data_env`)

---

## Project Structure
```text
banking-churn-analytics/
├── data/
│   └── raw/
│       └── Bank Customer Churn Prediction.csv
├── sql/
│   └── banking_churn_analysis.sql   # Production SQL queries & CTEs
├── notebooks/
│   └── 01_banking_churn_eda.ipynb   # Exploratory Data Analysis & visual stats
├── app.py                           # Interactive Streamlit web dashboard
├── requirements.txt                 # Project library dependencies
└── README.md                        # Portfolio case study documentation
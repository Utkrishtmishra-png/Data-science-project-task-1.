# Part 1 — Month 1: Python Basics and Data Manipulation

Complete submission for all four weeks, including theory hands-on
exercises, client projects, and concept summaries as required for
Google Classroom submission.

A single running "client" (a small retail chain) ties the month
together: Week 1 explores its daily temperature log, Weeks 2–3 clean
its raw sales export, and Week 4 visualizes what the clean data reveals
— including a real, data-driven finding (ice cream sales track
temperature far more closely than any other product category).

## Folder Structure

```
month1_project/
├── week1/
│   ├── temperature_converter.py          (hands-on)
│   ├── calculator.py                     (hands-on)
│   ├── client_project_avg_temperature.py (client project)
│   ├── daily_temperatures.csv            (input data)
│   └── summary_week1.md
├── week2/
│   ├── data_structures_functions.py      (hands-on)
│   ├── client_project_data_cleaning.py   (client project)
│   ├── customer_orders.csv               (raw input data)
│   ├── customer_orders_cleaned.csv       (cleaned output)
│   └── summary_week2.md
├── week3/
│   ├── numpy_pandas_operations.py        (hands-on)
│   ├── client_project_clean_aggregate.py (client project)
│   ├── retail_sales_data.csv             (raw input data)
│   ├── summary_by_store.csv              (aggregated output)
│   ├── summary_by_category.csv           (aggregated output)
│   └── summary_week3.md
└── week4/
    ├── visualization_script.py           (hands-on)
    ├── client_project_dashboard.py       (client project)
    ├── retail_sales_data.csv             (input data)
    ├── plots/                            (7 individual plots)
    ├── dashboard.png                     (combined dashboard)
    └── summary_week4.md
```

## How to Run

Each script is self-contained — `cd` into its week folder and run it
directly (all scripts assume their CSV inputs are in the same folder):

```bash
cd week1 && python3 temperature_converter.py
cd week1 && python3 client_project_avg_temperature.py

cd week2 && python3 data_structures_functions.py
cd week2 && python3 client_project_data_cleaning.py

cd week3 && python3 numpy_pandas_operations.py
cd week3 && python3 client_project_clean_aggregate.py

cd week4 && python3 visualization_script.py
cd week4 && python3 client_project_dashboard.py
```

Requires: `pandas`, `numpy`, `matplotlib`, `seaborn` (standard
data-science stack). `temperature_converter.py` and `calculator.py`
are interactive (they use `input()`); all other scripts run end-to-end
with no input required.

## Weekly Summaries
See `summary_week1.md` through `summary_week4.md` in each folder for
the concepts learned and results, ready to paste into or attach on
Google Classroom.

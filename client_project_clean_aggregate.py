"""
Week 3 - Client Project: Clean & Aggregate Retail Sales Data
--------------------------------------------------------------
The client's retail_sales_data.csv covers 90 days of daily sales across
4 stores and 5 product categories. It contains:
  - Missing values in units_sold and revenue
  - A handful of exact duplicate rows

This script uses Pandas to remove missing values and duplicates, then
aggregates the clean data to answer the client's core questions:
  - Average units sold and revenue per store
  - Average units sold and revenue per product category
  - Which category benefits most from warmer temperatures
"""

import pandas as pd

INPUT_FILE = "retail_sales_data.csv"
STORE_SUMMARY_FILE = "summary_by_store.csv"
CATEGORY_SUMMARY_FILE = "summary_by_category.csv"


def load_and_clean(filename):
    df = pd.read_csv(filename)

    report = {"original_rows": len(df)}

    # Remove exact duplicate rows
    df = df.drop_duplicates()
    report["after_dedup"] = len(df)

    # Remove rows with missing units_sold or revenue
    df = df.dropna(subset=["units_sold", "revenue"])
    report["after_dropna"] = len(df)

    return df, report


def aggregate_by_store(df):
    return (
        df.groupby("store")
        .agg(
            avg_units_sold=("units_sold", "mean"),
            avg_revenue=("revenue", "mean"),
            total_revenue=("revenue", "sum"),
        )
        .round(2)
        .sort_values("total_revenue", ascending=False)
    )


def aggregate_by_category(df):
    return (
        df.groupby("category")
        .agg(
            avg_units_sold=("units_sold", "mean"),
            avg_revenue=("revenue", "mean"),
            total_revenue=("revenue", "sum"),
        )
        .round(2)
        .sort_values("total_revenue", ascending=False)
    )


def temperature_correlation(df):
    """Correlation between daily temperature and units sold, per category."""
    return (
        df.groupby("category")
        .apply(lambda g: g["temperature_c"].corr(g["units_sold"]))
        .round(3)
        .sort_values(ascending=False)
    )


def main():
    df, report = load_and_clean(INPUT_FILE)

    print("=== Cleaning Report ===")
    print(f"Original rows:        {report['original_rows']}")
    print(f"After removing dupes: {report['after_dedup']}")
    print(f"After dropping NaNs:  {report['after_dropna']}")

    store_summary = aggregate_by_store(df)
    category_summary = aggregate_by_category(df)
    temp_corr = temperature_correlation(df)

    print("\n=== Average Sales by Store ===")
    print(store_summary)

    print("\n=== Average Sales by Category ===")
    print(category_summary)

    print("\n=== Correlation: Temperature vs. Units Sold (by category) ===")
    print(temp_corr)
    print(
        f"\nInsight: '{temp_corr.index[0]}' shows the strongest positive "
        f"relationship with temperature (r = {temp_corr.iloc[0]}), suggesting "
        f"the client should stock more of it as the weather warms up."
    )

    store_summary.to_csv(STORE_SUMMARY_FILE)
    category_summary.to_csv(CATEGORY_SUMMARY_FILE)
    print(f"\nSaved: {STORE_SUMMARY_FILE}, {CATEGORY_SUMMARY_FILE}")


if __name__ == "__main__":
    main()

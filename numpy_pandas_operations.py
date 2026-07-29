"""
Week 3 - Hands-On Exercise: NumPy and Pandas for Data Manipulation
Concepts practiced: NumPy arrays, operations, broadcasting, and
Pandas DataFrames, Series, indexing, and data grouping.
"""

import numpy as np
import pandas as pd


def demo_numpy():
    print("=== NumPy: Arrays, Operations, Broadcasting ===")

    # Creating arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.arange(10, 60, 10)  # [10, 20, 30, 40, 50]
    print(f"a = {a}")
    print(f"b = {b}")

    # Element-wise operations
    print(f"a + b = {a + b}")
    print(f"a * 2 = {a * 2}")
    print(f"a ** 2 = {a ** 2}")

    # Aggregate operations
    print(f"sum(a) = {a.sum()}, mean(a) = {a.mean():.2f}, std(a) = {a.std():.2f}")

    # 2D array (matrix) basics
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatrix:\n{matrix}")
    print(f"Shape: {matrix.shape}")
    print(f"Column sums: {matrix.sum(axis=0)}")
    print(f"Row sums: {matrix.sum(axis=1)}")

    # Broadcasting: applying an operation across mismatched shapes automatically
    print("\n--- Broadcasting ---")
    prices = np.array([10.0, 20.0, 30.0])       # shape (3,)
    tax_rate = 1.08                              # scalar broadcasts to every element
    prices_with_tax = prices * tax_rate
    print(f"Prices: {prices}")
    print(f"Prices with 8% tax (broadcast): {prices_with_tax}")

    # Broadcasting a (3,) row vector against a (2,3) matrix
    discounts = np.array([0.9, 1.0, 0.8])
    discounted_matrix = matrix * discounts
    print(f"Matrix:\n{matrix}\nDiscounts (broadcast across rows): {discounts}")
    print(f"Result:\n{discounted_matrix}")
    print()


def demo_pandas():
    print("=== Pandas: Series, DataFrames, Indexing, Grouping ===")

    # Series: a single labeled column of data
    scores = pd.Series([92, 78, 85, 88], index=["Alice", "Bob", "Chen", "Diego"])
    print("Series:\n", scores)
    print(f"Alice's score (label indexing): {scores['Alice']}")
    print(f"Scores above 80:\n{scores[scores > 80]}")

    # DataFrame: a table of labeled columns
    data = {
        "name": ["Alice", "Bob", "Chen", "Diego"],
        "department": ["Sales", "Sales", "Engineering", "Engineering"],
        "salary": [65000, 58000, 72000, 69000],
    }
    df = pd.DataFrame(data)
    print("\nDataFrame:\n", df)

    # Indexing
    print("\n--- Indexing ---")
    print("Column 'salary':\n", df["salary"])
    print("Row 0 (loc):\n", df.loc[0])
    print("Rows where department == 'Engineering':\n", df[df["department"] == "Engineering"])

    # Grouping
    print("\n--- Grouping ---")
    dept_avg_salary = df.groupby("department")["salary"].mean()
    print("Average salary by department:\n", dept_avg_salary)

    dept_summary = df.groupby("department")["salary"].agg(["mean", "min", "max", "count"])
    print("\nFull salary summary by department:\n", dept_summary)
    print()


if __name__ == "__main__":
    demo_numpy()
    demo_pandas()

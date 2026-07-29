# Week 3 Summary: NumPy and Pandas for Data Manipulation

## Concepts Learned

**NumPy Arrays & Operations**
NumPy's `ndarray` supports fast, vectorized math — `a + b`, `a * 2`,
`a ** 2` all apply element-wise without writing a manual loop.
Aggregate methods like `.sum()`, `.mean()`, `.std()` summarize data in
one call, and 2D arrays support axis-aware operations (`.sum(axis=0)`
for column sums, `axis=1` for row sums).

**Broadcasting**
NumPy automatically "stretches" smaller arrays to match a larger array's
shape during arithmetic, so a single tax rate can be applied to a whole
price array, or a 3-value discount row can be applied across every row
of a matrix — without writing explicit loops.

**Pandas Series & DataFrames**
- A **Series** is a single labeled column (like a dictionary with
  ordered keys/index).
- A **DataFrame** is a table of columns, each a Series, sharing a
  common index.

**Indexing**
`df["column"]` selects a column, `df.loc[row]` selects a row by label,
and boolean masks (`df[df["salary"] > 60000]`) filter rows by condition.

**Grouping**
`df.groupby("column")` splits data into groups, and `.agg([...])` or
`.mean()` computes statistics per group — the core tool for turning raw
rows into a summary table.

## Hands-On Work
`numpy_pandas_operations.py` demonstrates array creation, element-wise
math, aggregation, 2D matrix operations, broadcasting, and the Pandas
Series/DataFrame/indexing/grouping workflow with a small salary dataset.

## Client Project
`client_project_clean_aggregate.py` cleans the client's
`retail_sales_data.csv` (90 days × 4 stores × 5 categories) by removing
duplicate rows and rows with missing `units_sold`/`revenue`, then
aggregates it to answer:

- **Average sales by store** — Uptown leads in total revenue.
- **Average sales by category** — Beverages generate the most total
  revenue; Ice Cream the least (lowest average volume).
- **Temperature correlation** — Ice Cream sales correlate strongly with
  temperature (r = 0.841), far more than any other category, meaning the
  client should plan to stock more of it as the weather warms.

**Cleaning result:** 1,825 raw rows → 1,800 after removing duplicates →
1,711 after dropping rows with missing values.

## Files Submitted
- `numpy_pandas_operations.py`
- `client_project_clean_aggregate.py`
- `retail_sales_data.csv` (raw input data)
- `summary_by_store.csv`, `summary_by_category.csv` (aggregated outputs)
- `summary_week3.md` (this file)

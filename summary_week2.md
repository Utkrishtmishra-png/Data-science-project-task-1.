# Week 2 Summary: Data Structures and Functions

## Concepts Learned

**Core Data Structures**
- **Lists** — ordered, mutable sequences (`fruits.append(...)`).
- **Tuples** — ordered, immutable — good for fixed-shape records like a
  coordinate pair.
- **Dictionaries** — key-value mappings, ideal for labeled records
  (`{"Alice": 92}`).
- **Sets** — unordered collections of unique items — perfect for
  de-duplication and fast membership checks.

**Functions**
Functions package reusable logic (`sum_of_squares`, `filter_even`,
`normalize_name`). Good functions do one thing, take clear inputs, and
return a predictable output.

**Lambda Functions**
Small, anonymous one-line functions (`lambda x: x ** 2`), often used
inline with `map()`, `filter()`, and `sorted(key=...)` when a full
`def` would be overkill.

**Recursion**
A function that calls itself, with a base case to stop it — demonstrated
with `factorial(n)` and `fibonacci(n)`.

**List Comprehension**
A compact way to build a list from a loop + optional condition in one
line: `[n ** 2 for n in numbers if n % 2 == 0]`. Used throughout the
week's exercises for squaring, filtering, and pairing values.

## Hands-On Work
`data_structures_functions.py` walks through each concept above with
runnable, printed examples — including sorting words by length with a
lambda key and generating the first 10 Fibonacci numbers recursively.

## Client Project
`client_project_data_cleaning.py` cleans the client's messy
`customer_orders.csv` export using only core Python:
- **Sets** to detect and drop exact duplicate rows
- **List comprehension** to filter out rows with a missing product
- A helper **function** to normalize inconsistent name formatting
  (extra whitespace, ALL CAPS → Title Case)

**Result on the sample data:** 68 raw rows → 56 cleaned rows (5 dropped
for a missing product, 7 dropped as duplicates), covering 42 unique
customers. Cleaned output saved to `customer_orders_cleaned.csv`.

## Files Submitted
- `data_structures_functions.py`
- `client_project_data_cleaning.py`
- `customer_orders.csv` (raw input data)
- `customer_orders_cleaned.csv` (cleaned output)
- `summary_week2.md` (this file)

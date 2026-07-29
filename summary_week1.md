# Week 1 Summary: Introduction to Python Programming

## Concepts Learned

**Variables & Data Types**
Python variables don't need explicit type declarations — the interpreter infers
type from the assigned value. Core built-in types covered: `int`, `float`,
`str`, `bool`. Type conversion (`int()`, `float()`, `str()`) is used constantly
when handling user input, since `input()` always returns a string.

**Operators**
- Arithmetic: `+ - * / // % **`
- Comparison: `== != < > <= >=`
- Logical: `and`, `or`, `not`

**Input / Output**
`input()` reads a line of text from the user (always as a string).
`print()` writes output, and f-strings (`f"{value:.2f}"`) make formatted
output easy to read.

**Conditional Statements**
`if / elif / else` blocks direct program flow based on conditions — used
throughout the calculator (choosing an operator) and the temperature
converter (choosing a conversion, validating input).

**Loops**
- `while` loops repeat until a condition becomes false — ideal for a menu
  that keeps running until the user chooses to quit.
- `for` loops iterate over a known sequence (e.g., rows of data, a range of
  numbers).
- Input-validation loops (`while True: ... try/except ... break`) are a
  common pattern for robustly getting numeric input from a user.

## Hands-On Work
- `temperature_converter.py` — converts between Celsius, Fahrenheit, and
  Kelvin using a menu-driven loop.
- `calculator.py` — a basic calculator supporting `+ - * / ** %`, with
  input validation and a running count of calculations performed.

## Client Project
`client_project_avg_temperature.py` reads `daily_temperatures.csv` (90 days
of readings) using only core Python (the `csv` module, loops, and
conditionals — no external libraries) and reports:
- Number of days processed
- Average, coldest, and warmest temperature
- A simple hot/mild/cold classification breakdown

**Result on the sample data:** average temperature 12.98°C, coldest day
2026-01-04 (1.9°C), warmest day 2026-03-13 (24.5°C).

## Files Submitted
- `temperature_converter.py`
- `calculator.py`
- `client_project_avg_temperature.py`
- `daily_temperatures.csv` (input data)
- `summary_week1.md` (this file)

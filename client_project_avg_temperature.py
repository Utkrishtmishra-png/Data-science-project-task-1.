"""
Week 1 - Client Project: Average Temperature Processor
-------------------------------------------------------
A small "client" wants a simple script that reads a CSV of daily
temperature readings and reports summary statistics, without using any
external libraries (pandas/NumPy are introduced in Week 3) - only core
Python: file I/O, loops, conditionals, and basic data types.

Input file: daily_temperatures.csv (columns: date, temperature_c)
"""

import csv

INPUT_FILE = "daily_temperatures.csv"


def load_temperatures(filename):
    """Read the CSV file and return a list of (date, temperature) tuples."""
    readings = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row["date"]
            temp = float(row["temperature_c"])
            readings.append((date, temp))
    return readings


def compute_stats(readings):
    """Compute average, min, and max temperature using plain loops."""
    total = 0.0
    count = 0
    min_reading = None
    max_reading = None

    for date, temp in readings:
        total += temp
        count += 1

        if min_reading is None or temp < min_reading[1]:
            min_reading = (date, temp)
        if max_reading is None or temp > max_reading[1]:
            max_reading = (date, temp)

    average = total / count if count > 0 else 0.0
    return average, min_reading, max_reading, count


def classify_day(temp):
    """Simple conditional logic: bucket a temperature into a category."""
    if temp < 5:
        return "Cold"
    elif temp < 15:
        return "Mild"
    else:
        return "Warm"


def main():
    readings = load_temperatures(INPUT_FILE)
    average, min_reading, max_reading, count = compute_stats(readings)

    print("=== Average Temperature Report ===")
    print(f"Days processed: {count}")
    print(f"Average temperature: {average:.2f}°C")
    print(f"Coldest day: {min_reading[0]} ({min_reading[1]}°C)")
    print(f"Warmest day: {max_reading[0]} ({max_reading[1]}°C)")

    # Count how many days fall into each category
    category_counts = {"Cold": 0, "Mild": 0, "Warm": 0}
    for _, temp in readings:
        category = classify_day(temp)
        category_counts[category] += 1

    print("\nDay classification breakdown:")
    for category, cnt in category_counts.items():
        print(f"  {category}: {cnt} day(s)")


if __name__ == "__main__":
    main()

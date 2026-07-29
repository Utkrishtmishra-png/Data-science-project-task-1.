"""
Week 2 - Client Project: Order Data Cleaning
----------------------------------------------
The client's order export (customer_orders.csv) has three common
real-world problems:
  1. Exact duplicate rows (a data-entry glitch re-submitted some orders)
  2. Inconsistent name formatting (extra whitespace, ALL CAPS)
  3. Missing product values on some rows

This script cleans the data using core Python data structures (lists,
dictionaries, sets) and functions/list comprehensions — no external
libraries. It writes a cleaned file and prints a before/after report.
"""

import csv

INPUT_FILE = "customer_orders.csv"
OUTPUT_FILE = "customer_orders_cleaned.csv"


def load_orders(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


def normalize_name(name):
    """Trim whitespace and convert to Title Case for consistency."""
    return name.strip().title()


def clean_orders(orders):
    """
    Clean the order records:
      - normalize customer names
      - drop rows with a missing product
      - remove exact duplicate rows (using a set of seen tuples)
    Returns (cleaned_orders, stats_dict).
    """
    stats = {
        "original_count": len(orders),
        "missing_product_dropped": 0,
        "duplicates_dropped": 0,
    }

    # Step 1: normalize names
    for order in orders:
        order["customer_name"] = normalize_name(order["customer_name"])

    # Step 2: filter out rows with missing product (list comprehension)
    before = len(orders)
    orders = [o for o in orders if o["product"].strip() != ""]
    stats["missing_product_dropped"] = before - len(orders)

    # Step 3: remove exact duplicates using a set to track what we've seen
    seen = set()
    deduped = []
    for order in orders:
        # a tuple of the record's values is hashable, so it can go in a set
        fingerprint = tuple(order.values())
        if fingerprint not in seen:
            seen.add(fingerprint)
            deduped.append(order)
    stats["duplicates_dropped"] = len(orders) - len(deduped)

    stats["final_count"] = len(deduped)
    return deduped, stats


def save_orders(orders, filename):
    if not orders:
        return
    fieldnames = list(orders[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)


def main():
    orders = load_orders(INPUT_FILE)
    cleaned, stats = clean_orders(orders)
    save_orders(cleaned, OUTPUT_FILE)

    print("=== Data Cleaning Report ===")
    print(f"Original rows:            {stats['original_count']}")
    print(f"Dropped (missing product): {stats['missing_product_dropped']}")
    print(f"Dropped (duplicates):      {stats['duplicates_dropped']}")
    print(f"Final rows:                {stats['final_count']}")
    print(f"\nCleaned file written to: {OUTPUT_FILE}")

    # bonus: unique customers, using a set
    unique_customers = {o["customer_name"] for o in cleaned}
    print(f"Unique customers in cleaned data: {len(unique_customers)}")


if __name__ == "__main__":
    main()

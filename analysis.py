import csv
from pathlib import Path


def load_sales():
    path = Path(__file__).resolve().parent / "data" / "sales.csv"
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def display_sales(rows):
    if not rows:
        return

    keys = list(rows[0].keys())
    table = [keys]
    table.extend(
        [str(row.get(key, "")) for key in keys]
        for row in rows
    )
    widths = [
        max(len(row[column]) for row in table)
        for column in range(len(table[0]))
    ]

    for row_index, row in enumerate(table):
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))
        if row_index == 0:
            print("-+-".join("-" * width for width in widths))

def total_revenue(rows):
    total = 0.0
    for row in rows:
        total += int(row["units"]) * float(row["unit_price"])
    return total


def total_units(rows):
    total = 0

    for row in rows:
        units = int(row["units"])
        total += units

    return total


def revenue_for_category(rows, category):
    total = 0.0

    for row in rows:
        if row["category"] == category:
            units = int(row["units"])
            price = float(row["unit_price"])
            total += units * price

    return total


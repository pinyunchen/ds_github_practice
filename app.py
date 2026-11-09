from analysis import load_sales, total_revenue


def main():
    rows = load_sales()
    print("Welcome to sales analysis!")
    print(f"Order lines: {len(rows)}")
    print(f"Total revenue: ${total_revenue(rows):.2f}")


if __name__ == "__main__":
    main()

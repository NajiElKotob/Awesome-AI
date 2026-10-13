import pandas as pd


def get_sales_summary():
    # Load the sales dataset.
    df = pd.read_csv("sales.csv")

    # Calculate revenue and cost for each order line.
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    df["Cost"] = df["Quantity"] * df["UnitCost"]

    # Calculate profit for each order line.
    df["Profit"] = df["Revenue"] - df["Cost"]

    # Aggregate the results.
    total_revenue = df["Revenue"].sum()
    total_cost = df["Cost"].sum()
    total_profit = df["Profit"].sum()

    # Avoid division by zero.
    profit_margin = (
        total_profit / total_revenue * 100
        if total_revenue != 0
        else 0
    )

    # Return structured results.
    return {
        "total_revenue": round(float(total_revenue), 2),
        "total_cost": round(float(total_cost), 2),
        "total_profit": round(float(total_profit), 2),
        "profit_margin_percent": round(float(profit_margin), 2),
    }

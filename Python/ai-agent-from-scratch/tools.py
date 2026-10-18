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


def get_sales_by(group_by, region=None):
    # Revenue and profit per Region, Product or Category,
    # optionally for one region only.
    if group_by not in ["Region", "Product", "Category"]:
        return {"error": f"Cannot group by '{group_by}'. Use Region, Product or Category."}

    df = pd.read_csv("sales.csv")

    if region:
        df = df[df["Region"].str.lower() == region.lower()].copy()
        if df.empty:
            return {"error": f"No sales found for region '{region}'."}

    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    df["Profit"] = df["Revenue"] - df["Quantity"] * df["UnitCost"]

    totals = df.groupby(group_by)[["Revenue", "Profit"]].sum()
    totals = totals.sort_values("Profit", ascending=False)

    return {
        "group_by": group_by,
        "region": region or "All regions",
        "rows": [
            {group_by: name, "revenue": float(row["Revenue"]), "profit": float(row["Profit"])}
            for name, row in totals.iterrows()
        ],
    }


def get_exchange_rate(currency):
    # Dummy tool – fixed rates instead of a real currency API.
    rates = {"EUR": 0.92, "AED": 3.67, "GBP": 0.79}
    code = currency.upper()
    if code not in rates:
        return {"error": f"No rate available for '{currency}'."}
    return {"currency": code, "rate_vs_usd": rates[code]}

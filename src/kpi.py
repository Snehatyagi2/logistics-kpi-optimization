def compute_kpis(df):
    """Compute delivery KPI columns and a compact dashboard dictionary."""
    if df.empty:
        raise ValueError("No valid delivered orders remain after cleaning.")

    df = df.copy()

    df["delivery_time"] = (
        df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["expected_time"] = (
        df["order_estimated_delivery_date"] - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["is_delayed"] = df["delivery_time"] > df["expected_time"]
    df["delay_days"] = (df["delivery_time"] - df["expected_time"]).clip(lower=0)

    kpis = {
        "total_orders": int(len(df)),
        "avg_delivery_time_days": round(df["delivery_time"].mean(), 2),
        "avg_delay_days": round(df["delay_days"].mean(), 2),
        "delay_rate_percent": round(df["is_delayed"].mean() * 100, 2),
        "on_time_rate_percent": round((~df["is_delayed"]).mean() * 100, 2),
    }

    return df, kpis

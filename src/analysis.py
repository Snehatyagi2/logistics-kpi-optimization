def monthly_delay_analysis(df):
    """Return monthly delayed-order percentage as a timestamp-indexed series."""
    df = df.copy()
    df["month"] = df["order_purchase_timestamp"].dt.to_period("M").dt.to_timestamp()
    monthly_delay = df.groupby("month")["is_delayed"].mean().mul(100)
    return monthly_delay.rename("delay_rate_percent")

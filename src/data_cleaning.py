import pandas as pd


DATE_COLUMNS = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


def clean_orders(df):
    """Normalize order dates and keep records that can support delivery KPIs."""
    df = df.copy()

    for column in DATE_COLUMNS:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    df = df.dropna(subset=DATE_COLUMNS)
    df = df.drop_duplicates(subset=["order_id"])
    df = df.sort_values("order_purchase_timestamp").reset_index(drop=True)

    return df

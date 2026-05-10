from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError


REQUIRED_ORDER_COLUMNS = {
    "order_id",
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
}


def load_orders(path):
    """Load the Olist orders CSV and validate the columns used by the app."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Orders dataset not found: {csv_path}")
    if csv_path.stat().st_size == 0:
        raise ValueError(f"Orders dataset is empty: {csv_path}")

    try:
        df = pd.read_csv(csv_path)
    except EmptyDataError as exc:
        raise ValueError(f"Orders dataset has no readable columns: {csv_path}") from exc

    missing_columns = REQUIRED_ORDER_COLUMNS.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Orders dataset is missing required column(s): {missing}")

    return df

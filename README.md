# KPI Optimization and Route Efficiency

This project computes delivery performance KPIs from an Olist-style orders CSV and plots the monthly delayed-order trend.

## Run

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run with the bundled sample data:

```powershell
python -m src.main --data data/sample_orders.csv --save-plot reports/monthly_delay.png --no-show
```

Run with the full dataset after adding data to `data/olist_orders_dataset.csv`:

```powershell
python -m src.main --data data/olist_orders_dataset.csv
```

## Required Columns

The orders CSV must include:

- `order_id`
- `order_purchase_timestamp`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

## Outputs

The app prints:

- total orders
- average delivery time in days
- average delay days
- delay rate percentage
- on-time rate percentage

It can also save a monthly delay trend chart with `--save-plot`.

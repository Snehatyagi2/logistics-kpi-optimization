import argparse
from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.data_loader import load_orders
from src.data_cleaning import clean_orders
from src.kpi import compute_kpis
from src.analysis import monthly_delay_analysis
from src.visualization import plot_dashboard


DEFAULT_DATASET = Path("data") / "olist_orders_dataset.csv"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute delivery KPIs and monthly delay trends for Olist orders."
    )
    parser.add_argument("--data", default=DEFAULT_DATASET, help="Path to orders CSV.")
    parser.add_argument(
        "--save-plot",
        help="Optional path for saving the dashboard chart, for example reports/dashboard.png.",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Do not open an interactive chart window.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    df = load_orders(args.data)
    df = clean_orders(df)
    df, kpis = compute_kpis(df)

    print("KPI Dashboard:")
    for name, value in kpis.items():
        print(f"- {name}: {value}")

    monthly_delay = monthly_delay_analysis(df)
    plot_dashboard(df, kpis, monthly_delay, output_path=args.save_plot, show=not args.no_show)
    if args.save_plot:
        print(f"Saved dashboard chart to {args.save_plot}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)

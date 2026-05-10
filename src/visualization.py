import matplotlib.pyplot as plt
from pathlib import Path


def plot_dashboard(df, kpis, monthly_delay, output_path=None, show=True):
    """Plot the delivery KPI dashboard and optionally save it to disk."""
    monthly_delivery = (
        df.set_index("order_purchase_timestamp")["delivery_time"]
        .resample("ME")
        .mean()
    )

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    monthly_delay.plot(ax=axes[0, 0], marker="o", linewidth=2, color="#2563eb")
    axes[0, 0].set_title("Monthly Delay Trend")
    axes[0, 0].set_ylabel("Delay Rate (%)")
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].bar(
        ["On Time", "Delayed"],
        [kpis["on_time_rate_percent"], kpis["delay_rate_percent"]],
        color=["#16a34a", "#dc2626"],
    )
    axes[0, 1].set_title("On-Time vs Delayed Orders")
    axes[0, 1].set_ylabel("Orders (%)")
    axes[0, 1].set_ylim(0, 100)

    monthly_delivery.plot(ax=axes[1, 0], marker="o", linewidth=2, color="#7c3aed")
    axes[1, 0].set_title("Average Delivery Time by Month")
    axes[1, 0].set_ylabel("Days")
    axes[1, 0].set_xlabel("Month")
    axes[1, 0].grid(True, alpha=0.3)

    delayed_orders = df.loc[df["is_delayed"], "delay_days"]
    axes[1, 1].hist(delayed_orders, bins=30, color="#f97316", edgecolor="white")
    axes[1, 1].set_title("Delay Days Distribution")
    axes[1, 1].set_ylabel("Orders")
    axes[1, 1].set_xlabel("Delay Days")

    fig.suptitle("Delivery KPI Dashboard", fontsize=16)
    fig.autofmt_xdate()
    fig.tight_layout()

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)

    return fig


def plot_monthly_delay(monthly_delay, output_path=None, show=True):
    """Plot monthly delay trend and optionally save it to disk."""
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_delay.plot(ax=ax, marker="o", linewidth=2)
    ax.set_title("Monthly Delay Trend")
    ax.set_ylabel("Delay Rate (%)")
    ax.set_xlabel("Month")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150)
    if show:
        plt.show()
    else:
        plt.close(fig)

    return fig

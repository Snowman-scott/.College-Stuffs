from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

file_path = "theme_park_ticket_sales.csv"
df = pd.read_csv(file_path, index_col=0)

df_t = df.T

if "Date" in df.columns:
    df_t["Date"] = pd.to_datetime(df_t["Date"], errors="coerce")
    df_t.set_index("Date", inplace=True)
else:
    df_t.index = pd.to_datetime(df_t.index, errors="coerce")


df_t = df_t.dropna(axis=0, how="any")

numeric_cols = df_t.select_dtypes(include="number").columns
highest_date = df_t["Total"].idxmax()
highest_date = pd.to_datetime(highest_date)  # type: ignore
highest_sales = df_t.loc[highest_date]

print("=" * 25)
print("HIGHEST SALES DAY REPORT")
print("=" * 25)
print(f"Date: {highest_date.strftime('%m/%d/%Y')}")
print(f"Total Sales: {highest_sales.get('Total', 0):.0f} tickets\n")
print("Breakdown by Ticket Type:")
print("-" * 40)

for ticket_type in numeric_cols:
    if ticket_type != "Total":
        sales = highest_sales[ticket_type]
        percentage = (
            (sales / highest_sales["Total"]) * 100 if highest_sales["Total"] > 0 else 0
        )
        print(f"{ticket_type:15} {sales:6.0f} tickets  ({percentage:5.1f}%)")

print("=" * 40)

ticket_totals = df.drop(columns=["Total"]).select_dtypes(include="number").sum()

plt.figure(figsize=(10, 6))
ticket_totals.plot(kind="bar", color="steelblue")
plt.title("Total Sales by Ticket Type", fontsize=14, fontweight="bold")
plt.xlabel("Ticket Type")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
for column in numeric_cols:
    if column != "Total":
        plt.plot(df.index, df[column], marker="x", label=column, linewidth=2)

plt.plot(
    df.index,
    df["Total"],
    marker="s",
    label="Total",
    linewidth=3,
    linestyle="--",
    color="red",
)
plt.title("Ticket Sales Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend(loc="best")
plt.xticks(rotation=45, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

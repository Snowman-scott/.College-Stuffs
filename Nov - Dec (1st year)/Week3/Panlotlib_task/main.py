from functools import total_ordering

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("theme_park_ticket_sales.csv", index_col=0)

df_T = df.T

print(df_T)


def date_with_Highest_sales():
    total_sales_per_day = df_T.sum(axis=1)
    date_w_Hi_sales = total_sales_per_day.idxmax()
    Sorted_data_ye = total_sales_per_day.sort_values(ascending=False)
    print("---Total Tickets Sold Per Day---")
    print(Sorted_data_ye)
    print(f"Date With Highest sales: {date_w_Hi_sales}")
    print(f"Total sales on that date: {total_sales_per_day[date_w_Hi_sales]}")


def total_sales_of_each_T_Type():
    total_sales_per_T_Type = df_T.sum(axis=0)
    plt.figure(figsize=(10, 6))
    total_sales_per_T_Type.plot(kind="bar")
    plt.title("Total Sales by ticket Type")
    plt.xlabel("Ticket type")
    plt.ylabel("Total Sold")
    plt.xticks(rotation=45)
    plt.tight_layout()


def line_for_sales_over_time_pd():
    df_T["Total"] = df_T.sum(axis=1)

    df_T.plot(kind="line", figsize=(12, 6))

    plt.title("Ticket Sales Over Time", fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend(loc="best")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


date_with_Highest_sales()
total_sales_of_each_T_Type()
line_for_sales_over_time_pd()

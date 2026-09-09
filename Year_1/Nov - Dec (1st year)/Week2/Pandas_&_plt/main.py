import os

import matplotlib.pyplot as plt
import pandas as pd


def clear():
    os.system("cls" if os.name == "nt" else "clear")


df = pd.read_csv("theme_park_rides.csv")


def avrg_wait_times():
    avrg_wait_times = round(df.groupby("ride_name")["wait_time_minutes"].mean(), 2)

    df2 = avrg_wait_times.reset_index()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(df2["ride_name"], df2["wait_time_minutes"])
    plt.xlabel("Ride name")
    plt.ylabel("Wait Time for Ride")
    plt.title("Ride wait times")
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{df2['wait_time_minutes'].iloc[i]}",
            ha="center",
            va="bottom",
        )
    plt.show()


avrg_wait_times()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("WeatherData.csv", index_col=0)

print(df)


def avrg_temp_and_precipitation():
    avg_temp = df["Temperature (C)"].mean()
    avg_precip = df["Precipitation (mm)"].mean()
    print(f"Average Temperature: {avg_temp:.2f}°C")
    print(f"Average Precipitation: {avg_precip:.2f}mm")


def date_with_hi_and_lowest_temps_and_precip():
    max_temp_date = df["Temperature (C)"].idxmax()
    min_temp_date = df["Temperature (C)"].idxmin()
    max_precip_date = df["Precipitation (mm)"].idxmax()
    min_precip_date = df["Precipitation (mm)"].idxmin()
    print(f"Date with Highest Temperature: {max_temp_date}")
    print(f"Date with Lowest Temperature: {min_temp_date}")
    print(f"Date with Highest Precipitation: {max_precip_date}")
    print(f"Date with Lowest Precipitation: {min_precip_date}")


# Create graphs that show the trends and patterns over time for both the temperature and precipitation, you will need to decide on the most suitable graph for the scenario
#
def graph_temp_and_precip_over_time():
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Temperature (C)"], label="Temperature (C)")
    plt.plot(df.index, df["Precipitation (mm)"], label="Precipitation (mm)")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Temperature and Precipitation Over Time")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()


avrg_temp_and_precipitation()
date_with_hi_and_lowest_temps_and_precip()
graph_temp_and_precip_over_time()

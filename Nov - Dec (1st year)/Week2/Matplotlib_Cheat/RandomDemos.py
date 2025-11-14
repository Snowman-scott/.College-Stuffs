import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("theme_park_rides.csv")

# print(df.to_string(index = False))

averageWaitTimes = round(df.groupby("ride_name")["wait_time_minutes"].mean(), 2)

df2 = averageWaitTimes.reset_index()

print(df2.to_string(index=False))

plt.bar(df2["ride_name"], df2["wait_time_minutes"])
plt.title("Average Wait Time for each Ride")
plt.xlabel("Ride")
plt.ylabel("Wait Time")
plt.grid()
plt.show()


df = pd.read_csv("theme_park_times.csv")

print(df.to_String(index=False))
# Converts data passed into function to datetime
df["visit_timestamp"] = pd.to_datetime(df["visit_timestamp"])

# creatrs two new collumns, called date and time, and stores them date and time data seperatly
df["date"] = df["visit_timestamp"].dt.date
df["time"] = df["visit_timestamp"].dt.time

# built-in function to order values sp the graph dosnet plot incorrectly
df2 = df.sort_values("visit_timestamp")

areas = df["areas"].unique()

Lines = []

times_to_plot = []
for time in df["time"]:
    times_to_plot.append(str(time))
big_line = plt.plot(times_to_plot, df["number_of_people_visited"], lable="All")

for area in areas:
    line_to_plot = df[df["area"] == area]
    times_to_plot = []
    for time in line_to_plot["time"]:
        times_to_plot.append(str(time))
    plt.plot(
        line_to_plot["visit_timestamp"],
        line_to_plot["number_of_people_visited"],
        lable=area,
    )

line1 = big_line(0)
line1.remove()

plt.xticks(rotation=90)
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# Line Chart Practice

df = pd.read_csv("theme_park_times.csv")

# print(df.to_string(index=False))

# Convert data passed into function to datetime (usually from a string)
df["visit_timestamp"] = pd.to_datetime(df["visit_timestamp"])

# Creates two new columns, called date and time, and stores the datetime data separately
df["date"] = df["visit_timestamp"].dt.date
df["time"] = df["visit_timestamp"].dt.time

# Built-in function to order values so the graph doesn't plot incorrectly
df = df.sort_values("visit_timestamp")

# Groups the Data into the seperate areas
areas = df["area"].unique()

# We create a blank list to append the times to
timesToPlot = []
# We then loop through the time column to pull allthe times out and put them into the list
for time in df["time"]:
    timesToPlot.append(str(time))
# We then plot the line graph in a variable so we can delete lines later
bigLine = plt.plot(timesToPlot, df["number_of_people_visited"], label="All")

# We then loop through the Areas plotting the line graph
for area in areas:
    lineToPlot = df[
        df["area"] == area
    ]  # This puts the data into a variable so we can plot it
    print(lineToPlot)
    timesToPlot = []  # We create a blank list to append the times to
    for time in lineToPlot[
        "time"
    ]:  # And loop through the times to put them into the list
        timesToPlot.append(str(time))
    plt.plot(
        timesToPlot, lineToPlot["number_of_people_visited"], label=area
    )  # And plot the line graph

l = bigLine.pop(0)  # We remove the line graph from the list so we can delete it
l.remove()  # We remove the line graph from the list so we can delete it

plt.xticks(rotation=90)  # We rotate the x-axis labels for better readability
plt.show()  # Finally we show the graph

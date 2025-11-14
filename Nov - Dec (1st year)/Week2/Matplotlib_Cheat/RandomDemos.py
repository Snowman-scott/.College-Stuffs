import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("theme_park_rides.csv")

#print(df.to_string(index = False))

averageWaitTimes = round(df.groupby("ride_name")["wait_time_minutes"].mean(), 2)

df2 = averageWaitTimes.reset_index()

print(df2.to_string(index=False))

plt.bar(df2["ride_name"], df2["wait_time_minutes"])
plt.title("Average Wait Time for each Ride")
plt.xlabel("Ride")
plt.ylabel("Wait Time")
plt.grid()
plt.show()




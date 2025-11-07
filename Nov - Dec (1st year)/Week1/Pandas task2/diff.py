import pandas as pd

# Imports data
df = pd.read_csv("random_data.csv")

#Sorts the data into its country name and score for country
groupdata = df.groupby("Country")["Score"]

# Adds all the scores up
groupTotal = groupdata.sum()

print(groupTotal)

#This takes grouped data and turns it back int a data frame
df2 = groupTotal.reset_index()

print(df2)

# Min and Max values
print(f"Min score: {df2["Score"].min()}")
print(f"Max score: {df2["Score"].max()}")
print(df2["Score"].idxmin())
print(df2["Score"].idxmax())

Lowscoreindex = df2["Score"].idxmin()
Highscoreindex = df2["Score"].idxmax()

# iloc
def ilocs():
    print(f"The country with the lowest total score was: {df2["Country"].iloc[Lowscoreindex]}")
    print(f"The country with the highest total score was: {df2["Country"].iloc[Highscoreindex]}")

ilocs()
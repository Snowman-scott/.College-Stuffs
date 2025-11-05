import pandas as pd
import os
#cd 'Nov - Dec (1st year)'\Week1\Pandas task1
os.system("cls")

def blank():
    for x in range(2):
        print(" ")

SeriesData = [0,1,2,3,4,5,[6,8]]
Series = pd.Series(SeriesData)
print(Series)
blank()

data = {
    'Calories' : [420,380,390],
    'Duration' : [50,40,45]
}
df = pd.DataFrame(data)
print(df)
blank()

df2 = pd.read_csv("st.csv")
print(df2)
blank()

vo300 = []
for index, row in df2.iterrows():
    if row["speed"] > 300:
        vo300.append(index)

# Create empty DataFrame with correct columns
df3 = pd.DataFrame(columns=["speed", "time"])  # Match your CSV column names

# Add rows where speed > 300
for rowindex in vo300:
    df3.loc[len(df3)] = df2.loc[rowindex]  # Use .loc with the actual index

print("df3:")
print(df3)
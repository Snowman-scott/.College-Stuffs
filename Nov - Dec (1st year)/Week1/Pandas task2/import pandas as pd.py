import pandas as pd
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

df = pd.read_csv("random_data.csv")

USA = []
UK = []
Australia = []
Germany = []
Canada = []

def Country_sort():
    for index, row in df.iterrows():
        if row["Country"] == "USA":
            USA.append(index)
        elif row["Country"] == "UK":
            UK.append(index)
        elif row["Country"] == "Australia":
            Australia.append(index)
        elif row["Country"] == "Germany":
            Germany.append(index)
        elif row["Country"] == "Canada":
            Canada.append(index)
        else:
            print("Something went Wrong with sorting the rows into Country groups")

Country_sort()
print(USA)
print(UK)
print(Australia)
print(Germany)
print(Canada)
#def score_strip():
    #for index, row in 
import pandas as pd
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

df = pd.read_csv("random_data.csv")

USA = []
USA_rounded = []
UK = []
UK_rounded = []
Australia = []
Australia_rounded = []
Germany = []
Germany_rounded = []
Canada = []
Canada_rounded = []

def Country_sort():
    for index, row in df.iterrows():
        if row["Country"] == "USA":
            USA.append(row["Score"])
            USA_rounded.append(round(row["Score"]))
        elif row["Country"] == "UK":
            UK.append(row["Score"])
            UK_rounded.append(round(row["Score"]))
        elif row["Country"] == "Australia":
            Australia.append(row["Score"])
            Australia_rounded.append(round(row["Score"]))
        elif row["Country"] == "Germany":
            Germany.append(row["Score"])
            Germany_rounded.append(round(row["Score"]))
        elif row["Country"] == "Canada":
            Canada.append(row["Score"])
            Canada_rounded.append(round(row["Score"]))
        else:
            print("Something went Wrong with sorting the rows into Country groups")

def mean(country_list):
    x = 0
    avg = 0
    for x in range(len(country_list)):
        avg = avg + country_list[x]
    avg = avg / len(country_list)
    return avg

def print_mean():
    print("The mean Score for each country is: \n")
    print(f"USA: {mean(USA)}\n")
    print(f"UK: {mean(UK)}\n")
    print(f"Australia: {mean(Australia)}\n")
    print(f"Germany: {mean(Germany)}\n")
    print(f"Canada: {mean(Canada)}\n")

def print_mean_rounded():
    print("The mean Score for each country is: \n")
    print(f"USA: {mean(USA_rounded)}\n")
    print(f"UK: {mean(UK_rounded)}\n")
    print(f"Australia: {mean(Australia_rounded)}\n")
    print(f"Germany: {mean(Germany_rounded)}\n")
    print(f"Canada: {mean(Canada_rounded)}\n")

def mode(num_list):
    frequency = {}
    for num in num_list:
        frequency[num] = frequency.get(num, 0) + 1
    max_count = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_count]
    return modes if len(modes) < len(num_list) else "No mode"

def print_mode():
    print("\n \n")
    print("The Mode Score for each country is: \n")
    print(f"USA: {mode(USA)}\n")
    print(f"UK: {mode(UK)}\n")
    print(f"Australia: {mode(Australia)}\n")
    print(f"Germany: {mode(Germany)}\n")
    print(f"Canada: {mode(Canada)}\n")

def print_mode_rounded():
    print("\n \n")
    print("The Mode Score for each country is: \n")
    print(f"USA: {mode(USA_rounded)}\n")
    print(f"UK: {mode(UK_rounded)}\n")
    print(f"Australia: {mode(Australia_rounded)}\n")
    print(f"Germany: {mode(Germany_rounded)}\n")
    print(f"Canada: {mode(Canada_rounded)}\n")

def median(data):
    if not data:
        raise ValueError("Dataset cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[(n-1)//2]
    else:
        return (sorted_data[n//2-1]+sorted_data[n//2])/2

def print_median():
    print("\n \n")
    print("The Median Score for each country is: \n")
    print(f"USA: {median(USA)}\n")
    print(f"UK: {median(UK)}\n")
    print(f"Australia: {median(Australia)}\n")
    print(f"Germany: {median(Germany)}\n")
    print(f"Canada: {median(Canada)}\n")

def print_median_rounded():
    print("\n \n")
    print("The Median Score for each country is: \n")
    print(f"USA: {median(USA_rounded)}\n")
    print(f"UK: {median(UK_rounded)}\n")
    print(f"Australia: {median(Australia_rounded)}\n")
    print(f"Germany: {median(Germany_rounded)}\n")
    print(f"Canada: {median(Canada_rounded)}\n")

def main():
    Country_sort()
    clear()
    print("____NORMAL SECTION____")
    print_mean()
    print_mode()
    print_median()
    print("\n \n \n")
    print("____ROUNDED SECTION____")
    print_mean_rounded()
    print_mode_rounded()
    print_median_rounded()


if __name__ == "__main__":
    main()
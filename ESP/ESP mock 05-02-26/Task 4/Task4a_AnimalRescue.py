import os
import subprocess

import matplotlib.pyplot as plt
import pandas as pd


def clear_terminal():
    """Clear terminal on Windows, Mac, and Linux"""
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def main_menu():
    flag = True

    while flag:
        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Type of post interaction Data")
        print("### 3. Time Of day post interaction Data")

        choice = input("Enter your number selction here: ")

        try:
            int(choice)
        except:
            clear_terminal()
            print("Sorry, you did not enter a valid option \n")
            flag = True
        else:
            if choice in ["1", "2", "3"]:
                flag = False
            else:
                clear_terminal()
                print("Please enter a number show in the menu\n \n")
                flag = True

    return choice


def average_menu():
    flag = True
    clear_terminal()

    while flag:
        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")
        print("### 2. Average number of Shares")
        print("### 3. Average number of Comments")

        choice = input("Enter your number selction here: ")

        try:
            int(choice)
        except:
            clear_terminal()
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            if choice in ["1", "2", "3"]:
                print("Choice accepted!")
                flag = False
            else:
                clear_terminal()
                print("Please enter a number show in the menu\n \n")
                flag = True

    return choice


def convert_avg_men_coice(avg_men_choice):
    if avg_men_choice == "1":
        avg_choice = "Likes"
    elif avg_men_choice == "2":
        avg_choice = "Shares"
    else:
        avg_choice = "Comments"

    return avg_choice


def get_avg_data(avg_choice):
    df = pd.read_csv("Task4a_data.csv")
    extract = df.groupby(["Date"], as_index=False)[avg_choice].mean()
    extract_no_index = extract.to_string(index=False)

    clear_terminal()
    print(
        "Here is the average number of {} each day during the campaign:".format(
            avg_choice
        ),
        "\n \n \n \n",
    )
    return extract_no_index


def post_type_interactions():
    df = pd.read_csv("Task4a_data.csv")  # Reading csv for data
    extract = df.groupby(["Post Type"], as_index=False)[
        ["Likes", "Shares", "Comments"]
    ].sum()  # Using pandas to filter data
    extract["Total"] = extract[["Likes", "Shares", "Comments"]].sum(
        axis=1
    )  # Data filtering
    extract = extract.sort_values("Total", ascending=True)  # Sorting filtered data
    print(extract, "\n \n \n \n")  # Output data
    plt.figure(figsize=(10, 6))  # Plotting graph
    plt.barh(extract["Post Type"], extract["Total"])  # putting data into the graph
    plt.xlabel("Post type")  # Graph label
    plt.ylabel("Total interactions")  # Graph label
    plt.title("Amount of post interaction Based on Type of post")  # Graph title


def tod_post_type():  # Offering users a choice of bar or line graph to present data
    print("#################################################")
    print("################# Type of graph #################")
    print("#################################################")
    print("")
    print("########### Please select an option #############")
    print("### 1. Bar Graph")
    print("### 2. Line Graph")

    choice = input("Enter your number selection here: ")

    try:
        int(choice)
    except:
        clear_terminal()
        print("Sorry, you did not enter a valid option")
        flag = True
    else:
        if choice in ["1", "2"]:
            print("Choice accepted!")
            flag = False
        else:
            clear_terminal()
            print("Please enter a number show in the menu\n \n")
            flag = True

    return choice


def graph_type_conversion(graph_type_choice):
    if graph_type_choice == "1":
        graph_choice = "bar"
    elif graph_type_choice == "2":
        graph_choice = "line"
    else:
        print("ERROR: graph type choice is not a valid input")

    return graph_choice


def post_pref_at_diff_times_in_day(graph_choice):
    df = pd.read_csv("Task4a_data.csv")  # Reads the Data
    extract = df.groupby(["Time"], as_index=False)[  # Groups all the Time's together
        ["Likes", "Shares", "Comments"]
    ].sum()
    extract["Total"] = extract[["Likes", "Shares", "Comments"]].sum(
        axis=1
    )  # Adds a total column
    extract = extract.set_index("Time")  # Sets index to time
    extract.plot(kind=graph_choice, figsize=(12, 6))

    plt.xlabel("Time period")
    plt.ylabel("Total interactions")
    plt.title("Amount of post interaction Based on Type of post")
    plt.xticks(rotation=45, ha="right")
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3, linewidth=0.7)
    plt.tight_layout()
    plt.show()


main_menu_choice = main_menu()
if main_menu_choice == "1":
    avg_men_choice = average_menu()
    avg_choice = convert_avg_men_coice(avg_men_choice)
    print(get_avg_data(avg_choice))
elif main_menu_choice == "2":
    post_type_interactions()
elif main_menu_choice == "3":
    graph_type_choice = tod_post_type()
    graph_choice = graph_type_conversion(graph_type_choice)
    post_pref_at_diff_times_in_day(graph_choice)

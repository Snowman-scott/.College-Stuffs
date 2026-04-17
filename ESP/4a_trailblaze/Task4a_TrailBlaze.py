import pandas as pd


# Outputs the main menu and checks the user input
# This starter solution currently supports one completed menu option.
def main_menu():
    flag = True

    while flag:
        print("-" * 70)
        print("---------- TrailBlaze Adventure Bookings Module ------------- ")
        print("-" * 70)
        print("")
        print("----------------------- Main Menu -------------------------- ")
        print("1. Total places sold by activity")

        choice = input("Enter your number selection here: ")

        if choice.isdigit():
            flag = False
        else:
            flag = True

        return int(choice)


# Generates submenu of available activity codes and allows user to select an activity
def get_activity_id():

    df = pd.read_csv("Task4a_TrailBlaze_data.csv")

    activity_codes = df["Activity ID"].unique().tolist()

    flag = True

    while flag:
        print("-" * 70)
        print("---------- TrailBlaze Adventure Bookings Module ------------- ")
        print("-" * 70)
        print("")
        print("----------------------- Main Menu -------------------------- ")
        print("Select an activity code:")
        for i in range(len(activity_codes)):
            print(i + 1, " ", activity_codes[i])

        selection = input("Enter your number selection here: ")

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        activity_id = activity_codes[selection - 1]

        print("You have selected activity id:", activity_id)
        return activity_id


# Gets and converts user input from string to date format
def get_date(start_end):

    flag = True

    while flag:
        date = input(
            "Please enter {} date for your date range (DD/MM/YYYY) : ".format(start_end)
        )

        try:
            pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False

        return date


# Extracts data based on activity ID within a user specified date range.
def get_data_by_id_and_date(activity_id, start_date, end_date):
    all_data = pd.read_csv("Task4a_TrailBlaze_data.csv")
    activity_data = all_data.loc[all_data["Activity ID"] == activity_id].copy()

    activity_data["Date"] = pd.to_datetime(
        activity_data["Date"], format="%d/%m/%Y", errors="raise"
    )

    date_range = (
        activity_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")
    ) & (activity_data["Date"] <= pd.to_datetime(end_date, format="%d/%m/%Y"))

    extracted_data = activity_data.loc[date_range]

    return extracted_data


# Generates a total of the number of places sold for the extracted data
def calculate_total_places_sold(date_id, activity_id, start_date, end_date):
    total_places = date_id["Places Sold"].sum()
    print(
        "The total number of places sold for activity {}, between {} and {} was: {}".format(
            activity_id, start_date, end_date, total_places
        )
    )


main_menu_choice = main_menu()

if main_menu_choice == 1:
    activity_id = get_activity_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_id = get_data_by_id_and_date(activity_id, start_date, end_date)
    calculate_total_places_sold(date_id, activity_id, start_date, end_date)

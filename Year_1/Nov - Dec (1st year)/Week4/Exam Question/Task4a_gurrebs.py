import matplotlib.pyplot as plt
import mplcursors
import pandas as pd


# Displays the main menu and collects choice of menu item
def menu():
    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item")
        print("2. ")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)


# Menu item selection form user and validates it
def get_product_choice():
    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = [
            "Nachos",
            "Soup",
            "Burger",
            "Brisket",
            "Ribs",
            "Corn",
            "Fries",
            "Salad",
        ]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice) - 1]
                return item_name


# Displays a calendar view of available dates
def display_date_range():
    df = pd.read_csv("Task4a_data.csv")
    available_dates = df.columns[2:]
    min_date = pd.to_datetime(available_dates[0], dayfirst=True)
    max_date = pd.to_datetime(available_dates[-1], dayfirst=True)

    print("\n" + "=" * 60)
    print(
        f"Available date range: {min_date.strftime('%d/%m/%Y')} - {max_date.strftime('%d/%m/%Y')}"
    )
    print("=" * 60)

    current_date = min_date
    current_month = min_date.month
    current_year = min_date.year

    while current_date <= max_date:
        if current_date.month != current_month or current_date.year != current_year:
            current_month = current_date.month
            current_year = current_date.year

        print(f"\n{current_date.strftime('%B %Y')}")

        days_in_month = []
        temp_date = current_date

        while temp_date.month == current_month and temp_date <= max_date:
            days_in_month.append(temp_date.day)
            temp_date += pd.Timedelta(days=1)

        for i in range(0, len(days_in_month), 10):
            row = days_in_month[i : i + 10]
            print("  ".join(f"{day:2}" for day in row))

        current_date = temp_date

    print("=" * 60 + "\n")


# Gets user input of start of date range
# Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    flag = True

    df = pd.read_csv("Task4a_data.csv")
    available_dates = df.columns[2:]
    min_date = pd.to_datetime(available_dates[0], dayfirst=True)
    max_date = pd.to_datetime(available_dates[-2], dayfirst=True)

    display_date_range()

    while flag:
        start_date = input(
            "Please enter start date for your time range (DD/MM/YYYY) : "
        )

        try:
            date_obj = pd.to_datetime(start_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            if date_obj < min_date or date_obj > max_date:
                print(
                    f"Sorry, the date must be between {min_date.strftime('%d/%m/%Y')} and {max_date.strftime('%d/%m/%Y')}"
                )
                flag = True
            else:
                flag = False

    return start_date


# Gets user input of end of date range
# Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date(start_date):
    flag = True

    df = pd.read_csv("Task4a_data.csv")
    available_dates = df.columns[2:]
    start_date_obj = pd.to_datetime(start_date, dayfirst=True)
    max_date = pd.to_datetime(available_dates[-1], dayfirst=True)

    while flag:
        end_date = input("Please enter end date for your time range (DD/MM/YYYY) : ")

        try:
            date_obj = pd.to_datetime(end_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            if date_obj < start_date_obj:
                print(
                    f"Sorry, the end date must be on or after the start date ({start_date})"
                )
                flag = True
            elif date_obj > max_date:
                print(
                    f"Sorry, the date must be on or before {max_date.strftime('%d/%m/%Y')}"
                )
                flag = True
            else:
                flag = False

    return end_date


# imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv")
    df2 = df1.loc[df1["Menu Item"] == item]
    df3 = df2.loc[:, startdate:enddate]
    df_T = df3.T
    df_T.columns = ["Lunch", "Dinner"]

    df_T.plot(kind="line", figsize=(12, 6), marker="x", markersize=4)

    plt.title("Lunch and Dinner sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3, linewidth=0.7)
    plt.tight_layout()
    plt.show()

    return df3


"""

IGNORE THIS, NOT TO DO WITH MAIN MATPLOTLIB WORK!


def get_selected_item_mplc(item, startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv")
    df2 = df1.loc[df1["Menu Item"] == item]
    df3 = df2.loc[:, startdate:enddate]
    df_T = df3.T
    df_T.columns = ["Lunch", "Dinner"]

    fig, ax = plt.subplots(figsize=(12, 6))

    df_T.plot(kind="line", ax=ax, marker="x", markersize=4)

    cursor = mplcursors.cursor(hover=True)

    @cursor.connect("add")
    def on_add(sel):
        date = df_T.index[int(sel.target[0])]
        values = df_T.loc[date]
        text = f"Date : {date}\n" + "\n".join(
            [f"{col}: {val}" for col, val in values.items()]
        )
        sel.annotations.set_text(text)

        plt.title("Lunch and Dinner sales")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.legend(loc="best")
        plt.grid(True, alpha=0.3, linewidth=0.7)
        plt.tight_layout()
        plt.show()
        """


def item_W_Hi_sales_and_avrg(startdate, enddate):
    df1 = pd.read_csv("Task4a_data.csv")
    df2 = df1.loc[
        :, ["Menu Item", "Service"] + list(df1.loc[:, startdate:enddate].columns)
    ]

    print("\n" + "=" * 80)
    print(f"Sales Statistics for All Menu Items ({startdate} to {enddate})")
    print("=" * 80)

    menu_items = df2["Menu Item"].unique()

    for item in menu_items:
        item_data = df2.loc[df2["Menu Item"] == item]
        item_data_only = item_data.loc[:, startdate:enddate]
        df_T = item_data_only.T
        df_T.columns = ["Lunch", "Dinner"]

        Hi_sold = df_T.max()
        Hi_sold_date = df_T.idxmax()
        avrg_sold = df_T.mean()

        print(f"\n{item}:")
        print(
            f"  Lunch  - Highest sales: {Hi_sold['Lunch']} on {Hi_sold_date['Lunch']}"
        )
        print(f"  Lunch  - Average sales: {avrg_sold['Lunch']:.2f}")
        print(
            f"  Dinner - Highest sales: {Hi_sold['Dinner']} on {Hi_sold_date['Dinner']}"
        )
        print(f"  Dinner - Average sales: {avrg_sold['Dinner']:.2f}")

    print("\n" + "=" * 80 + "\n")


main_menu = menu()
if main_menu == 1:
    item = get_product_choice()
    start_date = get_start_date()
    end_date = get_end_date(start_date)

    item_W_Hi_sales_and_avrg(item, start_date, end_date)
    extracted_data = get_selected_item(item, start_date, end_date)
    extracted_data_mplc = get_selected_item_mplc(item, start_date, end_date)

    print(
        "Here is the sales data for {} between dates {} and {}:".format(
            item, start_date, end_date
        )
    )
    extract_no_index = extracted_data.to_string(index=False)

    print(extract_no_index)
else:
    print("This part of the program is still under development")

import os
import subprocess
import time

import matplotlib.pyplot as plt
import pandas as pd


def clear_terminal():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)


def main_menu():
    flag = True

    clear_terminal()

    while flag:
        print("#################################")
        print("What would you like to do?")
        print("1. Conversion")
        print("2. Value of money")
        print("3. preformance of money")
        print("#################################")

        menu_c = input("\nPlease enter a number between 1 - 3: ")

        try:
            int(menu_c)
        except:
            print("Sorry, you did not enter a valid choice!")
            flag = True
        else:
            if int(menu_c) < 1 or int(menu_c) > 3:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(menu_c)


# The menu() function generates the UI the accepts and validates user choice
def conversion_menu():

    flag = True

    clear_terminal()

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound (GBP) to Australian Dollars (AUD)")
        print("4. Australian Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        print("")
        print("######################################################")

        menu_choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 6:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(menu_choice)


# Gets the short version of the conversion information based on user menu choice
def get_currency(menu_choice):
    currencies = {
        1: "GBP - EUR",
        2: "EUR - GBP",
        3: "GBP - AUD",
        4: "AUD - GBP",
        5: "GBP - JPY",
        6: "JPY - GBP",
    }

    currency = currencies.get(menu_choice)

    print(currency)

    return currency


# The get_conversion_rate function uses pandas to get the latest conversion rate
# Imports a csv file in to a data frame
# Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate(currency):
    df = pd.read_csv("Task4a_RSBX_data.csv")

    print(currency)

    conversion_rate = round(df[currency].iloc[-1], 2)

    return conversion_rate


# Accepts and validates user input for the amount they want to convert
def get_amount_to_convert(currency):

    clear_terminal()

    print("You are converting: ", currency)

    flag = True

    while flag:
        conversion_amount = input("please enter the amount you wish to convert: ")

        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            flag = True
        else:
            return float(conversion_amount)


# Performs the conversion and outputs the final values
def perfom_conversion(currency, conversion_amount, conversion_rate):
    clear_terminal()
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print("You are converting {} in {}".format(conversion_amount, currency[0:3]))
    print("You will receive {} in {}".format(amount_recieved, currency[6:9]))


def value_GBP():
    df = pd.read_csv("Task4a_RSBX_data.csv")
    df2 = df.iloc[-1], 2

def select_currency():

    while True:
        print("1. GBP")
        print("2. EUR")
        print("3. AUD")
        print("4. JPY")

        choice = input("Please enter the number of your choice (1-6): ")

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid choice")
            return True
        else:
            if int(choice) < 1 or int(choice) > 4:
                print("Sorry, you did not enter a valid choice")
                return True
            else:
                return int(choice)


def get_currencyy(choice):
    currencies = {
        1 : "GBP",
        2 : "EUR",
        3 : "AUD",
        4 : "JPY",
    }

    currency = currencies.get(choice)

    return currency

def preformance(currency):
    df = pd.read_csv("Task4a_RSBX_data.csv")
    print(df["Date"])
    start = input("Enter start date: ")
    end = input("Enter end date: ")

    print(currency)

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%y")
    mask = (df["Date"] >= pd.to_datetime(start, format="%d/%m/%Y")) & (
            df["Date"] <= pd.to_datetime(end, format="%d/%m/%Y"))

    filtered = df[mask]
    if filtered.empty:
        print("YOU FUCKED UP NO DATA FOUND")
        return
    plt.figure(figsize=(10, 5))
    plt.plot(filtered['Date'], filtered[currency])
    plt.title('{} Exchange Rate'.format(currency))
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    while True:
        menu_c = main_menu()
        if menu_c == 1:
            print("We are in menu 1 code")
            menu_choice = conversion_menu()

            currency = get_currency(menu_choice)
            conversion_rate = get_conversion_rate(currency)
            conversion_amount = get_amount_to_convert(currency)
            perfom_conversion(currency, conversion_rate, conversion_amount)
            print("\n\n\n\n")
            return False
        elif menu_c == 2:
            value_GBP()
            return False
        elif menu_c == 3:
            choice = select_currency()
            currency = get_currencyy(choice)
            preformance(currency)
        else:
            print("You have done something VERY wrong!")
            time.sleep(1)
            return True


if __name__ == "__main__":
    main()

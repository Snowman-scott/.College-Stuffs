import pandas as pd
import matplotlib.pyplot as plt
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

df = pd.read_csv("sales_data.csv")

def mean_rev():
    revenue = df.groupby("Region")["Revenue"]
    rev_avrg = round(revenue.mean())

    df2 = rev_avrg.reset_index()

    clear()
    print("---Average revenue by region---")
    print(df2.round)
    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df2["Region"], df2["Revenue"])
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.title("Average Revenue by Region")
    print("\n \n")
    print(f"The region that had the highest average revenue is: The {df["Region"].iloc[df2["Revenue"].idxmax()]}")
    print("\n \n")

def total_unit_sold():
    units_sold = df.groupby("Product")["UnitsSold"]
    T_units_sold = units_sold.sum()

    df2 = T_units_sold.reset_index()

    print("---Total units sold per product---")
    print(df2)
    print("\n")
    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df2["Product"], df2["UnitsSold"])
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.title("Total Units Sold by Product")
    plt.show()
    print("\n \n")
    print(f"The product that sold the most units is: {df2["Product"].iloc[df2["UnitsSold"].idxmax()]}")
    print("\n \n")

def salesperson_ranking():
    salesperson_rev = df.groupby("Salesperson")["Revenue"].sum()
    salesperson_rank = salesperson_rev.rank(method='dense', ascending=False)
    salesperson_rank_alt = sorted(salesperson_rev)
    df2 = salesperson_rank.reset_index()
    df2.columns = ["Salesperson", "Rank"]
    df2 = df2.sort_values("Rank")

    print("---Salesperson Ranking based on Revenue---")
    print(df2)
    print("\n \n")
    print(f"The pesrson who has generated the most revenue overall is: {df2["Salesperson"].iloc[df2["Rank"].idxmax()]} \nWith a revenue of: {salesperson_rank_alt[len(salesperson_rank_alt)-1]}")
    print("\n \n")

def Rev_and_unit_sold_by_region_and_product():
    region_and_product = df.groupby(["Region", "Product"])[["Revenue", "UnitsSold"]].sum()
    df2 = region_and_product.reset_index()

    top_prod_for_region = df2.groupby("Region")["UnitsSold"].idxmax()
    top_prodcts = df2.loc[top_prod_for_region]

    print("---Revenue and units sold by Region and product---")
    print(df2)
    print("\n \n")
    print("---Best preforming product in each region (By units sold)---")
    print(top_prodcts)

mean_rev()
total_unit_sold()
salesperson_ranking()
Rev_and_unit_sold_by_region_and_product()
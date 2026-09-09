import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv("nintendo_game_sales.csv")

# Display basic info
print("=" * 60)
print("NINTENDO GAME SALES ANALYSIS")
print("=" * 60)

# ============================================================
# TRENDS AND PATTERNS OVER TIME
# ============================================================
print("\n" + "=" * 60)
print("TRENDS AND PATTERNS OVER TIME")
print("=" * 60)

# Group by release year to see trends
yearly_stats = (
    df.groupby("ReleaseYear")
    .agg(
        {
            "UnitsSold_Millions": ["sum", "mean", "count"],
            "Revenue_USD_Millions": ["sum", "mean"],
        }
    )
    .round(2)
)

yearly_stats.columns = [
    "Total_Units",
    "Avg_Units",
    "Num_Games",
    "Total_Revenue",
    "Avg_Revenue",
]
print("\nYearly Sales Summary:")
print(yearly_stats)

# Units Sold Trends
print("\n--- Units Sold Trends ---")
print(
    f"Year with highest total units sold: {yearly_stats['Total_Units'].idxmax()} ({yearly_stats['Total_Units'].max():.1f}M units)"
)
print(
    f"Year with lowest total units sold: {yearly_stats['Total_Units'].idxmin()} ({yearly_stats['Total_Units'].min():.1f}M units)"
)
print(
    f"Year with highest average units per game: {yearly_stats['Avg_Units'].idxmax()} ({yearly_stats['Avg_Units'].max():.2f}M units)"
)

# Revenue Trends
print("\n--- Revenue Trends ---")
print(
    f"Year with highest total revenue: {yearly_stats['Total_Revenue'].idxmax()} (${yearly_stats['Total_Revenue'].max():.1f}M)"
)
print(
    f"Year with lowest total revenue: {yearly_stats['Total_Revenue'].idxmin()} (${yearly_stats['Total_Revenue'].min():.1f}M)"
)
print(
    f"Year with highest average revenue per game: {yearly_stats['Avg_Revenue'].idxmax()} (${yearly_stats['Avg_Revenue'].max():.2f}M)"
)

# ============================================================
# HIGHEST AND LOWEST PERFORMING GAMES
# ============================================================
print("\n" + "=" * 60)
print("HIGHEST AND LOWEST PERFORMING GAMES")
print("=" * 60)

# Most units sold
max_units = df.loc[df["UnitsSold_Millions"].idxmax()]
print(f"\n--- MOST UNITS SOLD ---")
print(f"Game: {max_units['Title']}")
print(f"Units Sold: {max_units['UnitsSold_Millions']}M")
print(f"Revenue: ${max_units['Revenue_USD_Millions']}M")
print(f"Release Year: {max_units['ReleaseYear']}")
print(f"Franchise: {max_units['Franchise']}")

# Least units sold
min_units = df.loc[df["UnitsSold_Millions"].idxmin()]
print(f"\n--- LEAST UNITS SOLD ---")
print(f"Game: {min_units['Title']}")
print(f"Units Sold: {min_units['UnitsSold_Millions']}M")
print(f"Revenue: ${min_units['Revenue_USD_Millions']}M")
print(f"Release Year: {min_units['ReleaseYear']}")
print(f"Franchise: {min_units['Franchise']}")

# Most revenue
max_revenue = df.loc[df["Revenue_USD_Millions"].idxmax()]
print(f"\n--- HIGHEST REVENUE ---")
print(f"Game: {max_revenue['Title']}")
print(f"Revenue: ${max_revenue['Revenue_USD_Millions']}M")
print(f"Units Sold: {max_revenue['UnitsSold_Millions']}M")
print(f"Release Year: {max_revenue['ReleaseYear']}")
print(f"Franchise: {max_revenue['Franchise']}")

# Least revenue
min_revenue = df.loc[df["Revenue_USD_Millions"].idxmin()]
print(f"\n--- LOWEST REVENUE ---")
print(f"Game: {min_revenue['Title']}")
print(f"Revenue: ${min_revenue['Revenue_USD_Millions']}M")
print(f"Units Sold: {min_revenue['UnitsSold_Millions']}M")
print(f"Release Year: {min_revenue['ReleaseYear']}")
print(f"Franchise: {min_revenue['Franchise']}")

# ============================================================
# POKEMON GAMES BAR CHART
# ============================================================
print("\n" + "=" * 60)
print("POKEMON GAMES ANALYSIS")
print("=" * 60)

# Filter Pokemon games
pokemon_df = df[df["Franchise"] == "Pokémon"].sort_values(
    "UnitsSold_Millions", ascending=True
)
print(f"\nNumber of Pokemon games in dataset: {len(pokemon_df)}")
print("\nPokemon Games Sales:")
print(
    pokemon_df[
        ["Title", "UnitsSold_Millions", "Revenue_USD_Millions", "ReleaseYear"]
    ].to_string(index=False)
)

# Create bar chart for Pokemon games
fig, ax = plt.subplots(figsize=(12, 8))

bars = ax.barh(
    pokemon_df["Title"],
    pokemon_df["UnitsSold_Millions"],
    color="#FFCB05",
    edgecolor="#3D7DCA",
    linewidth=1.5,
)

# Add value labels on bars
for bar, value in zip(bars, pokemon_df["UnitsSold_Millions"]):
    ax.text(
        value + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{value}M",
        va="center",
        ha="left",
        fontsize=10,
        fontweight="bold",
    )

ax.set_xlabel("Units Sold (Millions)", fontsize=12, fontweight="bold")
ax.set_ylabel("Game Title", fontsize=12, fontweight="bold")
ax.set_title("Pokemon Games Sales on Nintendo Switch", fontsize=14, fontweight="bold")
ax.set_xlim(0, max(pokemon_df["UnitsSold_Millions"]) + 3)

plt.tight_layout()
plt.savefig("pokemon_sales_chart.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nChart saved as 'pokemon_sales_chart.png'")

# ============================================================
# ADDITIONAL VISUALIZATIONS - TRENDS OVER TIME
# ============================================================

# Create trend charts
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Total Units Sold by Year
ax1 = axes[0, 0]
years = yearly_stats.index
ax1.bar(years, yearly_stats["Total_Units"], color="#E60012", edgecolor="black")
ax1.set_xlabel("Release Year")
ax1.set_ylabel("Total Units Sold (Millions)")
ax1.set_title("Total Units Sold by Year")
ax1.set_xticks(years)

# 2. Total Revenue by Year
ax2 = axes[0, 1]
ax2.bar(years, yearly_stats["Total_Revenue"], color="#00A0E9", edgecolor="black")
ax2.set_xlabel("Release Year")
ax2.set_ylabel("Total Revenue (USD Millions)")
ax2.set_title("Total Revenue by Year")
ax2.set_xticks(years)

# 3. Average Units per Game by Year
ax3 = axes[1, 0]
ax3.plot(
    years,
    yearly_stats["Avg_Units"],
    marker="o",
    linewidth=2,
    markersize=8,
    color="#E60012",
)
ax3.set_xlabel("Release Year")
ax3.set_ylabel("Average Units Sold (Millions)")
ax3.set_title("Average Units Sold per Game by Year")
ax3.set_xticks(years)
ax3.grid(True, alpha=0.3)

# 4. Number of Games Released by Year
ax4 = axes[1, 1]
ax4.bar(years, yearly_stats["Num_Games"], color="#7AC74C", edgecolor="black")
ax4.set_xlabel("Release Year")
ax4.set_ylabel("Number of Games")
ax4.set_title("Number of Games Released by Year")
ax4.set_xticks(years)

plt.tight_layout()
plt.savefig("nintendo_trends_chart.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nTrends chart saved as 'nintendo_trends_chart.png'")

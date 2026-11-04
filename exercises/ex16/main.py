import matplotlib.pyplot as plt
import pandas as pd

df_yearly = pd.read_csv("./data/annual_deaths_by_clinic.csv")
df_monthly = pd.read_csv("./data/monthly_deaths.csv")

# checking for NaN values
# yearly_info = df_yearly.info()
monthly_info = df_monthly.isna().values.any()

# checking for duplicate values
# print(f"Any yearly duplicates? {df_yearly.duplicated().values.any()}")
# print(f"Any monthly duplicates? {df_monthly.duplicated().values.any()}")

# data statistics
df_monthly.describe().round(2)
df_yearly.describe().round(2)

# calculate the probability
prob = df_yearly.deaths.sum() / df_yearly.births.sum() * 100
print(f"Chances od dying in the 1840s in Vienna: {prob:.3}%")

# visualization
plt.figure(figsize=(14, 8), dpi=200)
plt.title("Total Number of Monthly Births and Deaths", fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.grid(color="grey", linestyle="--")
ax1.plot(df_monthly.date, df_monthly.births, color="skyblue", linewidth=3)

ax2.plot(
    df_monthly.date, df_monthly.deaths, color="crimson", linewidth=2, linestyle="--"
)

plt.show()

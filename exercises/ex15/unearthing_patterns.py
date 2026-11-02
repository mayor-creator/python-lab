import matplotlib.pyplot as plt

# import numpy as np
import pandas as pd
import seaborn as sns

df_data = pd.read_csv("./data/nobel_prize_data.csv")

# convert the birth_date column to datetime
df_data["birth_date"] = pd.to_datetime(df_data["birth_date"], errors="coerce")

birth_years = df_data.birth_date.dt.year

# calculate the age at the time of award
df_data["winning_age"] = df_data.year - birth_years

# descriptive statistics and histogram
df_data.winning_age.describe()

plt.figure(figsize=(8, 4), dpi=200)
# sns.histplot(data=df_data, x=df_data.winning_age, bins=30)

# plt.xlabel("Age")
# plt.title("Distribution of Age on Receipt of Prize")
# plt.show()

# box plot
with sns.axes_style("whitegrid"):
    sns.boxplot(data=df_data, x="category", y="winning_age")

plt.show()

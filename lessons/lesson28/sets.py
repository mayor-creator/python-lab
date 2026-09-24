import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./data/sets.csv")
# print(df.head())
# print()
# print(df.tail())

first_release_year = df.sort_values("year").head()
# print(first_release_year)

number_of_sets = df[df["year"] == 1949]
# print(number_of_sets)

largest_number_of_parts = df.sort_values("num_parts", ascending=False).head()
# print(largest_number_of_parts)

# plotting graph
sets_by_year = df.groupby("year").count()

# aggregate
theme_by_year = df.groupby("year").agg({"theme_id": pd.Series.nunique})
theme_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
# print(theme_by_year)

x = sets_by_year.index[:-2]
y = sets_by_year.set_num[:-2]
h = theme_by_year.index[:-2]
k = theme_by_year.nr_themes[:-2]

fig, ax = plt.subplots()
ax.set_xlabel("Year")
ax.set_ylabel("Number of Sets", color="green")
ax.plot(x, y, h, k)
plt.show()

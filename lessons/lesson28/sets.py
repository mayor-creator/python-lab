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

fig, ax1 = plt.subplots()

# two separate axes plot
ax2 = ax1.twinx()

ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Sets", color="green")
ax2.set_ylabel("Number of Themes", color="blue")

line1 = ax1.plot(x, y, color="g", label="Number of Sets")[0]
line2 = ax2.plot(h, k, color="b", label="Number of Themes")[0]

# combine legends from both axes
lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

plt.title("LEGO Sets and Themes Released by Year")
plt.show()

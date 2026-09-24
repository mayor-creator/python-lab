import pandas as pd

colors = pd.read_csv("./data/colors.csv")

unique_colors = colors["name"].nunique()
print(unique_colors)

# transparent_colors = colors.groupby("is_trans").count()
# print(transparent_colors)

print(colors.is_trans.value_counts())

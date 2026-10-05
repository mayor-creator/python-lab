import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("./data/cost_revenue_dirty.csv")

none_values = df.isna().values.any()
# print(none_values)

duplicate_values = df.duplicated().values.any()
# print(duplicate_values)

duplicated_rows = df[df.duplicated()]
# print(len(duplicated_rows))

# convert data in budget to a numeric values
char_to_remove = [",", "$"]
column_to_clean = ["USD_Production_Budget", "USD_Worldwide_Gross", "USD_Domestic_Gross"]

for col in column_to_clean:
    for char in char_to_remove:
        # replace each character with empty string
        df[col] = df[col].astype(str).str.replace(char, "")
    # covert column to a numeric data type
    df[col] = pd.to_numeric(df[col])

# print(df.head())

# convert the release date column to date time object
df.Release_Date = pd.to_datetime(df.Release_Date)

# lowest budget movie
(df[df.USD_Production_Budget == 1100.00])

# highest budget movie
(df[df.USD_Production_Budget == 425000000.00])

# multiple conditional statement
international_release = df.loc[
    (df.USD_Domestic_Gross == 0) & (df.USD_Worldwide_Gross != 0)
]

# print(international_release.head())

# find the difference between revenue
scrape_date = pd.Timestamp("2018-5-1")
future_release = df[df.Release_Date >= scrape_date]

clean_df = df.drop(future_release.index)
money_losing = clean_df.query("USD_Production_Budget > USD_Worldwide_Gross")

# data visualization using Seaborn
plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(
        data=clean_df,
        x="USD_Production_Budget",
        y="USD_Worldwide_Gross",
        hue="USD_Worldwide_Gross",
        size="USD_Worldwide_Gross",
    )

    ax.set(
        ylim=(0, 3000000000),
        lim=(0, 450000000),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $100 millions",
    )

plt.show()

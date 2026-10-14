import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_data = pd.read_csv("./data/nobel_prize_data.csv")

# adding column that contains the percentage shares
separated_values = df_data.prize_share.str.split("/", expand=True)
numerator = pd.to_numeric(separated_values[0])
denominator = pd.to_numeric(separated_values[1])
df_data["share_pct"] = numerator / denominator

prize_per_year = df_data.groupby(by='year').count().prize

# number of average of prizes awarded over time
moving_average = prize_per_year.rolling(window=5).mean()

yearly_avg_share = df_data.groupby(by="year").agg({"share_pct":pd.Series.mean})
share_moving_average = yearly_avg_share.rolling(window=5).mean()

# create a scatter graph to show number of prizes awarded per year over time
plt.title("Number of Nobel Prizes Awarded per Year", fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(
    # create a 5-year tick marks on the axis
    ticks=np.arange(1900, 2021, step=5),
    fontsize=14,
    rotation=45
)

# get current axis
ax1=plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900,2020)

# can invert axis
ax2.invert_yaxis()

ax1.scatter(
    x=prize_per_year.index,
    y=prize_per_year.values,
    c='dodgerblue',
    alpha=.7,
    s=100
)

ax1.plot(
    prize_per_year.index,
    moving_average.values,
    c="crimson",
    linewidth=3
)

# adding prize share plot on second axis
ax2.plot(
    prize_per_year.index,
    share_moving_average.values,
    c="grey",
    linewidth=3
)

plt.show()
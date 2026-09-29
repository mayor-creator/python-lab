import pandas as pd
from matplotlib import pyplot as plt

df_tesla = pd.read_csv("./data/TESLA Search Trend vs Price.csv")

# convert the month column to datetime format
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)

# create the graph axis
x_axis = df_tesla.MONTH
y_axis = df_tesla.TSLA_USD_CLOSE
h_axis = df_tesla.MONTH
k_axis = df_tesla.TSLA_WEB_SEARCH

# graph resolution
plt.figure(figsize=(14, 18), dpi=100)

# graph title
plt.title("Tesla Web Search vs Price", fontsize=18)

# plot the graph
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontsize=14)
ax2.set_ylabel("Search Trend", color="blue", fontsize=14)
ax1.plot(x_axis, y_axis, color="#E6232E", linewidth=3)
ax2.plot(h_axis, k_axis, color="blue", linewidth=3)
plt.show()

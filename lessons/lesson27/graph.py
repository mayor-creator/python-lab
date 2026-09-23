import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./data/QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
df.DATE = pd.to_datetime(df.DATE)

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
reshaped_df.fillna(0, inplace=True)
roll_df = reshaped_df.rolling(window=6).mean()

x = roll_df.index

fig, ax = plt.subplots()
for column in roll_df.columns:
    ax.plot(x, roll_df[column], linewidth=3, label=roll_df[column].name)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.legend(fontsize=14)
plt.show()

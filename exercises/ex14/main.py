import pandas as pd
import plotly.express as px

df_apps = pd.read_csv("./data/apps.csv")

# remove unwanted column
df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)

# find NaN values in rating
nan_rows = df_apps[df_apps.Rating.isna()]

# cleanup data
df_apps_clean = df_apps.dropna()

# find duplicate values
df_apps_duplicate = df_apps_clean.duplicated()

# remove duplicate values
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
df_apps_clean[df_apps_clean.App == "Instagram"]

# find the highest rated app
highest_rated_app = df_apps_clean.sort_values("Rating", ascending=False).head()

# find what's the size in MB of the largest android app
highest_size = df_apps_clean.sort_values("Size_MBs", ascending=False).head()

# find the app with the highest number of reviews
highest_review = df_apps_clean.sort_values("Reviews", ascending=False).head(50)

# graphing a pie chart
ratings = df_apps_clean.Content_Rating.value_counts()

fig = px.pie(
    labels=ratings.index,
    values=ratings.values,
    title="Google Store Apps Content Rating",
    names=ratings.index,
    hole=0.6,
)
fig.update_traces(textposition="outside", textfont_size=15, textinfo="percent")

fig.show()

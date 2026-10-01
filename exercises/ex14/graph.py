import pandas as pd
import plotly.express as px

df_apps = pd.read_csv("./data/apps.csv")

df_apps.drop(["Last_Updated", "Android_Ver"], axis=1, inplace=True)
nan_rows = df_apps[df_apps.Rating.isna()]
df_apps_clean = df_apps.dropna()
df_apps_duplicate = df_apps_clean.duplicated()
df_apps_clean = df_apps_clean.drop_duplicates(subset=["App", "Type", "Price"])
df_apps_clean[df_apps_clean.App == "Instagram"]

# getting information about dataframe
data_info = df_apps_clean.info()

# remove the comma character from Installs column and convert it to numeric data types
df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(",", "")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[["App", "Installs"]].groupby("Installs").count()

df_apps_clean.Price = df_apps_clean.Price.astype(str).str.replace("$", "")
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price)
df_apps_clean[["App", "Price"]].groupby("Price").count()

# remove all apps that cost more than $250
df_apps_clean = df_apps_clean[df_apps_clean["Price"] < 250]
df_apps_clean.sort_values("Price", ascending=False).head()

# find the total number of categories
# print(df_apps_clean.Category.nunique())

# find the top 10 categories
top10_category = df_apps_clean.Category.value_counts()[:10]
# print(top10_category)

# create a bar chat graph
bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

# number of category installed
category_installs = df_apps_clean.groupby("Category").agg({"Installs": pd.Series.sum})
category_installs.sort_values("Installs", ascending=True, inplace=True)

h_bar = px.bar(
    x=category_installs.Installs,
    y=category_installs.index,
    orientation="h",
    title="Category Popularity",
)

h_bar.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")

h_bar.show()

# scatter graph
cat_number = df_apps_clean.groupby("Category").agg({"App": pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on="Category", how="inner")
print(f"The dimensions of the DataFrame are: {cat_merged_df.shape}")
cat_merged_df.sort_values("Installs", ascending=False)

scatter = px.scatter(
    cat_merged_df,  # data
    x="App",  # column name
    y="Installs",
    title="Category Concentration",
    size="App",
    hover_name=cat_merged_df.index,
    color="Installs",
)

scatter.update_layout(
    xaxis_title="Number of Apps (Lower=More Concentrated)",
    yaxis_title="Installs",
    yaxis=dict(type="log"),
)

scatter.show()

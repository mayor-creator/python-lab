import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

df_data = pd.read_csv("./data/nobel_prize_data.csv")

# do duplicates values exist?
df_data.duplicated().values.any()

# do NaN values exist?
df_data.isna().values.any()

# count NaN values per column
df_data.isna().sum()

# filtering on NaN values in the birth date column
col_subset = [
    "year",
    "category",
    "laureate_type",
    "birth_date",
    "full_name",
    "organization_name",
]
df_data.loc[df_data.birth_date.isna()][col_subset]

# convert birth_date to Datetime object
df_data.birth_date = pd.to_datetime(df_data.birth_date)

# adding column that contains the percentage shares
separated_values = df_data.prize_share.str.split("/", expand=True)
numerator = pd.to_numeric(separated_values[0])
denominator = pd.to_numeric(separated_values[1])
df_data["share_pct"] = numerator / denominator

# create a donut chart showing prizes between men and women
biology = df_data.sex.value_counts()
fig = px.pie(
    labels=biology.index,
    values=biology.values,
    title="Percentage of Male vs Female Winners",
    names=biology.index,
)

fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

# fig.show()

# Who are the female winners?
df_data[df_data.sex == "Female"].sort_values('year', ascending=True)

# Who are the repeated winners?
is_winner = df_data.duplicated(subset=['full_name'], keep=False)
multiple_winners = df_data[is_winner]
column_subset = ['year', 'category', 'laureate_type', 'full_name']
multiple_winners[column_subset]

# number of prize per category
df_data.category.nunique()

# create a bar chart to show the number of price per category
prizes_per_category = df_data.category.value_counts()
v_bar = px.bar(
    x=prizes_per_category.index,
    y=prizes_per_category.values,
    color=prizes_per_category.values,
    color_continuous_scale = "Aggrnyl",
    title="Number of Prizes Award per Category"
)

v_bar.update_layout(
    xaxis_title="Noble Prize Category",
    coloraxis_showscale=False,
    yaxis_title="Number of Prizes"
)

# v_bar.show()

# find male and female winners per category
category_men_women = df_data.groupby(['category', 'sex'], as_index=False).agg({'prize':pd.Series.count})
category_men_women.sort_values('prize', ascending=False, inplace=True)

# create a bar char to show men vs women category
v_bar_split = px.bar(
    x=category_men_women.category,
    y=category_men_women.prize,
    color=category_men_women.sex,
    title="Number of Prizes Awarded per Category split between Men and Women"
)

v_bar_split.update_layout(
    xaxis_title="Nobel Prize Category",
    yaxis_title="Number of Prizes"
)

# v_bar_split.show()

# Number of prizes awarded over time
prize_per_year = df_data.groupby(by='year').count().prize

# create a scatter graph to show number of prizes award over time
plt.figure(figsize=(16,8), dpi=200)
plt.title("Number of Nobel Prizes Awarded per Year", fontsize=18)

plt.scatter(
    x=prize_per_year.index,
    y=prize_per_year.values,
    c='dodgerblue',
    alpha=.7,
    s=100
)

# number of average of prizes awarded over time
moving_average = prize_per_year.rolling(window=5).mean()

plt.plot(
    prize_per_year.index,
    moving_average.values,
    c="crimson",
    linewidth=3
)

plt.show()
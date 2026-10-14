import pandas as pd
import plotly.express as px

df_data = pd.read_csv("./data/nobel_prize_data.csv")

df_data["cleaned_country"] = df_data["birth_country_current"].str.lower().str.strip()

african_countries = {
    "algeria",
    "angola",
    "benin",
    "botswana",
    "burkina faso",
    "burundi",
    "cabo verde",
    "cameroon",
    "central african republic",
    "chad",
    "comoros",
    "congo",
    "democratic republic of the congo",
    "djibouti",
    "egypt",
    "equatorial guinea",
    "eritrea",
    "eswatini",
    "ethiopia",
    "gabon",
    "gambia",
    "ghana",
    "guinea",
    "guinea-bissau",
    "ivory coast",
    "cote d'ivoire",
    "kenya",
    "lesotho",
    "liberia",
    "libya",
    "madagascar",
    "malawi",
    "mali",
    "mauritania",
    "mauritius",
    "morocco",
    "mozambique",
    "namibia",
    "niger",
    "nigeria",
    "rwanda",
    "sao tome and principe",
    "senegal",
    "seychelles",
    "sierra leone",
    "somalia",
    "south africa",
    "south sudan",
    "sudan",
    "tanzania",
    "togo",
    "tunisia",
    "uganda",
    "zambia",
    "zimbabwe",
}

african_df = df_data[df_data["cleaned_country"].isin(african_countries)]

# display unique country names present in the data
unique_african_countries = african_df["birth_country_current"].unique()

# display countries and their respective row counts
country_counts = african_df["birth_country_current"].value_counts()

# aggregate the data to count prizes per country
prize_counts = african_df["birth_country_current"].value_counts().reset_index()

# rename columns for clarity
prize_counts.columns = ["birth_country_current", "prize_count"]

# category break down by country
category_country = african_df.groupby(
    ["birth_country_current", "category"], as_index=False
).agg({"prize": pd.Series.count})
category_country.sort_values(by="prize", ascending=False, inplace=True)

# merge the dataframe with category_country and prize_counts
merge_df = pd.merge(category_country, prize_counts, on="birth_country_current")
merge_df.columns = ["birth_country_current", "category", "cat_prize", "total_prize"]
merge_df.sort_values(by="total_prize", inplace=True)

# create bar chart using the aggregated dataframe
h_bar = px.bar(
    x=prize_counts["prize_count"],
    y=prize_counts["birth_country_current"],
    orientation="h",
    color=prize_counts["birth_country_current"],
    color_continuous_scale="Blackbody",
    title="African Countries by Number of Nobel Prizes",
)

h_bar.update_layout(
    xaxis_title="Number of Prizes", yaxis_title="Country", coloraxis_showscale=False
)

# h_bar.show()

category_country_bar = px.bar(
    x=merge_df.cat_prize,
    y=merge_df.birth_country_current,
    color=merge_df.category,
    orientation="h",
    title="African Countries by Number of Nobel Prizes and Category",
)

category_country_bar.update_layout(
    xaxis_title="Number of Prizes", yaxis_title="Country"
)

# category_country_bar.show()

# country prizes over time
prize_by_year = african_df.groupby(
    by=["birth_country_current", "year"], as_index=False
).count()
prize_by_year = prize_by_year.sort_values("year")[
    ["year", "birth_country_current", "prize"]
]

cumulative_prizes = (
    prize_by_year.groupby(by=["birth_country_current", "year"])
    .sum()
    .groupby(level=[0])
    .cumsum()
)
cumulative_prizes.reset_index(inplace=True)
print(cumulative_prizes)

# create a line graph
l_chart = px.line(
    cumulative_prizes,
    x="year",
    y="prize",
    color="birth_country_current",
    hover_name="birth_country_current",
)

l_chart.update_layout(xaxis_title="Year", yaxis_title="Number of Prizes")

l_chart.show()

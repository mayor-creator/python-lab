import pandas as pd
import plotly.express as px

df_data = pd.read_csv("./data/nobel_prize_data.csv")

# find top 20 countries
top_countries = df_data.groupby(["birth_country_current"], as_index=False).agg(
    {"prize": pd.Series.count}
)
top_countries.sort_values(by="prize", inplace=True)
top_countries = top_countries[-20:]

# print(top_countries)

h_bar = px.bar(
    x=top_countries.prize,
    y=top_countries.birth_country_current,
    orientation="h",
    color=top_countries.prize,
    color_continuous_scale="Viridis",
    title="Top 20 Countries by Number of Prizes",
)

h_bar.update_layout(
    xaxis_title="Number of Prizes", yaxis_title="Country", coloraxis_showscale=False
)

# h_bar.show()

# displaying data on map
df_countries = df_data.groupby(["birth_country_current", "ISO"], as_index=False).agg(
    {"prize": pd.Series.count}
)
df_countries.sort_values("prize", ascending=False)

world_map = px.choropleth(
    df_countries,
    locations="ISO",
    color="prize",
    hover_name="birth_country_current",
    color_continuous_scale=px.colors.sequential.matter,
)

world_map.update_layout(coloraxis_showscale=True)

world_map.show()

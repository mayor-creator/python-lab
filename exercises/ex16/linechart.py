import pandas as pd
import plotly.express as px

df_yearly = pd.read_csv("./data/annual_deaths_by_clinic.csv")
df_monthly = pd.read_csv("./data/monthly_deaths.csv")


line = px.line(
    df_yearly,
    x="year",
    y="births",
    color="clinic",
    title="Total Yearly Births by Clinic",
)

# line.show()

# create a new column
df_yearly["pct_deaths"] = df_yearly.deaths / df_yearly.births

# calculate the average death rate for both clinics
clinic_1 = df_yearly[df_yearly.clinic == "clinic 1"]
avg_c1 = clinic_1.deaths.sum() / clinic_1.births.sum() * 100
print(f"Average death rate in clinic 1 is {avg_c1:.3}%")

print()

clinic_2 = df_yearly[df_yearly.clinic == "clinic 2"]
avg_c2 = clinic_2.deaths.sum() / clinic_2.births.sum() * 100
print(f"Average death rate in clinic 2 is {avg_c2:.3}%")

line_chart = px.line(
    df_yearly,
    x="year",
    y="pct_deaths",
    color="clinic",
    title="Proportion of Yearly Deaths by Clinic",
)

line_chart.show()

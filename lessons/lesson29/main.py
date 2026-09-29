import pandas as pd

df_tesla = pd.read_csv("./data/TESLA Search Trend vs Price.csv")

# shape of the data frames
print(df_tesla.shape)
print()
# columns of the data frames
print(df_tesla.columns)
print()
# access column values
print(f"The largest value for Tesla in Web search: {df_tesla["TSLA_WEB_SEARCH"].max()}")
print(
    f"The smallest value for Tesla in Web search: {df_tesla["TSLA_WEB_SEARCH"].min()}"
)
print()
# describe the dataframe statistics
print(df_tesla.describe())

print("***** Unemployment Data ******")
df_unemployment = pd.read_csv("./data/UE Benefits Search vs UE Rate 2004-19.csv")

print(df_unemployment.head())

print()

print(df_unemployment.columns)

print("**** Bitcoin Data ****")
df_bitcoin = pd.read_csv("./data/Daily Bitcoin Price.csv")

# missing data value
print(f"Missing values for Bitcoin?: {df_bitcoin.isna().values.any()}")

# remove missing value
df_bitcoin = df_bitcoin.dropna()

# removing any missing values available
df_bitcoin = df_bitcoin.dropna(inplace=True)

# converting strings to date
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
print(df_tesla.MONTH)

# converting daily data into monthly data

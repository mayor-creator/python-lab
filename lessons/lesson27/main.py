import pandas as pd

df = pd.read_csv("./data/QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

# determine the total number of programming languages
total_languages = df.groupby("TAG").sum()

# determine the number of months of data exist per language
count_language = df.groupby("TAG").count()

# data cleaning and working with time stamps
date_time = df.DATE[1]

# convert date string to a timestamp
string_date = pd.to_datetime(date_time)

# convert the entire df["DATE"] column to timestamp
df.DATE = pd.to_datetime(df.DATE)

# data manipulation: pivoting dataframes
reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")

# print(reshaped_df.shape)
# print(reshaped_df.columns)
# print(reshaped_df.count())

# dealing with NaN values
reshaped_df.fillna(0, inplace=True)
# print(reshaped_df.head())

# determine if NaN values still exist in the entire dataframe
print(reshaped_df.isna().values.any())

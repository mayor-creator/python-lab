import pandas as pd

# read a csv file
df = pd.read_csv("./data/salaries_by_college_major.csv")

# determine the first 5 rows of dataframe
row_data = df.head()

# determine the number of rows and columns
num_rows_columns = df.shape

# access columns attributes
columns = df.columns

# determine not a number values
not_num = df.isna()

# determine the last 5 rows of dataframe
last_row_data = df.tail()

# delete the last row
clean_df = df.dropna()
clean_df.tail()

# access to a particular column dataframe
salary = clean_df["Starting Median Salary"]

# determine highest value
highest_salary = salary.max()

# determine row number with the highest values
row_highest_salary = clean_df["Starting Median Salary"].idxmax()

# determine the value of a particular cell
cell = clean_df["Undergraduate Major"].loc[43]
# clean_df["Undergraduate Major"][43]
# print(clean_df.loc[43])

# perform arithmetic with entire columns
difference = clean_df["Mid-Career 90th Percentile Salary"].subtract(
    clean_df["Mid-Career 10th Percentile Salary"]
)

# add data to existing dataframe
spread_col = (
    clean_df["Mid-Career 90th Percentile Salary"]
    - clean_df["Mid-Career 10th Percentile Salary"]
)
clean_df.insert(1, "Spread", spread_col)
print(clean_df.head())

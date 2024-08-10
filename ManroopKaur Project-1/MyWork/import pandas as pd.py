import pandas as pd

# Load datasets
df1 = pd.read_csv('Resources\Mental health Depression disorder Data.csv')
df2 = pd.read_csv('Resources\Suicide Rates from 2012-2017.xlsx')

# Inspect the datasets
print(df1.head())
print(df2.head())

# Drop unnecessary columns (example)
df1 = df1.drop(columns=['unnecessary_column1', 'unnecessary_column2'])
df2 = df2.drop(columns=['unnecessary_column3', 'unnecessary_column4'])

# Handle missing data (example: dropping rows with missing values)
df1 = df1.dropna()
df2 = df2.dropna()

# Alternatively, impute missing values (example: filling with mean)
df1['some_column'] = df1['some_column'].fillna(df1['some_column'].mean())
df2['another_column'] = df2['another_column'].fillna(df2['another_column'].mean())

# Standardize column names
df1.rename(columns={'Country': 'country', 'Year': 'year'}, inplace=True)
df2.rename(columns={'Country': 'country', 'Year': 'year'}, inplace=True)

# Merge datasets
merged_df = pd.merge(df1, df2, on=['country', 'year'], how='inner')

# Inspect the merged dataset
print(merged_df.head())


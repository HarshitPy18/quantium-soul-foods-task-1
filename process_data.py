import pandas as pd

# Load the three CSV files
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

# Combine all three dataframes into one
df = pd.concat([df0, df1, df2], ignore_index=True)

# Print the first few rows just to make sure it worked
print(df.head())
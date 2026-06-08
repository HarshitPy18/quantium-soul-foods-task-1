import pandas as pd

# Load the three CSV files
df0 = pd.read_csv('data/daily_sales_data_0.csv')
df1 = pd.read_csv('data/daily_sales_data_1.csv')
df2 = pd.read_csv('data/daily_sales_data_2.csv')

# Combine all three dataframes into one
df = pd.concat([df0, df1, df2], ignore_index=True)

# 1. Filter out all rows that aren't "pink morsel"
df = df[df['product'] == 'pink morsel']

# 2. Clean the price column (remove the '$' and convert to a number)
df['price'] = df['price'].str.replace('$', '').astype(float)

# 3. Create the new "sales" column by multiplying price and quantity
df['sales'] = df['price'] * df['quantity']

# 4. Keep only the columns we need: sales, date, and region
final_df = df[['sales', 'date', 'region']]

# 5. Save this clean data to a new CSV file
final_df.to_csv('formatted_data.csv', index=False)

print("Data processed successfully!")
print(final_df.head())
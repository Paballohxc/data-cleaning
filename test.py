import pandas as pd

# Replace the path below with the correct path to your CSV if it's somewhere else
df = pd.read_csv("dirty_sales_data.csv")

# Print the whole dataset
print(df)

# 🔁 Step 1: Remove duplicate rows
df = df.drop_duplicates()
print("\nAfter removing duplicates:\n", df)

# 🔎 Step 2: Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# 🧹 Step 3: Impute or remove missing data

# Fill missing 'Category' with "Unknown"
df['Category'] = df['Category'].fillna("Unknown")

# Fill missing 'Quantity' with median
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# Fill missing 'Price' with mean
df['Price'] = df['Price'].fillna(df['Price'].mean())

# Fill missing 'Date' with forward fill (previous row's value)
df['Date'] = df['Date'].fillna(method='ffill')

# Drop rows where 'Product' is still missing (can’t impute meaningfully)
df = df.dropna(subset=['Product'])

# 💾 Optional: Save the cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

# ✅ Show cleaned data
print("\nCleaned Data:\n", df)
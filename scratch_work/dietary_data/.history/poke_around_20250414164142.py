import pandas as pd
df = pd.read_sas("DR1IFF_L.xpt", format="xport")
# Show first few rows
print(df.head())

# Show column names
print(df.columns)

# Check types
print(df.dtypes)

# Basic summary
print(df.describe(include="all"))

df.to_csv("converted.csv", index=False)

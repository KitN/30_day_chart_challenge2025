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

#  Read another file
df = pd.read_sas("DRXFCD_L.xpt", format="xport")
df.to_csv("codes.csv", index=False)

df = pd.read_sas("DEMO_L.xpt", format="xport")
df.to_csv("demographics.csv", index=False)
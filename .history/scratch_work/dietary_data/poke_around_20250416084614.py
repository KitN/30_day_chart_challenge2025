import pandas as pd
# Basic summary
#print(df.describe(include="all"))

#df.to_csv("converted.csv", index=False)

#  Read another file
#df = pd.read_sas("DRXFCD_L.xpt", format="xport")
#df.to_csv("codes.csv", index=False)

df = pd.read_sas("scratch_work\dietary_data\DEMO_L.xpt", format="xport")
df.to_csv("scratch_work\dietary_data\demographics.csv", index=False)
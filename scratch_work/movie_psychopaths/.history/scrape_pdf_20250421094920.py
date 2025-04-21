import camelot

# Extract tables from a PDF
tables = camelot.read_pdf("psychopath_table.pdf", pages="1")

# Print the number of tables found
print(f"Number of tables found: {len(tables)}")

# Export the first table to a CSV file
tables[0].to_csv("table.csv")

# Convert the first table to ap pandas DataFrame
df = tables[0].df
print(df)
"""
pandas

What it does:
- Works with tabular data.
- Similar to Excel, but inside Python.
- Useful for CSV analysis, reports, filtering, grouping, and data cleaning.
"""
import pandas as pd

# Create data - Creates a dictionary with columns.
data = {
    "ticket_id": ["INC001", "INC002", "INC003", "INC004"],
    "status": ["Open", "Closed", "Open", "In Progress"],
    "priority": ["High", "Medium", "Low", "High"]
}

# Create DataFrame - A DataFrame is like a table in Python.
df = pd.DataFrame(data) # pd is a common alias instead of writing pandas.

print(df)

# Show first rows
print(df.head())

# Filter Rows
open_tickets = df[df["status"]=="Open"]

# Count Values
status_count = df["status"].value_counts()
print(status_count)

# Save to CSV
df.to_csv("tickets.csv", index=False)

# Read from CSV
csv_data = pd.read_csv("tickets.csv")
print(csv_data)

# Group by priority
priority_count = df.groupby("priority").size()
print(priority_count)

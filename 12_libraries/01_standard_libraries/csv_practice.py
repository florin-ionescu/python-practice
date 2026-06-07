"""
CSV Module
What it does:
- Reads and writes CSV files.
- CSV means Comma-Separated Values.
- Useful for reports, exported ticket data, spreadsheets, logs, etc.
"""
import csv

# Example 1: Write data to a CSV file
# w means write mode. If the file does not exist, Python creates it. If it already exists, Python overwrites it.
with open("employees.csv", "w", newline="") as file:
    # newline="" helps avoid extra blank lines when writing CSV files, especially on Windows.
    # csv.writer() built in function
    writer = csv.writer(file)

    # writerow() is a built-in method of the CSV writer object.
    writer.writerow(["name", "role", "department"])
    writer.writerow(["Florin", "IT Support", "Oracle"])
    writer.writerow(["Ana", "QA Engineer", "Testing"])

# Example 2: Read data from a CSV file.
with open("employees.csv", "r") as file:
    # csv.reader() built in function
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Example 3: Read CSV as dictionaries:
with open("employees.csv", "r") as file:
    # csv.DictReader() built in function that reads the csv as dict
    reader = csv.DictReader(file)
    # {"name": "Florin", "role": "IT Support", "department": "Oracle"}

    for row in reader:
        print(row["name"], "-", row["role"], "- Department:", row["department"])
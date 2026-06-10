"""
String Parsing

What this file covers:
- Extracting useful information from strings
- Splitting text
- Searching inside text
- Parsing simple logs, emails, and IDs
"""
# 1. Parse full name
full_name = "Florin Ionescu"
parts = full_name.split()

first_name = parts[0]
last_name = parts[1]
print(first_name)
print(last_name)
# .split() separates the string by spaces.
# "Florin Ionescu" becomes ["Florin", "Ionescu"].


# 2. Parse email
email = "florin.ionescu@example.com"
email_parts = email.split("@")

username = email_parts[0]
domain = email_parts[1]

print(username)
print(domain)
# Splitting by "@" separates the username and domain.

# 3. Parse domain name. "example.com" becomes ["example", "com"].
domain_parts = domain.split(".")

company = domain_parts[0]
extension = domain_parts[1]

print(company)
print(extension)

# 4. Parse ticket ID
ticket = "INC123456"

prefix = ticket[0:3]
number = ticket[3:0]

print(prefix)
print(number)
# ticket[0:3] gives the first 3 characters: INC.
# ticket[3:] gives everything after index 3.

# 5. Parse simple log line
log_line = "2026-06-10 ERROR Payment service timeout"

date = log_line[0:10]
level = log_line[11:16]
message = log_line[17:]

print(date)
print(level)
print(message)
# Explanation:
# This uses slicing when the text format is predictable.

# 6. Better parsing with split()
log_line = "\n2026-06-10|ERROR|Payment service timeout"
print(log_line)
parts = log_line.split("|")

date = parts[0]
level = parts[1]
message = parts[2]

print(date)
print(level)
print(message)
# If the string has a separator like "|", split() is cleaner.

# 7. Parse key-value text
record = "name=Florin;role=IT Support;company=Oracle"

fields = record.split(";")

for field in fields:
    key_value = field.split("=")
    key = key_value[0]
    value = key_value[1]

    print(key, "=>", value)
# Explanation:
# First split by ";" to separate fields.
# Then split by "=" to separate key and value.

# 8. Extract file extension
filename = "report.csv"
extension = filename.split(".")[-1]
print(extension)
# Explanation:
# split(".") gives ["report", "csv"].
# [-1] gets the last item.

# 9. Extract folder and file name from path
path = "reports/2026/tickets.csv"
parts = path.split("/")

folder = parts[0]
year = parts[1]
filename = parts[2]

print(folder)
print(year)
print(filename)
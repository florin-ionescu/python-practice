"""
re module

What it does:
- Works with regular expressions.
- Useful for searching patterns in text.
- Common examples: emails, ticket IDs, error codes, timestamps.
"""

import re

text = """
User florin@example.com reported issue INC123456.
Another email is support@company.com.
Error code: ORA-00942
"""

# Search for first match
match = re.search(r"INC\d+", text)

if match:
    print("Found ticket:", match.group())

# Find all email addresses
emails = re.findall(r"\w+@\w+\.\w+", text)
print("Emails:", emails)

# Find Oracle-style error code
error_code = re.findall(r"ORA-\d+", text)
print("Error code:", error_code)

# Replace text
cleaned_text = re.sub(r"INC\d+", "[TICKET_ID]", text)
# re.sub() means substitute/replace.
print(cleaned_text)

# Validate simple email
email = "test@example.com"
# ^ means start of string.
# $ means end of string.
pattern = r"^\w+@\w+\.\w+$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")



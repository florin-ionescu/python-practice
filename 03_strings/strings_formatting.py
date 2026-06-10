"""
String Formatting

What this file covers:
- Combining text and variables
- f-strings
- Formatting numbers
- Formatting decimals
"""

# 1. Basic string concatenation
name = "Florin"
role = "IT Support"
message = "My name is " + name + " and I am under " + role
print(message)
# Explanation:
# + joins strings together.
# This is called concatenation.


# 2. Concatenation problem with numbers
age = 30
# Wrong:
# print("Age: " + age)

# correct
print("Age: " + str(age))
# Explanation:
# You cannot join string + integer directly.
# str(age) converts the integer to string.


# 3. Printing with commas
print("Name:", name)
print("Age:", age)
# Explanation:
# print() with commas can display different data types.
# Python automatically adds spaces.


# 4. f-string basics
print(f"My name is {name}.")
print(f"I am {age} years old.")
# f-strings allow you to insert variables directly inside text.
# Variables go inside curly braces.


# 5. f-string with expression
first_number = 10
second_number = 5

print(f"Total is {first_number + second_number}")
# Explanation:
# You can also use expressions inside f-strings.


# 6. Format decimal number
price = 19.231234
print(f"Price: {price:.2f}")
# Explanation:
# :.2f keeps 2 digits after the decimal point.
# Output:  19.88



# 7. Format percentage
success_rate = 0.9231
print(f'Success: {success_rate:.2%}')
# Explanation:
# :.2% formats the number as a percentage with 2 decimals.
# 0.92345 becomes 92.35%.


# 8. Practical ticket message
ticket_id = "INC123456"
status = "Open"
priority = "High"

print(f"Ticket {ticket_id} is currently {status} with {priority} priority.")
# This creates a clean readable message using variables.

# 9. Align text
print(f"{'Name':<10}{'Role':<25}")
print(f"{'Florin':<10} {'IT Support':<25}")
print(f"{'Ana':<10} {'QA Engineer':<25}")
# <10 means left-align inside 10 spaces.
# <25 means left align inside 25 spaces.
# This is useful for simple terminal tables.


# 10. Format large numbers
users = 137000
print(f"Users supported: {users:,}")
# :, adds thousand separators.
# 137000 becomes 137,000.
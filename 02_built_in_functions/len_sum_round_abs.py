"""
len(), sum(), round(), abs()

What this file covers:
- len() for length
- sum() for totals
- round() for rounding numbers
- abs() for absolute values
"""

# 1. len() with string
name = "Florin"
print(len(name))
# len() returns the number of characters in a string.
# "Florin" has 6 characters.

# 2. len() with list
skills = ["Python", "SQL", "GIT"]
print(len(skills))
# len() returns the number of items in a list.

# 3. len() with dictionary
user = {
    "name": "Florin",
    "role": "IT Support Engineer",
    "company": "Oracle"
}
print(len(user))
# len() returns the number of keys in a dictionary.
# This dictionary has 3 keys.

# 4. sum() with list of numbers
numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)
# sum() adds all numbers from a list.
# 10 + 20 + 30 + 40 = 100

# 5. Calculate average
grades = [8, 9, 10, 7]
average = sum(grades) / len(grades)
print(average)
# Average = total divided by number of items.
# sum(grades) gives the total.
# len(grades) gives how many grades exist.

# 6. round() basic usage
price = 19.87654
rounded_price = round(price, 1)
print(rounded_price)
# round(number, digits) rounds a number.
# round(price, 2) keeps 2 decimals.

# 7. round() without second argument
number = 19.87654

print(round(number))
# Explanation:
# If you do not provide the second argument,
# round() rounds to the nearest whole number.

# 8. abs() basic usage

difference = -15
print(abs(difference))
# abs() returns the absolute value.
# It removes the minus sign.
# abs(-15) becomes 15.

# 9. Practical example: ticket difference
expected_tickets = 100
actual_tickets = 87
difference = actual_tickets - expected_tickets
print(difference)
print(abs(difference))
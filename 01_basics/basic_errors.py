"""
Basic Errors in Python

What this file covers:
- Common beginner Python errors
- Why they happen
- How to fix them

Important:
Errors are normal. They are Python's way of telling you what went wrong.
"""

# 1. SyntaxError
# A SyntaxError can happen when code is not written correctly.

# Wrong: print("Hello"
# Correct:
print("Hello, World")

# 2. NameError
# # A NameError happens when you use a variable that does not exist.

# 3. TypeError
# A TypeError happens when you use the wrong data type.

# Wrong:
# age = 30
# print("Age: " + age)

# Explanation:
# You cannot directly join a string and an integer with +.
# Convert the integer to a string first using str(),
# or use comma inside print().

# 4. ValueError
# A ValueError happens when the data type is correct,
# but the value itself is not valid.
# Wrong:
# number = int("abc")

# Correct:
number = int("123")
print(number)

# 5. IndexError
# An IndexError happens when you try to access a list position that does not exist.

skills = ["Python", "SQL", "Git"]
# Wrong:
# print(skills[5])

# Correct:
print(skills[0])
print(skills[1])
print(skills[2])


# Explanation:
# Python indexes start from 0.
# skills[0] is "Python"
# skills[1] is "SQL"
# skills[2] is "Git"
# skills[5] does not exist.


# 6. KeyError
# A KeyError happens when you try to access a dictionary key that does not exist.
user = {
    "name": "Florin",
    "role": "IT Support Engineer"
}
# Wrong:
# print(user["age"])
# Correct:
print(user["name"])
print(user.get("age", "Age not found"))

# 7. ZeroDivisionError
# A ZeroDivisionError happens when you divide by zero.
# Wrong:
# result = 10 / 0 # Division by zero is not allowed in mathematics or Python.

# Correct:
result = 10 / 2
print(result)


# 8. FileNotFoundError
# A FileNotFoundError happens when Python tries to open a file that does not exist.
# wrong
# with open("missing_file.txt", "r") as file:
#       content = file.read()

# correct:
with open('example_file.txt', "w") as file:
    file.write("This file exists now")
with open('example_file.txt', 'r') as file:
    content = file.read()
print(content)

# 9. Basic try/except
# try/except lets you handle errors without crashing the program.


text = "abc"

try:
    converted_number = int(text)
    print(converted_number)
except ValueError:
    print("Cannot convert text to number.")

# 10. Practical example: safe division

first_number = 10
second_number = 0

try:
    division_result = first_number / second_number
    print(division_result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
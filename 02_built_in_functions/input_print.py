"""
input() and print()

What this file covers:
- How to display information with print()
- How to ask the user for input()
- Why input() always returns a string
- How to convert input into numbers
"""
# 1. Basic print
print("Hello, Florin!")
print("Welcome to Python practice.")
# Explanation:
# print() displays information in the terminal.

# 2. Printing variables

name = "Florin"
role = "IT Support Engineer"

print(name)
print(role)

# Explanation:
# You can print text directly or print values stored inside variables.

# 3. Printing multiple values

print("Name:", name)
print("Role:", role)

# Explanation:
# You can separate values with commas inside print().
# Python automatically adds spaces between them.

# 4. Using f-strings

print(f"My name is {name}.")
print(f"My role is {role}.")

# Explanation:
# f-strings allow you to insert variables inside text.
# The variable goes inside curly braces: {}

# 5. Basic input

user_name = input("Enter your name: ")

print(f"Hello, {user_name}!")
# Explanation:
# input() asks the user to type something.
# Whatever the user types is stored as a string.

# 6. input() always returns a string
age = input("Enter your age: ")

print(age)
print(type(age))
# # Even if the user types 30, Python stores it as "30", not as number 30.

# 7. Convert input to integer
age = int(input("Enter your age again: "))

print(f"Next year you will be {age + 1} years old.")


# Explanation:
# int() converts the input from string to integer.
# This allows you to do math with it.


# 8. Convert input to float
price = float(input("Enter a price: "))

print(f"Price with tax: {price * 1.19}")


# Explanation:
# float() converts the input to a decimal number.

# 9. Simple mini exercise

first_number = int(input("enter a number:"))
second_number = int(input("second number: "))

result = first_number + second_number
print(f"total is {result}")
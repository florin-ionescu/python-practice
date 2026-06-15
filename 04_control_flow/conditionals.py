"""
CONDITIONALS IN PYTHON

Conditionals allow your program to make decisions.

They are used when you want different code to run depending on whether
a condition is True or False.

Main keywords:
- if
- elif
- else
"""

# if means: check this condition first
# elif means: otherwise, check this other condition
# else means: if none of the conditions above were true, do this

age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Happy Birthday")
else:
    print("Adult")

'''
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False,
    # but condition_2 is True
else:
    # runs if none of the above conditions are True
'''

# Comparison operators

"""
==  equal to
!=  not equal to
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to
"""

while True:
    name = input("What is your name? (Type stop to exit): ")

    if name.lower() == "stop":
        break

    if name.lower() == "florin":
        print("Welcome, Boss")
    elif name.lower() == "cichicean":
        print("Hello, Master")
    else:
        print("No idea who you are, buddy!")


# Logical operators

"""
and - both conditions must be True
or  - at least one condition must be True
not - reverses the result
"""



# Truthy and falsy values

"""
Falsy values:
- False
- None
- 0
- empty string ""
- empty list []
- empty dictionary {}

Everything else is usually considered truthy.
"""
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")



"""
WHEN TO USE CONDITIONALS

Use conditionals when:
- you need to make decisions
- you need to validate input
- you need to handle different cases
- you need to control what happens based on data

Examples:
- checking if a user is logged in
- checking if a payment was successful
- checking if a file exists
- checking if a ticket is open, closed, or escalated
"""
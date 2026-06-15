# Nested conditions means putting an if statement inside another if statement.

age = 18
has_id = False

if age >= 18:
    # So the inner condition only runs if the outer condition is true.
    if has_id:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote!")
else:
    print("You are too young to vote!")



# Ask the user for a username.
username = input("Enter username: ")

# Ask the user for a password.
password = input("Enter password: ")

if username == "admin":
    # This is a nested condition.
    # It is inside the first if block.
    # Python checks the password only if the username is correct.
    if password == "1234":
        print("Login successful.")
    else:
        print("Incorrect password.")

# this runs when the username is not admin
else:
    print("Unknown username.")

'''
First check condition 1
Only if condition_one is true, check condition_two.

if condition_one:
    if condition_two:
        print("Both conditions are true")
'''
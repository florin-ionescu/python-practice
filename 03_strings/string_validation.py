"""
String Validation

What this file covers:
- Checking if strings match simple rules
- Validating names, emails, passwords, and ticket IDs
"""
# 1. Validate that a name is not empty
name = "Florin"

if name:
    print("Name is valid")
else:
    print("Name is missing")
# Explanation:
# Empty strings are treated as False.
# Non-empty strings are treated as True.


# 2. Validate after stripping spaces
name = '   '

if name.strip():
    print("Name is TRUE")
else:
    print("Name is FALSE")
# Explanation:
# "   " contains spaces, but no real text.
# .strip() removes spaces before checking.


# 3. Validate email simple version
email = "florin@example.com"

if "@" in email and "." in email:
    print("Email looks valid")
else:
    print("Email looks invalid")
# Explanation:
# This is a simple beginner check.
# It checks if the email contains @ and dot.

# 4. Validate password length
password = "Python123"

if len(password) >= 8:
    print("TRUE - Valid email")
else:
    print("FALSE - Not valid")
# Explanation:
# len(password) counts the number of characters.

# 5. Validate password has a digit
has_digit = False

for character in password:
    if character.isdigit():
        has_digit = True

if has_digit:
    print("Password contains a digit")
else:
    print("Password must contain a digit")


# 6. Validate password has uppercase letter
has_upper = False

for character in password:
    if character.isupper():
        has_uppercase = True

if has_uppercase:
    print("Password contains uppercase letter")
else:
    print("Password must contain uppercase letter")
# Explanation:
# .isupper() checks if a character is uppercase.


# 7. Validate ticket ID
ticket_id = "INC123456"

if ticket_id.startswith("INC") and ticket_id[3:0].isdigit():
    print("Valid ticket")
else:
    print("Invalid ticket")
# Explanation:
# .startswith("INC") checks the prefix.
# ticket_id[3:] gets everything after INC.
# .isdigit() checks if the rest is numeric.

# 8. Validate file extension
filename = "text.csv"
if filename.endswith('csv'):
    print("Yes, its a CSV")
else:
    print("Not csv")
# Explanation:
# .endswith(".csv") checks the file extension.


# 9. Validate username

username = "florin_123"
if len(username) >= 5 and "_" in username:
    print("Valid")
else:
    print("Invalid")
# Explanation:
# This checks two rules:
# - at least 5 characters
# - contains underscore


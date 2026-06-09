"""
Constant Naming in Python

What this file covers:
- What constants are
- How constants are named
- Why uppercase names are used
- Examples of good and bad constant naming
"""
# A constant is a value that should not change during the program.

# In Python, constants are usually written in UPPERCASE.
# This is a convention, not a strict rule.

MAX_LOGIN_ATTEMPTS = 3
DEFAULT_LANGUAGE = "English"
PI = 3.14159
COMPANY_NAME = "Oracle"
SUPPORT_EMAIL = "support@example.com"


print(MAX_LOGIN_ATTEMPTS)
print(DEFAULT_LANGUAGE)
print(PI)
print(COMPANY_NAME)
print(SUPPORT_EMAIL)
# Explanation:
# These values are written in uppercase because they should stay the same.
# Python will still allow you to change them, but you should not.

# Example: using a constant in logic

failed_login_attempts = 2

if failed_login_attempts >= MAX_LOGIN_ATTEMPTS:
    print("Account locked")
else:
    print("You can try again")

# Example: password validation
password = "Python123"

if len(password) >= MIN_PASSWORD_LENGTH:
    print("Password length is valid")
else:
    print("Password is too short")

# Naming rules for constants:
# 1. Use uppercase letters.
# 2. Separate words with underscores.
# 3. Use clear names.
# 4. Avoid unclear abbreviations.


# Good names:
MAX_RETRY_COUNT = 5
DEFAULT_PAGE_SIZE = 20
DATABASE_NAME = "users_db"


# Bad names:
x = 5
num = 20
db = "users_db"

# Good names explain the purpose of the value.
# Bad names are unclear and harder to understand later.


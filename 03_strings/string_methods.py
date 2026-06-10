"""
String Methods

What this file covers:
- Common string methods
- How to clean and modify text
- How to search inside strings
"""
# # 1. upper() -  Converts all letters to uppercase.
text = "   python is useful for automation   "
print(text.upper())

# 2. .lower() converts into lowercase
print(text.lower())

# 3. .title()  Converts first letter of each word to uppercase
print(text.title())

# 4. capitalize() Converts only the FIRST letter of the string to upper
print(text.capitalize())

# 5. .strip() Removes spaces from the beginning and the end
print(text.strip())

# 6. .lstrip() Removes spaces from LEFT SIDE ONLY
print(text.lstrip())

# 7. .rstrip() Removes spaces from RIGHT ONLY
print(text.rstrip())

# 8. .replace() Replaces one part of a string with another
print(text.replace("useful", "very very good "))

# 9 .split() Converts string into a list and it is separated by spaces or by argument you provide
skills_text = "Python,SQL,Git,APIs"
skills_list_conversion = skills_text.split(",")
print(skills_list_conversion)

# 10. "".join() Joins list items into one string." " <- separator
skills_list = ["Python", "SQL", "Git", "APIs"]
joined_skills = " | ".join(skills_list)
print(joined_skills)

# 11. .startswith() Checks if a string starts with a specific value. Returns True or False
filename = "report_2026.csv"
print(filename.startswith("report"))

# 12. .endswith() check is it end with a specific value
print(filename.endswith("csv"))
# Useful for checking file extensions.


# 13. .find()  returns the index where the word starts.
message = "Error found in application logs"
print(message.find("application"))
# If the word is not found, it returns -1.

# 14. .count ||| returns how many times a value appears
log_text = "error warning error info error"
print(log_text.count("error"))

# 15. .isdigit() Checks if all characters are digits
number_text = "12345"
print(number_text.isdigit())

# 16. .isalpha() Check if all characters are letters.
name = "Florin"
print(name.isalpha())

# 17 .isalnum() Checks if all characters are letter OR numbers.
username = "Florin123"
print(username.isalnum())

# 18. Practical example: clean user input
user_input = "   FLORIN@EXAMPLE.COM   "
clean_email = user_input.strip().lower()
print(clean_email)

# .strip() removes spaces.
# .lower() converts the email to lowercase.
# You can chain string methods.
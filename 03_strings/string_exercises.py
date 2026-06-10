"""
String Exercises

What this file covers:
- Practice exercises with strings
- Combining string methods, indexing, slicing, and formatting
"""

name = "Florin"
print(name.upper())
# .upper() converts all letters to uppercase.

print(name.lower())
# .lower() converts all letters to lowercase.

print(len(name))
# len() returns the number of characters in a string.

print(name[0])
# Indexing starts from 0.
# name[0] gives the first character.

print(name[-1])
# Negative indexes start from the end.
# name[-1] gives the last character.

print(name[0:3])
# starts at position 0 and stops before index 3 so FLO index 0,1,2

message = "   Python is great   "
print(message.strip())
# .strip() removes spaces from the beginning and end.


sentence = "I am learning Python"
new_sentence = sentence.replace("Python", "Linux, SQL, Python")
print(new_sentence)
# .replace(old, new) replaces one part of a string with another.


text = "Python is really good for automation"
if "automation" in text:
    print("It's there")
else:
    print("It's not")
# The in operator checks if a value exists inside another value.


sentence = "Python SQL Git APIs"
words = sentence.split()
print(words)
# .split() breaks a string into a  list.
# by default, it splits by spaces

skills = ['Python', 'SQL', 'Git', 'APIs']
result = ", ".join(skills)
print(result)
# join combines a list into a string and it is separated by ", "

user_name = "Florin"
role = "QA Automation learner"
print(f"{user_name} is a genius Python expert that studies {role}")
# f-strings allow you to insert variables inside text

email = "florin@example.com"
if "@" and "." in email:
    print("Good")
else:
    print("bad")
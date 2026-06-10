"""
String Indexing and Slicing

What this file covers:
- Accessing characters by index
- Using positive and negative indexes
- Extracting parts of strings with slicing
"""
text = "Python"

# 1. Positive indexing
print(text[0])
print(text[1])
print(text[2])

# Explanation:
# Indexing starts from 0.
# P y t h o n
# 0 1 2 3 4 5


# 2. Negative indexing
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-5])

# Explanation:
# Negative indexing starts from the end.
# text[-1] is the last character.
# text[-2] is the second last character.


# 3. Basic slicing   [start: stop: step]
print(text[0:3])
# Explanation:
# text[0:3] means:
# start at index 0
# stop before index 3
# Result:
# Pyt


# 4. Slice from beginning
print(text[:3])
# Explanation:
# If start is missing, Python starts from the beginning.
# text[:3] is the same as text[0:3].

# 5. Slice to end
print(text[3:])
# if stop is missing python goes until the end
#output = hon


# 6. Full string copy
print(text[:])

# text[:] returns the full strin

# 7. Step slicing
print(text[::2])
# step - it means skip.


# 8. practical example: ticket ID
ticket_id = "INC123456"

prefix = ticket_id[:3]
number = ticket_id[3:]

print(prefix)
print(number)
# ticket_id[:3] extracts "INC".
# ticket_id[3:] extracts "123456".


# 10. Practical example: date string
date = "2026-06-10"

year = date[:4]
month = date[5:7]
day = date[8:10]
# This works because the date has a fixed format:
# YYYY-MM-DD


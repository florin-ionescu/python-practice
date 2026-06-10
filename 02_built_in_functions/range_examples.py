"""
range()

What this file covers:
- How range() works
- How to use range() in for loops
- start, stop, and step
- Common beginner examples
"""
# 1. Basic range
for number in range(5):
    print(number)
# range(5) generates numbers from 0 up to 5, but not including 5.

# 2. Range with start and stop

for number in range(1, 5):
    print(number)
# range(1, 6) starts at 1 and stops before 6.

# 3. Range with start, stop, and step
for number in range(0, 11, 2):
    print(number)
# range(0, 11, 2) means:
# start at 0
# stop before 11
# increase by 2 each time
# Output:

# 4. Countdown using range
for number in range(10, 0, -1):
    print(number)
# range(10, 0, -1) starts at 10 and goes down by 1.
# It stops before 0.

# 5. Repeat an action multiple times
for attempt in range(3):
    print("trying to connect...")
# range(3) repeats the code 3 times.
# This is useful for retries, login attempts, or repeated checks.

# 6. Use range with len()

skills = ["Python", "SQL", "Git"]
for index in range(len(skills)):
    print(index, skills[index])
# len(skills) returns 3.
# range(len(skills)) becomes range(3).
# That gives indexes:
# 0, 1, 2
#
# skills[0] is "Python"
# skills[1] is "SQL"
# skills[2] is "Git"

# 7. Better way to get index and value: enumerate()

for index, skill in enumerate(skills, start=1):
    print(index, skill)
# enumerate() is usually cleaner than range(len(...)).
# It gives both the index and the value directly.

# 8. Convert range to list
numbers = list(range(1, 6))
print(numbers)
# range() does not create a normal list immediately.
# list(range(1, 6)) converts it into:
# [1, 2, 3, 4, 5]

# 9. Create even numbers

even_numbers = list(range(2, 21, 2))

print(even_numbers)
# Explanation:
# Starts at 2.
# Stops before 21.
# Adds 2 each time.
# Result:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 10. Create odd numbers
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)
# Explanation:
# Starts at 1.
# Stops before 20.
# Adds 2 each time.
# Result:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# 11. Practical example: calculate total manually
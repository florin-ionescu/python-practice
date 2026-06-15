"""
BREAK AND CONTINUE IN PYTHON

break and continue are used inside loops.

They allow you to control how the loop behaves.

break:
- stops the loop completely

continue:
- skips the current iteration and moves to the next one
"""


# break stops the loop completely.
for letter in "python":
    if letter == "h":
        break
    print(letter)

# continue skips the current loop iteration and moves to the next one.
for letter in "python":
    if letter == "h": # when letter becomes "h", it is skipped and goes to next letter
        continue
    print(letter)

count = 0
while count < 10:
    count += 1
    if  count == 5:
        continue
    print(count)

'''
break = exit the loop.
continue = skip this round, go to the next round.
'''


# Practical example with break
tickets = ["INC001", "INC002", "INC003", "INC004"]
ticket_to_find = 'INC003'

for ticket in tickets:
    print(f'Checking ticket {ticket}')
    if ticket == ticket_to_find:
        print(f"Found ticket: {ticket}")
        break

attempts = 0
while True:
    attempts += 1
    print(f'Attempt {attempts}')

    if attempts == 3:
        print("Stopping loop")
        break
print(attempts)

# Using continue to skip invalid data
numbers =[10, 9, 2, 0 ,5]
for number in numbers:
    if number == 0:
        continue
    result = 100 / number
    print(result)


"""
WHEN TO USE BREAK

Use break when:
- you found what you were looking for
- continuing the loop is unnecessary
- you want to stop after a condition is met

Examples:
- stop searching after finding a ticket ID
- stop retrying after success
- stop reading data after a specific marker


WHEN TO USE CONTINUE

Use continue when:
- you want to skip invalid data
- you want to ignore certain values
- you want the loop to continue with the next item

Examples:
- skip closed tickets
- skip empty rows in a file
- skip invalid API responses
"""

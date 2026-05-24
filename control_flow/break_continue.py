# break and continue are used inside loops in Python.

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


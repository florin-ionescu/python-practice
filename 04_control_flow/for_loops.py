"""
FOR LOOPS IN PYTHON

A for loop is used to repeat code for each item in a sequence.

Common sequences:
- list
- tuple
- string
- dictionary
- range()
"""

'''
- A for loop is used to repeat a block of code a known number of times,
or to go through items in a collection such as a list, string, range, array, dictionary, or file.

for item in collection:
    do_something(item)
'''

grades = [90, 85, 78, 92, 88]
total = 0
amount = len(grades) #numarul de elemente din lista

for grade in grades:
    # total = total + grade adica total = 0 + 90 -> total = 90
    total += grade

print(total / amount)

total2 = sum(grades)
print(total2 / amount)

#range(5) va genera numere de la 0 la 4
for i in range(5):
    print(i)


word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(f'found {count} letters a') #put print outside loop to print only the final total

c = 0
c = word.count("a")
print(c)


# Using range()
"""
range() is commonly used when you want to repeat something
a specific number of times.
"""

for number in range(5):
    print(number)

# range(start, stop)
for number in range(1, 6):
    print(number)

# range(start, stop, step)
for number in range(1, 6, 2):
    print(number)

# Loop through a list and use conditions
scores = [55, 70, 88, 40, 95]
for score in scores:
    if score >= 70:
        print(f"{score} passing")
    else:
        print(f'{score} failed')

# Loop through a dictionary
user = {
    "name": "Florin",
    "role": "IT Support Engineer",
    "learning": "Python"
}
for key in user:
    print(key, user[key])

# Loop through a list with index
tickets = ["INC001", "INC002", "INC003"]
for index, ticket in enumerate(tickets, start=1):
    print(f'{index}: {tickets}')

# Practical example
ticket_statuses = ["open", "resolved", "open", "closed", "open"]
open_t = 0

for status in ticket_statuses:
    if status == "open":
        open_t += 1
print(f'Open tickets: {open_t}')


"""
WHEN TO USE FOR LOOPS

Use for loops when:
- you want to process every item in a list
- you want to repeat code a known number of times
- you want to read values from a dictionary
- you want to count, filter, or transform data

Examples:
- checking every ticket in a queue
- validating every item in a shopping cart
- reading every row from a CSV file
- testing multiple API responses
"""
# A list comprehension is a shorter way to create a new list from another sequence, like a list, range, string, etc.

# list comprehension:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers]
print(squares)

'''
STRUCTURE: 
[new_value for item in collection]
'''

'''
EXAMPLE:
[number * number for number in numbers] 

For each number in numbers, calculate number * number,
put the result into a new list.
'''

# you can also add an if condition

# Normal way
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print(evens)
print(odds)

# list comprehension way:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 != 0]
print(evens)
print(odds)
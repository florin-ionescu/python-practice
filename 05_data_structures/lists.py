#lists

numbers = [1, 2, 3, 4, 5]  #list of integers
doubled = [x*2 for x in numbers]

#for number in numbers:
    #doubled.append(number * 2)  #doubled = doubled + [number * 2]

print(doubled)

friends = ["Florin", "Andrei", "Mihai", "Ioana", "Maria"]
starts_with_m = [friend for friend in friends if friend.startswith("M")]

print(starts_with_m)
print(friends[0])  #first element
print(friends[-1])  #last element

#unpacking a list into variables
head, *tail = numbers

#first element
print(head)
print(tail)

#unpacking a list into variables using * to capture the rest of the elements
*head, tail = numbers

#all elements except the last one
print(head)

# list[start:stop:step]

numbers = [0, 1, 2, 3, 4, 5]
#start at index 1 stop before index 4
print(numbers[1:4])

# Omitting Start it just stops before index 3 and that's 0, 1, 2
print(numbers[:3])

# Omitting Stop - bellow example starts at position 2 until end of list skips 0, 1 and -> [2, 3, 4, 5]
print(numbers[2:])

# Full Copy - use : and result is [0, 1, 2, 3, 4, 5]
print(numbers[:])

# Using Step ::2 - output is [0, 2, 4] it jumps - take every 2nd element (using bellow example)
print(numbers[::2])

# Reverse a List - step = -1  reverse a list, move backward
print(numbers[::-1])

# Negative Indexing - Negative indexes count from the end. Output is  [3, 4, 5]
print(numbers[-3:])

# Slicing also works on strings.
text = "Python"
print(text[1:4])

# You can replace parts of a list.
num = [1, 2, 3, 4]

num[1:3] = [20, 30]
print(num)

"""
Why Slicing Is Useful

Slicing is heavily used for:

* data processing
* pagination
* reversing
* copying
* filtering patterns
* algorithms

<>! list[start:stop:step] !<>
"""
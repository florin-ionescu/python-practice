
# This is a tuple, not a list. A tuple is immutable, meaning it cannot be changed after it is created.
x = 5 , 6
print(type(x))

# This is also a tuple. The parentheses are optional when defining a tuple, but they can be used for clarity.
y = (5, 6)
print(type(y))

"""
A tuple is an ordered collection of items, similar to a list, but with one major difference:
*** Tuples are immutable. ***
"""

# You can also create single-element tuples: comma is important
single_elem_tuple = (5,)

# 1. Ordered - Tuples preserve insertion order. Elements stay in the same order.
t1 = ("a", "b", "c")
print(t[0])

# 2. Immutable - You cannot modify a tuple after creation.
t2 = (1, 2, 3)
# t[0] = 100   # ERROR TypeError

# 3. Allows Duplicate Values
t3 = (1, 1, 2, 3)
print(t3)

# 4. Can Store Multiple Data Types
# Tuples can contain: strings, integers, lists, booleans, other tuples, mixed types

# 5. Faster Than Lists: more memory efficient, slightly faster than lists because they are immutable.

# 6. Supports Indexing and Slicing
# Indexing
t6 = (10, 20, 30)
print(t6[1])

# Slicing
print(t[0:2])

# 7. Can Be Used as Dictionary Keys - Because tuples are immutable, they are hashable (if their contents are immutable too).
locations = {
    (10, 20): "Point A"
}

print(locations[(10, 20)])

# 8. Tuple Packing and Unpacking
# Packing
person = ("Bob", 30)

# Unpacking
name, age = person

print(name)
print(age)

# 9. Supports Nested Tuples
t9 = ((1, 2), (3, 4))

print(t9[1][0])

'''
When to Use Tuples

* data should not change
* representing fixed records
* returning multiple values from functions
* using dictionary keys
* protecting data from modification
'''

# An ordered, immutable collection that can store multiple values and supports indexing, slicing, and unpacking.
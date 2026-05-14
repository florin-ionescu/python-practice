# Sets built-in data type used to store a collection of unique items.

'''
Key features of Sets:
* No duplicate value
* Unordered (items do not have a fixed position)
* Mutable (you can add/remove items)
'''

# Creating a Set
numbers = {1, 2, 3, 4}
print(numbers)

# Duplicate Values Are Removed
nums = {1, 2, 2, 3, 3, 4}
print(nums)

# Empty Set - it creates a dictionary, not a set
my_set = set()

# Add an Item
fruits = {"apple", "banana"}
fruits.add("orange")

print(fruits)

# Set Operations Union (|)
# Union (|) Combines all unique items.
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

# Intersection (&)  Common items only.
print(a & b)

# Difference (-) - Items in first set but not second.
print(a - b)

# Symmetric Difference (^)  Items in either set, but not both.
print(a ^ b)

# Remove duplicates from a list
name_list = ["Florin", "Bogdan", "Alexandra", "Florin", "Bogdan"]
unique_names = set(name_list)
print(unique_names)

# Set → Unordered -> Mutable (Sets can be modified.) -> Set Removes Duplicates Automatically -> Set Does NOT Support Indexing

"""
Use Set When:
-> uniqueness matters
-> removing duplicates
-> fast lookup needed
-> mathematical set operations
"""

# A set is an unordered collection of unique mutable elements optimized for fast lookup.
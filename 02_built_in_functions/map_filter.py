# map() applies a function to each item

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda number: number ** 2, numbers))
print(squared)

# list comprehension is often easier:
sqaured_ls = [number ** 2 for number in numbers]
print(sqaured_ls)
def multiply(*args):
    print(args)
    total = 1
    for num in args:
        total *= num
    print(total)

multiply(1, 2, 3)  # Output: (1, 2, 3)

def add(x, y):
    return x + y
nums = [1, 2]
print(add(*nums))  # Output: 3
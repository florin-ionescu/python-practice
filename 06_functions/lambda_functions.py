#function that add two numbers
def add(x, y):
    return x + y
print(add(5, 3))

#DOES THE SAME THING AS THE ABOVE FUNCTION
lambda_add = lambda x, y: x + y
print(lambda_add(5, 3))

#map goes over each element in the list and applies the function to it

nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]
print(evens)
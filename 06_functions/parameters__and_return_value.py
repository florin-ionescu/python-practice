# In Python, parameters and return are used with functions.

# Parameter: A parameter is a variable inside a function that receives a value.
def greet(name):
    print("Hello", name)
greet("Florin")

# Multiple parameters
def add(a, b):
    print(a + b)

add(3, 5)

# return sends a value back out of the function.
def add(a, b):
    return a + b
result = add(3, 5)
print(result)

# Difference between print and return: print only shows something on the screen.

'''
Easy way to remember:
A parameter is input going into a function.

return is output coming back from a function.
'''
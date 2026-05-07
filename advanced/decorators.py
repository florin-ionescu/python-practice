#A decorator is a function that modifies another function without changing its original code.
def greet():
    print("Hello")

def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

greet = decorator(greet) #greet is now the wrapper function returned by the decorator

#decorators exist to help avoid repeating code
#The @ Syntax is a syntactic sugar for applying decorators to functions. It allows you to apply a decorator to a function in a more concise and readable way.

@decorator
def greet():
    print("Ce faci?")

greet()
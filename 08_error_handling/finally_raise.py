# finally and raise are used with errors/exceptions in Python.

# finally means: run this code no matter what happens.
try:
    number = int(input("Enter a number: "))
    print(10/number)
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("This always runs")

# raise means: create an error on purpose.
age = 15
if age < 18:
    raise ValueError("You are underage")
# output ValueError: You are underage

# You use raise when your program finds something invalid and you want to stop or warn clearly.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    return a / b
print(divide(2,3))
print(divide(10, 0))

# output  ZeroDivisionError: You cannot divide by zero


try:
    age = 15

    if age < 18:
        raise ValueError("Too young")

    print("Access allowed")

except ValueError as error:
    print("Error:", error)

# output: Error: Too young and doesnt stop the code

'''
Easy way to remember:
raise = throw/create an error.

finally = always run this at the end.
'''
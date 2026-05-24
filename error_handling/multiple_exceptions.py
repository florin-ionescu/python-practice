# Multiple exceptions means handling different types of errors in different ways.

'''
Basic structure:
try:
    # code that might cause an error
except ErrorType1:
    # handle first error
except ErrorType2:
    # handle second error
except ErrorType3:
    # handle third error
'''

try:
    number = int(input("Enter a number: "))
    result = 10/ number
    print(result)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Division by zero")

# Sometimes you want the same message for different errors.
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except (ValueError, ZeroDivisionError):
    print("Invalid input")

# Using as error: You can store the actual error message in a variable:
try:
    n = int(input("Enter a number: "))
    print(10 / n)
except ValueError as error:
    print("Value Error:", error)
except ZeroDivisionError as error:
    print("Division by zero:", error)

'''
Easy way to remember:
If this error happens, do this.
If that error happens, do that.
If another error happens, do something else.
'''
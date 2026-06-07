# WHILE Loops

"""
A while loop repeats code as long as a condition is true.

while condition:
    # code to repeat

"""

count = 1

while count <= 5:
    print(count)
    count += 1


password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")


number = 5

while number > 0:
    print(number)
    number -= 1

print("Go!")
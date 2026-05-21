#work in progress

# if means: check this condition first
# elif means: otherwise, check this other condition
# else means: if none of the conditions above were true, do this

age = 18

if age < 18:
    print("Minor")
elif age == 18:
    print("Happy Birthday")
else:
    print("Adult")

'''
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False,
    # but condition_2 is True
else:
    # runs if none of the above conditions are True
'''



while True:
    name = input("What is your name? (Type stop to exit): ")

    if name.lower() == "stop":
        break

    if name.lower() == "florin":
        print("Welcome, Boss")
    elif name.lower() == "cichicean":
        print("Hello, Master")
    else:
        print("No idea who you are, buddy!")
# Control flow means the program can choose different paths depending on conditions.

age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative")
elif age < 13:
    print("You are a chiled")
# This condition is checked only if age is NOT less than 13.
# So this means age is between 13 and 17.
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior.")
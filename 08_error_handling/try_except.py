"""try:
    The things you want the code to do
except Exception:
    What to do if it can't do what you want it to do
"""

try:
    # Open file and show its name.
    the_file = open('people.csv')
    print(the_file.name)
except Exception:
    print("Sorry, I don't see a file named people.csv here")

try:
    # Open file and show its name.
    the_file = open('people.csv')
    print(the_file.name)
    print(the_file.wookems())
except FileNotFoundError:
    print("Sorry, I don't see a file named people.csv here")
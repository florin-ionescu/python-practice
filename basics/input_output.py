#Input = information the program receives
#Output = information the program shows or returns

name = input("What is your name? ")

#input() ALWAYS returns a string (str). Even if a number is typed

age = input("How old are you? ")
print(type(age))

print("Hello", name)

print("My name is ", end="")
print("Monty Python.")

print("My name is\nFlorin Ionescu")


#The keyword argument that can do this is named sep (like separator).
print("My", "name", "is", "Monty", "Python.", sep="-")

print("I'm Monty Python.")
print('I\'m Monty Python.')

#output using print() function

#Function output return Send value back to the caller.


#visual analogy print shows the output on the screen, while return sends the value back to the caller, which can be used later in the program.
#print() => "Coffee ready!" while return "The machine HANDS YOU the coffee." and you can use it elsewhere.


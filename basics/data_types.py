#data types

#integer - int = whole numbers
age = 37
print(age)
print(type(age))

#float = decimal numbers
height = 1.83  #float
print(height)
print(type(height))

#string - str = text with "" or ''
name = "Florin"
print(name)
print(type(name))

#boolean - bool = True or False
true_value = True
false_value = False
print(true_value)
print(false_value)

"""The name comes from George Boole (1815-1864), the author of the fundamental work, The Laws of Thought, 
which contains the definition of Boolean algebra - a part of algebra which makes use of only two distinct values: True and False, denoted as 1 and 0.
"""

#“Empty” → False   #use bool() to check the truth value of an expression
print(bool("")) #this is False
print(bool(0)) #this is False
#“Non-empty” → True
print(bool("This is True"))

learning_python = "My name is " + name + " and I am learning Python. I am " + str(age) + " years old and my height is " + str(height) + " meters. This is " + str(true_value) + "!!"
print(learning_python)

calculation = age + height
print(calculation)


# remainder (modulo)
print(14 % 4)
"""
14 // 4 gives 3 → this is the integer quotient;
3 * 4 gives 12 → as a result of quotient and divisor multiplication;
14 - 12 gives 2 → this is the remainder.

"""
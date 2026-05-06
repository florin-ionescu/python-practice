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

#“Empty” → False   #use bool() to check the truth value of an expression
print(bool("")) #this is False
print(bool(0)) #this is False
#“Non-empty” → True
print(bool("This is True"))

learning_python = "My name is " + name + " and I am learning Python. I am " + str(age) + " years old and my height is " + str(height) + " meters. This is " + str(true_value) + "!!"
print(learning_python)

calculation = age + height
print(calculation)


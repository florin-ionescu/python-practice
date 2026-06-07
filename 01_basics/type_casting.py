"""Common Type Casting Functions
int() = integer
float() = converts to decimal number
str() = string
bool() = boolean
"""

#Type casting = convert the data type of a value to another data type
age = input("How old are you? ")
convert_to_integer = int(age)
print(type(convert_to_integer))

convert_to_float = float("3.14")
print(convert_to_float)

convert_to_string = str(convert_to_integer)

print(type(convert_to_string))

#convert_to_boolean = bool(0)
print(bool(0)) #this is False
print(bool("")) #this is False
print(bool("This is True")) #this is True

#explicit type casting = when the programmer manually converts a value from one data type to another using a built-in function like int(), float(), str(), or bool().
#implicit type casting = when Python automatically converts a value from one data type to another without the programmer explicitly requesting it. This can happen in certain situations, such as when performing operations between different data types. For example, if you add an integer and a float together, Python will automatically convert the integer to a float before performing the addition.

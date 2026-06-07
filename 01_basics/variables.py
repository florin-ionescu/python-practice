name = "Florin"
age = 36
height = str(1.83) + "m"

print(name)
print(height)

agent = (f"My name is {name} and I am {age} years old. I am {height} tall.")
print(agent)

# Variables can be reassigned
name = "Ionescu"
print(name)

# Variable names can contain letters, numbers and underscores, but they cannot start with a number
first_name = "Florin"
last_name = "Ionescu"

full_name = first_name + " " + last_name
print(full_name)

#camelCase is a common convention for variable names in some programming languages, but in Python, the convention is to use snake_case, which means using lowercase letters and underscores to separate words.
#snake_case_variable = "This is a variable in snake_case"
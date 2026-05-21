# Dict

#uses key and value pairs to store data.
this_is_a_dictionary = {"key" : "value", "key2" : "value2"}


my_dictionary = {
    "name" : "Florin",
    "age" : 37,
    "height" : 1.83,
    "is_student" : True
}

#accessing value by key
print(my_dictionary["name"])
print(this_is_a_dictionary["key"])

my_dictionary["sport"] = "Aikido"
print(my_dictionary)

for key in my_dictionary:
    # prints the keys of the dictionary
    print(key)

print(my_dictionary["sport"])
print(my_dictionary.get("name"))

# Dictionaries are great when you want to look something up by name, ID, label, or category.

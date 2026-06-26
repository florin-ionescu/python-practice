# A data structure is a way to organize and store data.

# A list is an ordered collection of values.
# Lists use square brackets: []

students = ["Ana", "Mihai", "Elena", "Andrei"]
print("Students", students)
print("First student", students[0])
students.append("Florin")
print("after adding Florin", students)

students.remove("Mihai")
print("Removed Mihai", students)


# A dictionary stores data as key-value pairs.
# Dictionaries use curly braces: {}
student_grades = {
    "Ana": 9,
    "Elena": 10,
    "Andrei": 8,
    "Ioana": 9
}

print("Student grades", student_grades)

# Access a value using its key.
print("Ana's grade:", student_grades["Ana"])

# update existing value
student_grades['Andrei'] = 5

# Add a new key-value pair.
student_grades["Vlad"] = 8

print(student_grades)


# A tuple is similar to a list, but it cannot be changed.
# Tuples use parentheses: ()
coordinates = (10, 20)
print("Coordinates", coordinates)


# A set stores unique values.
# Sets also use curly braces: {}
unique_numbers = {1, 2, 2, 3, 4, 4, 5, 5, 5, 5}
# Duplicate values are automatically removed.
print("Unique numbers:", unique_numbers)
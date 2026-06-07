# 1. Basic file reading

# with -> automatically closes the file after reading.
with open("notes.txt", "r") as file:
    content = file.read() # opens the file in read mode.

print(content)


# 2. Read file line by line

# This prints each line one by one. Very useful for logs, reports and automation
with open("notes.txt", "r") as file:
    for line in file:
        print(line)

with open("notes.txt", "r") as file:
    for line in file:
        # .strip() removes extra spaces and the newline \n.
        print(line.strip())

# 3. Read all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()
print(lines)

# Output without \n
with open("notes.txt", "r") as file:
    lines = file.read().splitlines()
print(lines)

# 4. Handle file not found error
# If the file does not exist, Python gives an error. Use try/except:
try:
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found")
    #This is important for automation projects.

'''
"r"  read file
"w"  write file, overwrites existing content
"a"  append to file
'''
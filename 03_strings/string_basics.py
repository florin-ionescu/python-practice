# Work in progress

# text.startswith("abc")

# text.endswith("abc")

def solution(text, ending):
    return text.endswith(ending)

print(solution("kamehameabc", "abc"))


# string.split() this turns a string into a list of strings ["hello", "world", "from", "python"]


# text.title() turns hello world into Hello World


words = ["Hello", "World"]

" ".join(words) #output = Hello World


'''
"ERROR" in text  (Checks if text contains something.)

"ERROR" in "ERROR database failed"
Output: True

'''

# text.count("ERROR")
# Counts how many times something appears.
"ERROR ERROR WARNING".count("ERROR")
#output: 2


# text.strip() removes spaces and newlines from both ends
# "  hello".lstrip()  removes spaces from left
# text.rstrip()  "hello\n".rstrip() Removes spaces/newlines from the right.

# REPLACE TEXT text.replace("old", "new")

# text.isdigit()  # Checks if the string contains only numbers.

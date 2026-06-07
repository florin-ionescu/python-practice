# reversed() gives items in reverse order.

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)

# strings
word = "python"

reversed_word = "".join(reversed(word))

print(reversed_word)  # nohtyp


# iterable is anything that you can loop over using a for loop (lists, tuples, strings, sets and dict)

# sequence strings lists

countries = ["Romania", "Italy", "France", "Germany", "Hungary", "Japan", "USA"]
countries.reverse()
print(countries)

nume = "aca"
reversed_nume = " ".join(reversed(nume))
print(reversed_nume)

reversed_countries = list(reversed(countries))
print(reversed_countries)

# Slicing - creates a reversed copy of a sequence
print('Japan'[::-1])

# palindrome
nume_invers = "".join(reversed(nume))
print(nume_invers)
if nume_invers == nume:
    print("Palindrome")
else:
    print("Not Palindrome")

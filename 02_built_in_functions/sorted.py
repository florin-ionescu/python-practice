

numbers = [10, 4, 25, 7, 18]

sorted_numbers = sorted(numbers)

print(sorted_numbers)  # [4, 7, 10, 18, 25]
print(numbers)         # original list unchanged

# Descending order:
print(sorted(numbers, reverse=True))  # [25, 18, 10, 7, 4]

countries = ["Romania", "Italy", "France", "Germany", "Hungary"]
reverse_c = sorted(countries, key=lambda x: len(x), reverse=True)
print(reverse_c)
print(countries) 
numbers = [1,2,3,4,5,6,7,8,9,10]

# all() → validate all API users have email
# all() - everything must be True in order to pass as True
print(all(number % 2 == 0 for number in numbers))

# any() → check if any log line contains "ERROR"
# any() - it is True even if some situations are False
print(any(number > 5 for number in numbers))
print(any(number < 5 for number in numbers))
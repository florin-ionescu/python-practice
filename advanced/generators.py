# Generators are a Python feature that let you produce values one at a time, instead of creating all values at once.
# Generator uses yield

def get_numbers():
    yield 1
    yield 2
    yield 3

# Output = <generator object get_numbers at ...>
numbers = get_numbers()
print(numbers)

# Because numbers is now a generator object. To get the values, you loop over it:
for number in get_numbers():
    print(number)

# yield pauses the function and remembers where it stopped.

'''
return = finish function and give back one result
yield  = pause function and give back the next result

A generator is especially good for reading files, processing large data, 
or creating sequences where you do not need everything at once.
'''

def count_up_to_three():
    print("Start")
    yield 1

    print("Continue")
    yield 2

    print("End")
    yield 3

gen = count_up_to_three()
print(next(gen)) # gives one value at a time -> Output Start 1
print(next(gen))
'''
- each yield gives back a value and pauses the function.
- The next time Python asks for another value, the function continues from where it stopped.
'''
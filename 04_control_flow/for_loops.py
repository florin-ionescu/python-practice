#for

'''
- A for loop is used to repeat a block of code a known number of times,
or to go through items in a collection such as a list, string, range, array, dictionary, or file.

for item in collection:
    do_something(item)
'''

grades = [90, 85, 78, 92, 88]
total = 0
amount = len(grades) #numarul de elemente din lista

for grade in grades:
    # total = total + grade adica total = 0 + 90 -> total = 90
    total += grade

print(total / amount)

total2 = sum(grades)
print(total2 / amount)

#range(5) va genera numere de la 0 la 4
for i in range(5):
    print(i)


word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(f'found {count} letters a') #put print outside loop to print only the final total

c = 0
c = word.count("a")
print(c)


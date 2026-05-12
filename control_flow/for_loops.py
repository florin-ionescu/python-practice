#for loops

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
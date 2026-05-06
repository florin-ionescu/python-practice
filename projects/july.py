
# eu """ this is a docstring
"""This is a multiline comment in Python
This type of comment is sometimes called a docstring.
A docstring starts with three double-quotation marks, and also ends with
three double quotation marks. """

print(type(-6.0))
x = 'Florin\'s cat'
print(x)
y = "Pe mine ma cheama Dorel \nsunt baiat destept\nsi cu capul chel"
print(y)

# modulus % este ce ramane dupa ce imparti la un numar 11 % 5 = 1 adica
# exponent adica 3**2 inseamna 3 la puterea a doua
print(3 ** 3)
# floor division // 9//5 inseamna 1 pentru ca 9/5 = 1.8 adica ce este dupa . se sterge si ramane doar integerul
# operatori +-==//**/% < > <= => != is (comparison operators) is not
# or and not  boolean operators

#camel case florinIonescu preferabil under_score (underscore)
# = assignment operator
# == equality operator
# != not equal operator
# > greater than operator
# < less than operator
# >= greater than or equal to operator
# <= less than or equal to operator

xz= 51
unit_price = 100.2
print(f"Subtotal: ${xz * unit_price:,}")   #intr-un f string adaugi la final :, pentru a adauga separator de mii
print(f"Subtotal: ${xz * unit_price:,.2f}") # adaugi dupa , .2f pentru a limita la 2 zecimale
taxe = 0.19
print(f"Taxe: {taxe:.0%}") # adaugi dupa . 2% pentru a afisa procentul cu 2 zecimale
#\n inseamna new line adica o linie noua

sun = "nu"
if sun == "soare": print("Este o zi frumoasa")
else: print("Este o zi innorata")

answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done")

cc = 55
while cc < 65:
    print(cc)
    cc += 15

students = ["Mark", "AmBer", "ToDd", "AnIta", "Sandy"]
print(len(students))
students.append("Florin")
print(students)

if "Smiorchi" in students: print("Smiorchi is in the class")
else: students.append("Smiorchi")
print(students)
if "Smiorchi" in students: print("Smiorchi is in the class")
students.sort(key=lambda s: s.lower())
print(students)
print(students.reverse())
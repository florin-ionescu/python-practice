#string concatenation - how to put strings together
# 3 modalitati de a scrie acelasi lucru
# youtuber = "Florin"
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f'subscribe to {youtuber}')
adj = input("Adjectiv: ")
verb = input("Verb: ")
verb2 = input("Verb:")
adj2 = input("verb: ")


madlib = (f"Hamsterul este atat de {adj}! Ii place sa fuga si sa {verb}. Cand nu {verb2} el nu face decat sa se {adj2}")

print(madlib)

#reverse sort
a = ["Mountain","Valley","River","Sky"]
b = [3,7,22,1,43]
b.sort(reverse = True)
a.sort(reverse = True)
print(a)
print(b)

#combining lists
list1 = ["Tomatoes", "Potato", "Onion"]
list2 = ["Apple", "Banana", "Watermelon"]
x = list1 + list2
print(x)

#to clear and remove item from a list

c = ["Sun","Moon","Water","Sand","Air"]
c.pop( 3 )
print(c)
c.clear()
print(c)
#We can use the append() method to add an element at the end of a list.

# On the flip side if we want to remove the last element of a list /
# we use the pop() method without providing any index.
planet = ["Venus", "Earth", "Mars"]
planet.append("Jupiter")
print(planet)
planet.pop()
print(planet)

#The values() method will return a list of all the values in the dictionary.
#The items() method will return each item in a dictionary, as (key, value) tuples in a list.

#The pop() method removes the item with the specified key name:
# The del keyword removes the item with the specified key name and can also delete the whole dictionary
# The clear() method empties the dictionary:
c = {"Ferrari":1967,"Honda":2001,"Ford":2016}
c.pop("Ford")
print(c)
c.clear()
print(c)

# With the "continue" statement we achieve the following

# We can stop the current iteration of the loop
# We continue with the next element.
# That is, we will not go any further in this particular iteration, and instead skip to the next iteration.

# However, it is also possible to specify the increment value by adding a third parameter.
#
# For eg - range(2, 30, 3)
# With the third parameter, the loop will add increment by
# 3 instead of the default
i = 20
for i in range(20,45, 2 ):  # 2 de aici inceamna 20 +2 22 +2 ...pana la 45
  print( i )

# "break" functions differently from "continue" that we learnt earlier
# "break" exits the loop completely and goes to the next section of the program
# "continue" exits the current iteration and skips the code remaining in the current loop iteration.
# However, the "for" or "while" loop continues with the next iteration.

def reverse_seq(n):
    return list(range(n, 0, -1))

print(reverse_seq(4))

#sau
def countdown(n):
    if n < 1:
        return []
    return [n] + countdown(n-1)



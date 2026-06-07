
def greet(name, surname):
    print(f"Hello, {name} {surname}!")

greet("Florin", "Ionescu")

nume = ["Florin", "Marius", "Andrei", "Alexandru", "Cristian"]

def add_friend(nume):
    friends_name = input("Enter the name of your friend: ")
    nume.append(friends_name)
    print(f"{friends_name} has been added to your friends list.")

add_friend(nume)

def add(x, y):
    result = x + y
    print(result)
add(5, 10)

print(nume)


#decorators = Decorators în Python sunt o modalitate de a modifica sau extinde comportamentul unei funcții (sau metode) fără să îi schimbi codul direct.


def find_uniq(arr):

    for n in set(arr):
        if arr.count(n) == 1:
            return n
arr1 = [1, 1, 1, 2, 1, 1]
print(find_uniq(arr1))
print(set(arr1))
print(arr1.count(1))

def replace_word():
    str = "Hi guys, I am Florin"
    word_to_replace = input("Word to replace: ")
    word_replacement = input("Enter a word to replace with: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()


def add(a, b):
    ans = a + b
    print(str(a) + " + " + str(b) + " = " + str(ans))
def sub(a,b):
    ans = a - b
    print(str(a) + " - " + str(b) + " = " + str(ans))
def mul(a,b):
    ans = a * b
    print(str(a) + " * " + str(b) + " = " + str(ans))
def div(a,b):
    ans = a / b
    print(str(a) + " / " + str(b) + " = " + str(ans))

while True:
    print("A - Add")
    print("S - Subtract")
    print("M - Multiply")
    print("D - Divide")
    print("E - Exit")

    choice = input("Choose ASMDE ")
    if choice == "a" or choice == "A":
        print("addition")
        a = int(input("first number "))
        b = int(input("2nd number "))
        add(a,b)
    elif choice == "s" or choice == "S":
        print("subtraction ")
        a = int(input("first number "))
        b = int(input("2nd number "))
        sub(a, b)
    elif choice == "c" or choice == "M":
        print("multiplication ")
        a = int(input("first number"))
        b = int(input("2nd number"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("divide")
        a = int(input("first number"))
        b = int(input("2nd number"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program end")
        quit()
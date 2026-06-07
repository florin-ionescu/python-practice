
import random
top_of_range = input("Scrie un numar (intre 0 si numarul scris te tine trebuie ghicit): ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Baga un numar mai mare de 0 data viitoare.")
        quit()
else:
    print("Baga un numar mai mare de 0 data viitoare.")
    quit()

random_number = random.randint(0,top_of_range)  #nu o sa includa ultima cifra adica 11 => randint include pe toate
# print(random_number)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Ghiceste numarul: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Trebuie sa scrii un numar.")
        continue
    if user_guess == random_number:
        # print("You got it")
        break
    # else:
    #     print("Wrong!")
    elif user_guess > random_number:
        print("Esti pe aproape. Scrie un numar mai mic")
    else:
        print("Esti pe aproape. Scrie un numar mai mare!")

print("Ai ghicit in", guesses, "incercari")
import random
guess = input("baga un numar de la 1 la 10")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input("Guess a number between 1 and {x}: ")
        if guess < random_number:
            print("Wrong, too low")
        elif guess > random_number:
            print("Wrong, too high, try again!")


    print(f"Grats. You have guessed the number {random_number} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess +1
    print(f"GG! Computer guess {guess}, correctly")

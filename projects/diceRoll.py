import random

def roll_dice():
    roll = input('Dai cu zarul? (Da/Nu): ')
    while roll.lower() == "Da".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print('Ai dat cu zarul: {} si {}'.format(dice1, dice2))

        roll = input("Mai dai cu zarul? (Da/Nu): ")

    print("Seionara!")
roll_dice()
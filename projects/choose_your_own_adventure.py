
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are at a crossroad choose your path - left or right? ")
if answer == "left":
    answer = input("You come to a river, you can walk around or swim? Type walk to walk and swim to swim.")
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You are dehydrated for walking in the desert, you died!. ")
    else:
        print("Not a valid option. You lost!")
elif answer == "right":
    answer = input("You came to a bridge - cross or go back? ")
    if answer == "back".lower:
        answer = input("You lost!")
    elif answer == "cross":
        answer = input("You cross the bridge and met a stranger. Talk to him? Yes or no?.")
        if answer == 'yes':
            print("The stranger rewarded you with gold. You win!")
        elif answer == 'no':
            print("Stranger ignored and you were robbed by strangers ahead. You lose.")
        else:
            print("You lose for not choosing a valid option")
    else:
        print("Not a valid option. ")


else:
    print("Not a valid option. You lose.")


print("Thank you for trying!")
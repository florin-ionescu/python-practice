
print("Welcome to... ")
playing = input('Do you want to play? ')

if playing.lower() != "yes":
    quit("bye bye!")

print("Ok! Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong answer!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong answer!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Wrong answer!")

answer = input("Who does kamehameha? ")
if answer.lower() == "goku":
    print("Correct")
    score += 1
else:
    print("Wrong answer!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4 ) * 100) + "%. right.")
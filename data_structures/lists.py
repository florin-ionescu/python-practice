#lists

numbers = [1, 2, 3, 4, 5]  #list of integers
doubled = [x*2 for x in numbers]

#for number in numbers:
    #doubled.append(number * 2)  #doubled = doubled + [number * 2]

print(doubled)

friends = ["Florin", "Andrei", "Mihai", "Ioana", "Maria"]
starts_with_m = [friend for friend in friends if friend.startswith("M")]

print(starts_with_m)
print(friends[0])  #first element
print(friends[-1])  #last element

#unpacking a list into variables
head, *tail = numbers

#first element
print(head)
print(tail)

#unpacking a list into variables using * to capture the rest of the elements
*head, tail = numbers

#all elements except the last one
print(head)
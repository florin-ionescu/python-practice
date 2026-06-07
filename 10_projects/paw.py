def remove_char(s):
    return s[1:len(s)-1]

print(remove_char("cichicean"))


help(len)

def remove_char(s):
    name = s.strip(s[0]) + s.strip(s[-1])
    return name

print(remove_char("silvica"))


#ca sa scoti primul si ultimul caracter
def remove_char(s):
    return s[1 : -1]

print(remove_char("silvica"))


def isPalindrome(s):
    return s == s[::-1]

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
def abbrev_name(name):
    return ".".join([w[0].upper() for w in name.split()])
# sau
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


# // rotunjeste
print(10.124 // 2.312)


def century(year):
    return (year + 99) // 100

lista0 = ["Telescopes", "Glasses", "Eyes", "Monocles"]
def sort_by_length(arr):
    return sorted(arr, key=len)
print(sort_by_length(lista0))

def points(games):
    n=0
    for i in games:
        temp = i.split(':')
        n1=int(temp[0])
        n2=int(temp[1])
        if n1>n2:
            n+=3
        elif n1==n2:
            n+=1
    return n
xxxx = ['1:0','3:2','3:3','4:1','2:2','4:3','1:4','2:3','2:4','4:4']
print(points(xxxx))

zzz = "Asa:merge:splitul:in:python"
print(zzz.split(":"))
print(list(zzz))

print(len(zzz))
print(zzz.count("Asa"))

def sum_two_smallest_numbers(numbers):
    numbers.sort(reverse=True)
    a=numbers.pop()
    b=numbers.pop()
    return a+b

print(sum_two_smallest_numbers([4,3,2,1]))


nr = [1,3,4,6,6,7,9]
xyz = nr.sort(reverse=False)
print(xyz)

print(zzz.find("merge"))

strg = "asta e un string"
print(strg.split())




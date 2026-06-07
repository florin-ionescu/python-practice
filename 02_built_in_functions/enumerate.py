# Enumerate - Useful when you need index + value:

names = ['Florin', 'Cristina', "Smiorchi", "Inky"]

for index, name in enumerate(names, start=1):
    print(index, name)


countries = ["Romania", "Italy", "France", "Germany"]
for index in range(len(countries)):
    print(f"{index+1} - {countries[index]}")

for item in enumerate(countries, start=1):
    print(item)

for index, country in enumerate(countries, start=1):
    print(f"{index}. {country}")
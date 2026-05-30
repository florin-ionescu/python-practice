from itertools import zip_longest

# zip() - Useful for combining lists:

names = ['Florin', 'Cristina', "Smiorchi", "Inky"]
scores = [10, 20, 30, 40, 50]

for name, score in zip(names, scores):
    print(name, score)

# enumerate() → number menu options in CLI app
# zip() → combine names + scores / columns + values

countries = ["Romania", "Italy", "France", "Germany", "Hungary", "Japan", "USA"]
capitals = ["Bucharest", "Rome", "Paris", "Berlin"]

for country, capital in zip(countries, capitals):
    print(f'The capital of {country} is {capital}')


for country, capital in zip_longest(countries, capitals, fillvalue="Unknown"):
    print(f'The capital of {country} is {capital}')
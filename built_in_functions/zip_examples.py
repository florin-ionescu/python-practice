# zip() - Useful for combining lists:

names = ['Florin', 'Cristina', "Smiorchi", "Inky"]
scores = [10, 20, 30, 40, 50]

for name, score in zip(names, scores):
    print(name, score)

# enumerate() → number menu options in CLI app
# zip() → combine names + scores / columns + values
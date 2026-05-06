# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('hamster', 0))
#
# print(counts)


# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])



d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k, i) in d.items():
    print(k, i)
print(max(d))

# tuples are related to dict
(a, y) = (4, "fred")
print(y)


#sorting lists of tuples

# d = {"a":10, "b":1, "c":22}
# d.items()
# dict_items([("a", 10), ("c", 22), ("b", 22)])


lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
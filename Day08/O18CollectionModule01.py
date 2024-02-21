
from collections import Counter, OrderedDict, defaultdict, ChainMap

st = "aabcaabccbbcabccbb"

res = Counter(st)

print(res)

print("Oredered Dictionary".center(60,"-"))
# it remembers the order in which the keys were inserted

d1 = {}
d1['name'] = "Slater"
d1['age'] = 34
d1['desig'] = "MGR"
d1['dept'] = "MKT"
d1['loc'] = "Che"

print("normal Dictionary.....")
for key, value in d1.items():
    print(key, "\t", value)

d2 = OrderedDict()
d2['name'] = "John"
d2['age'] = 32
d2['desig'] = "TL"
d2['dept'] = "Accounts"
d2['loc'] = "Del"

print("-" * 60)
print("oredered Dictionary.....")
for key, value in d2.items():
    print(key, "\t", value)

print("default Dictionary".center(60, "-"))
# default_factory is a function that provides the default value for the dictionary #created.  If this parameter is absent then the KeyError is raised.

d1 = defaultdict(int)
l = [1, 2, 3, 4, 2, 4, 1, 2]
print(f"l :{l}")

for i in l:
    d1[i] += 1      # d[1] = 1
    print(d1)


print(d1)

print("-" * 60)

d2 = defaultdict(list)

for i in range(5):
    d2[i].append(i)
    d2[i].append(i+1)


print(f"d2 :{d2}")

print("Chain Map".center(60, "-"))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

print(f"d1 :{d1}")
print(f"d2 :{d2}")
print(f"d3 :{d3}")

res = ChainMap(d1, d2, d3)
print(f"res :{res}")

print(res['a'])
print(res['f'])

print("-" * 60)
print(res.keys())

print("-" * 60)
print(res.values())

for i in res.keys():
    print(i)

print("-" * 60)
for j in res.values():
    print(j)

print("-" * 60)
d4 = {'g': 7, 'h': 8}
res = res.new_child(d4)
print(f"res :{res}")
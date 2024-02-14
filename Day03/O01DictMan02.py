
print("get".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 125, 'oppn': 'Eng'}
print(f"player :{player}")
print(f"Name :{player['name']}")
print(f"Runs :{player.get('run', 'Please mention the correct Key')}")
print(f"Runs :{player.get('runs')}")

print("setdefault".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 125, 'oppn': 'Eng'}
print(f"player :{player}")

player.setdefault("runs", 50)               # already existing
player.setdefault('venue', "Oval")          # new key
player.setdefault("name", "Sehwag")
print(f"player :{player}")

print("keys".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 125, 'oppn': 'Eng'}
print(f"player :{player}")

k = player.keys()
print(k)
print("-" * 60)

for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 125, 'oppn': 'Eng'}
print(f"player :{player}")

v = player.values()
print(f"values :{v}")

print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")

# convert the list into a dictionary - list elements will become the keys
res_dict = dict.fromkeys(cities)
print(f"res_dict :{res_dict}")
res_dict = dict.fromkeys(cities, 24)
print(res_dict)

print("pop".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 125, 'oppn': 'Eng'}
print(f"player :{player}")

ret = player.pop('age')
print(f"return :{ret}")

# ret = player.pop()
# print(f"return :{ret}")
print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'Rahul', 'age': 32, 'runs': 125, 'oppn': 'Eng'}
print(f"player :{player}")

ret = player.popitem()
print(f"return :{ret}")
print(f"player :{player}")

# d1 = {}
# d1.popitem()

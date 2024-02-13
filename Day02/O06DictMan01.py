
d1 = dict()         # empty dictionary
print(f"d1 :{d1}")
print(type(d1))
print("-" * 60)

d2 = {'name': 'sachin', 'age': 35, 'runs': 150, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict({'name': 'sourav', 'age': 36, 'runs': 80, 'oppn': 'SA'})
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='rahul', age=34, runs=45, oppn='NZL')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
d5 = dict([('name', 'sehwag'), ('age', 30), ('runs', 105), ('oppn', 'pak')])
print(f"d5 :{d5}")
print(type(d5))

# CRUD
player = {'name': 'Sachin', 'age': 34, 'runs': 98, 'oppn': 'WI'}
print(f"player :{player}")

# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iterate
for i in player:
    print(f"{i}\t{player[i]}")
print()

# add and update
print("-" * 60)
player['loc'] = 'Sabina Park'
player['runs'] = 85
player['age'] = 32
print(f"player :{player}")

# delete
print(f"player :{player}")
del player['age']
del player['runs']

print(f"player :{player}")

print(dir(player))

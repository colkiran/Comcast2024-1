
print("items".center(60, "-"))

#items = (keys + values) functions

emp = {
    'emp1': {'name': 'kennedy', 'age': 25, 'desig': 'MKT_E', 'dept': "MKT", 'gender': 'M'},
    'emp2': {'name': 'Tina', 'age': 34, 'desig': 'MGR', 'dept': "Admin", 'gender': 'F'},
    'emp3': {'name': 'Richard', 'age': 39, 'desig': 'TL', 'dept': "MKT", 'gender': 'M'}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for key, info in emp.items():
    print(key)
    print("-" * len(key))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("update".center(60, "-"))
emp1 =  {'name': 'kennedy', 'age': 25, 'desig': 'MKT_E', 'gender': 'M'}
emp2 =  {'name': 'Tina', 'age': 34,  'dept': "Admin", 'gender': 'F'}

# update emp1 with emp2 values
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

res = emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(60, "-"))
emp1 = {'name': 'kennedy', 'age': 25, 'desig': 'MKT_E', 'gender': 'M'}
print(f"emp1 :{emp1}")
emp1.clear()
print(f"emp1")

print("copy".center(60, "-"))
d1 = {'name': 'kennedy', 'age': 25, 'desig': 'MKT_E', 'gender': 'M'}
print(f"d1 before :{d1}")

# copy d1 to d2
d2 = d1                     # shallow copy
print(f"d2 before :{d2}")

d2['dept'] = "MKT"
d2['loc'] = 'Mumbai'
print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("-" * 60)
d3 = {'name': 'Tina', 'age': 34,  'dept': "Admin", 'gender': 'F'}
print(f"d3 before :{d3}")

# copy the elements of d3 to d4
d4 = d3.copy()              #deep copy
print(f"d4 before :{d4}")

d4['desig'] = "MGR"
d4['loc'] = 'BLR'
print(f"d4 after :{d4}")
print(f"d3 after :{d3}")

print("-" * 60)
d5 = {'name': 'Tina', 'age': 34, 'dept': 'Admin', 'gender': 'F', 'desig': {'hp': 'exe', 'wipro': 'sr. exe', 'cisco': 'MGR'}, 'loc': 'BLR'}
print(f"d5 before :{d5}")

# copy from d5 to d6
d6 = d5.copy()
print(f"d6 before :{d6}")

d6['desig']['ibm'] = 'asst MGR'
d6['desig']['CGI'] = 'AGM'

print(f"d6 after :{d6}")
print(f"d5 after :{d5}")

from copy import deepcopy
d7 = {'name': 'Tina', 'age': 34, 'dept': 'Admin', 'gender': 'F', 'desig': {'hp': 'exe', 'wipro': 'sr. exe', 'cisco': 'MGR'}, 'loc': 'BLR'}
print(f"d7 before:{d7}")

# copy data from d7 to d8
d8 = deepcopy(d7)
print(f"d8 before :{d8}")

d8['desig']['ibm'] = 'asst MGR'
d8['desig']['CGI'] = 'AGM'

print(f"d7 after:{d7}")
print(f"d8 after:{d8}")

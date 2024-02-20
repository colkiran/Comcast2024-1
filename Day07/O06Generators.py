
v1 = [x ** 2 for x in range(1, 11)]         # list comprehension
print(f"v1 :{v1}")
print(type(v1))

print("-" * 60)
v2 = (x ** 2 for x in range(1, 6))
print(f"v2 :{v2}")
print(type(v2))
print(next(v2))
print(next(v2))
print(next(v2))
print(next(v2))
print(next(v2))
# print(next(v2))             # stopiteration

print("-" * 60)
res = sum([x ** 2 for x in range(1, 11)])
print(f"res :{res}")

print("-" * 60)
res = sum((x ** 2 for x in range(1, 11)))
print(f"res :{res}")

print("-" * 60)
from sys import getsizeof

res1 = [x ** 2 for x in range(1, 5000)]
res2 = (x ** 2 for x in range(1, 5000))

print(f"res1 :{getsizeof(res1)}")
print(f"res2 :{getsizeof(res2)}")

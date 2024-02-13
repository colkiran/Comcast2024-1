"""
sort - sort the original list
sorted - sort a list and returns a copy of it
"""
import re

l1 = [8, 10, 2, 3, 5, 1, 9, 7, 4, 6]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending  :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 60)
l1 = [8, 'zebra', 10, 'apple', 2, 'yellow', 3, 'blue', 5, 'white', 1, 'cream', 9, 'violet', 7, 'green', 4, 'pink', 6, 'orange', 'dog', 'xray', 184, 1029, 29, 276, 2431]

print(f"l1 :{l1}")
print("-" * 60)
res = sorted(l1, key =ascii)
print(f"res :{res}")

print(res[0:res.index('zebra') + 1])
print(res[0:res.index('zebra') + 1] + sorted(res[res.index('zebra')+1:]))

print("-" * 60)
cities = ['chennai', 'mumbai', 'thiruvananthapuram', 'vishakapatnam', 'ooty', 'bangalore', 'hyderabad', 'delhi']
print(f"cities :{cities}")

print("-" * 60)
res_asc = sorted(cities, key=len)
print(f"Ascending :{res_asc}")
res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending :{res_desc}")

print("reverse".center(60, "-"))
l1 = [8, 10, 2, 3, 5, 1, 9, 7, 4, 6]
print(f"l1 :{l1}")
res = list(reversed(l1))
print(res)

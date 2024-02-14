
def add(i, j):
    return i + j

a = add
print(a(20, 30))

print("-" * 60)

b = lambda x, y: x + y
print(b(100, 200))

print("-" * 60)
# lambda are best used with - map, filter, reduce(functools)

# Map - it will have an expression (conversions - rs - dollars, kgs - pounds)
# map will implement the expression on all elements of the list
l = list(range(1, 11))
print(f"l :{l}")

# print the square of all these numbers
squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

print("-" * 60)
wgt = [10, 25, 18.5, 2, 3.7, 120, 45, 30]  # convert this into pounds
Lbs = list(map(lambda x : x * 2.205,wgt))
print(f"Pounds: {Lbs}")

print("-" * 60)
from calendar import month_abbr

months = ['aug', 'oct', 'dec', 'feb', 'sep', 'jan', 'apr', 'nov', 'mar', 'jun', 'may', 'jul']

print(f"Unsorted Months :{months}")
print(f"month_abbr :{list(month_abbr)}")

res = sorted(months, key=list(map(lambda mnt: mnt.lower(), list(month_abbr))).index)

print(f"sorted months :{res}")



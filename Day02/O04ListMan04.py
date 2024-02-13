
print("index".center(60, "-"))
lst1 = [1, 2, 3, 1, 2, 2, 2, 3, 2, 2, 1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1]
print(f"lst1 :{lst1}")

print("3 :", lst1.index(3))
print("3 :", lst1.index(3, lst1.index(3) + 1))
print("3 :", lst1.index(3, lst1.index(3, lst1.index(3) + 1) + 1))

print("clear".center(60, "-"))
lst = [1, 2, 3, 4, 5]
print(f"lst :{lst}")

lst.clear()
print(f"lst :{lst}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the elements of l1 to l2
l2 = l1             # shallow copy - copies the address along with the data
print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
# copy function
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy from l3 to l4
l4 = l3.copy()              # deep copy - only the data gets copied
print(f"l4 before :{l4}")

l4.extend([11, 12, 13])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

# there is a flaw in the copy function
print("=" * 60)
l5 = [10, 20, 30, 40, [2, 4, 6, 8, 10], 50]
print(f"l5 before :{l5}")

# copy from l5 to l6
l6 =l5.copy()           # deep copy
print(f"l6 before :{l6}")

l6[4].append(12)
l6[4].append(14)
l6[4].append(16)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
from copy import deepcopy
l7 = [1, 2, 3, [10, 20, 30], 4, 5]
print(f"l7 before :{l7}")

# copy from l7 to l8
l8 = deepcopy(l7)           # deep copy
print(f"l8 before:{l8}")

l8[3].extend([40, 50, 60])
print(f"l8 after:{l8}")
print(f"l7 after:{l7}")

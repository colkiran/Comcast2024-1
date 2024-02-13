
print("append".center(60, "-"))
lst1 = list(range(1, 6))
print(f"lst1 :{lst1}")

lst1.append(6)
lst1.append(7)
lst1.append(8)
print(f"lst1 :{lst1}")

lst1.append([9, 10, 11])
print(f"lst1 :{lst1}")

print("extend".center(60, "-"))
lst2 = [6, 7, 8, 9, 10]
print(f"lst2 :{lst2}")
lst2.extend([11, 12, 13])
print(f"lst2 :{lst2}")

print("insert".center(60, "-"))
lst3 = [10, 20, 30, 40, 50]
print(f"lst3 :{lst3}")

lst3.insert(1, 15)
lst3.insert(3, 25)
lst3.insert(5, 35)
lst3.insert(7, 45)
print(f"lst3 :{lst3}")

# delete
print("pop".center(60, "-"))
lst1 = list(range(1, 11))
print(f"lst1 :{lst1}")

res = lst1.pop(7)
print(f"res: {res}")
res = lst1.pop(3)
print(f"res: {res}")
# pop without index - will remove the last element from the list
res = lst1.pop()
print(f"res: {res}")

print(f"lst1 :{lst1}")

print("remove".center(60, "-"))
lst = [1, 2, 3, 1, 2, 2, 2, 3, 2, 2, 1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1]

print(f"lst :{lst}")
# lst.remove(3)
# lst.remove(3)
# lst.remove(3)

lst.pop(lst.index(3, lst1.index(3) + 1))

print(f"lst :{lst}")

for i in range(lst.count(1)):
        lst.remove(1)
print(f"lst: {lst}")

print("count".center(60, "-"))
lst = [1, 2, 3, 1, 2, 2, 2, 3, 2, 2, 1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1]

print("1 :", lst.count(1))
print("2 :", lst.count(2))
print("3 :", lst.count(3))
print("5 :", lst.count(5))

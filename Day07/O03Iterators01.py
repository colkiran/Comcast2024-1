
l = ['a', 'b', 'c']
print(f"l :{l}")
print(type(l))

# print(dir(l))
iterObj = l.__iter__()

print("-" * 60)
item1 = iterObj.__next__()
print(f"item1 :{item1}")

print("-" * 60)
item2 = iterObj.__next__()
print(f"item2 :{item2}")

print("-" * 60)
item3 = iterObj.__next__()
print(f"item3 :{item3}")

# print("-" * 60)
# item4 = iterObj.__next__()
# print(f"item4 :{item4}")

print("-" * 60)
for i in l:
    print(i, end=" ")
print()
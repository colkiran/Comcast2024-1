
s1 = set()          # empty set
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 5.3, 6.1, 7.0, 8.4, 'nine', 'ten', 'eleven', 'twelve', 13+2j, 14-3j, True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("add".center(60, "-"))
s1 = {1, 2, 3}
print(f"s1 :{s1}")
print("-" * 60)

s1.add(2)
s1.add(4)
s1.add(1)
s1.add(3)
s1.add(5)
s1.add(6)

print(f"s1 :{s1}")
print("update".center(60, "-"))
s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([4, 5, 6])
s1.update([6, 7, 8])
s1.update([8, 9, 10])

print(f"s1 :{s1}")

# delete
print("pop".center(60,"-"))
print(f"s1 :{s1}")

ret = s1.pop()
print(f"return :{ret}")
print(f"s1 :{s1}")

ret = s1.pop()
print(f"return :{ret}")
print(f"s1 :{s1}")

print("remove".center(60, "-"))
s1.remove(8)        # does not return anything
s1.remove(4)
# s1.remove(1)
print(f"s1 :{s1}")

print("discard".center(60, "-"))
s1.discard(10)
s1.discard(5)
s1.discard(1)       # will not throw any error
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 60)
print("A intersection B :", A & B)
print("A intersection B :", A.intersection(B))

print("-" * 60)
print("A difference B :", A - B)
print("B difference A :", B - A)

print("-" * 60)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

print("-" * 60)
a = frozenset({1, 2, 3, 4})     # immutable
print(f"a :{a}")
print(type(a))


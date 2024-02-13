
letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

#iterate through the list
for letter in letters:
    print(letter, end=" ")
print()
print("-" * 60)

for letter in enumerate(letters):
    print(letter[0], letter[1])
print("-" * 60)

for index, letter in enumerate(letters):
    print(index, letter)
print("-" * 60)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mylist)
print("-" * 60)

for ind, lst in enumerate(mylist):
    print(f"{ind}\t{lst}")
print("-" * 60)

for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"{idx}\t{num}")

print("-" * 60)

lst1 = list(range(1, 6))
print(f"lst1 :{lst1}")

# CRUD
# read
print(f"lst1[0]  :{lst1[0]}")
print(f"lst1[-1] :{lst1[-1]}")
# iterate
for x in lst1:
    print(x, end=" ")
print()
for x in range(0, len(lst1)):
    print(lst1[x], end=" ")
print("-" * 60)

# add new elements
print(f"lst1 :{lst1}")
lst1[2] = 101               # it is replacing the existing value
print(f"lst1 :{lst1}")
# deleting
del lst1[3]
print(f"lst1 :{lst1}")
print(len(lst1))

print("-" * 60)
print(dir(lst1))
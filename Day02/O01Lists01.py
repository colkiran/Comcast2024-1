
l1 = list()     # creates an empty  list
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.1, 6.3, 7.9, 8.4, 'nine', 'ten', 'eleven', 'twelve', 13+0j, 14-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1,11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
#unpack a list
values = list([10, 20, 30])
print(f"values :{values}")

a, b, c = values
print(a, b, c, sep=", ")
print("-" * 60)

values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values           # *c can accept more than
print(a, b, c, sep=',')

print("-" * 60)
a, *b, c = values
print(a, b, c, sep=',')
print("-" * 60)

*a, b, c = values
print(a, b, c, sep=',')
print(f"*a, b, c :{a, b, c}")
print("-" * 60)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]
lst3 = [lst1, lst2]
print(lst3)
print(len(lst3))
print("-" * 60)

lst4 = [*lst1, *lst2]
print(f"lst4 :{lst4}")
print(len(lst4))

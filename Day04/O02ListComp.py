
l = list(range(1, 11))
squares = [num ** 2 for num in l]       # list comprehension
print(f"squares :{squares}")

squares = [num ** 2 for num in range(1, 11)]       # list comprehension
print(f"squares :{squares}")

print("-" * 60)
fruits = [
    ('apple', 285),
    ('orange', 65),
    ('pineapple', 120),
    ('grapes', 150),
    ('watermelon', 75),
    ('gauva', 110),
    ('strawberry', 350),
    ('banana', 80)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[0] for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit[1] for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")

print("-" * 60)
price = [(fruit[0] , fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
         for fruit in fruits]
print(price)

print("-" * 60)

price = [(fruit[0] , fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
         for fruit in fruits if fruit[1] > 100]
print(price)

print("-" * 60)

fruits = [
    ('apple', 285),
    ('orange', 65),
    ('pineapple', 120),
    ('grapes', 150),
    ('watermelon', 75),
    ('gauva', 110),
    ('strawberry', 350),
    ('banana', 80)
]
y = [x for x in fruits]
print(y)

y = [x[1] for x in fruits]
print(y)

y = [x[0] for x in fruits]
print(y)

price = [(x, y, y * 0.9, y * 0.75) for x, y in fruits if y > 50]

print(price)
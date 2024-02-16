
class Player:
    def __init__(self, name, age):               # constructor
        print(f"Ctor called.......")
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is :{self.name}\nAge is {self.age}"

ply1 = Player("Rahul", 32)
# ply1.get_details()
print("-" * 60)

print(str(ply1))
print("-" * 60)
print(ply1)

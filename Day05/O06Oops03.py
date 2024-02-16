

class Player:

    # double underscore init = dunder_init
    def __init__(self, name, age):               # constructor
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")


ply1 = Player("Sourav", 35)
ply1.get_details()
print("-" * 60)

ply2 = Player("Sehwag", 28)
ply2.get_details()
print("-" * 60)
print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)

print("-" * 60)
ply2.runs = 150
print(ply2.runs)
print("ply2 :", ply2.__dict__)
print("ply1 :", ply1.__dict__)

# self - will have the name of the object that made a call to the method
# ply1.get_details()   - self will have ply1 stored in it


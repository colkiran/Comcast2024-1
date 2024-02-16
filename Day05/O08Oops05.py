
class Player:
    def __init__(self, name, age):               # constructor
        print(f"Ctor called.......")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("Factory.....")
        # cls = Player
        return cls(f"{fname} {lname}", age)            # calls the __init__ method
              #Player(f"{fname} {lname}", age)

ply1 = Player("Virat", 34)

ply1.get_details()
print("-" * 60)

# name = fname + lname
ply2 = Player.CreatePlayer("Rohit", "Sharma", 35)
ply2.get_details()

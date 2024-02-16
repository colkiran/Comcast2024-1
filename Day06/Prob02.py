import datetime
class Player:
    def __init__(self, name, age):  # constructor
        print(f"Ctor called.......")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is {self.age}")

    @classmethod
    def from_dob(cls, name, dob):
        (dy, mn, yr) = dob.split("/")
        dob = datetime.datetime(int(yr), int(mn), int(dy))
        today = datetime.date.today()
        age = today.year - dob.year
        return cls(name, age)


ply1 = Player.from_dob("Virat", "24/06/1992")
ply1.get_details()
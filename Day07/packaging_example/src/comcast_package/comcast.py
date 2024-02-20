
gname = "Sunil Gavaskar"

sports = ['cricket', 'football', 'hockey', 'tennis', 'swimming']

runs = {'odi': 14500, 'tests': 12000, 't20': 3500}

def greet(guest):
    print(f"Greetings Mr.{guest}, Welcome to the event.....")

# ------------------------------------------------------

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


print(__name__)

if __name__ == '__main__':
    greet("Kapil Dev")

    ply1 = Player("Srikanth", 65)
    ply1.get_details()

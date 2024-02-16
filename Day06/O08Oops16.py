
class Animal:

    def __init__(self):
        print("Animal Ctor.......")
        self.a = 10

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def __init__(self):                 #overriding the parent class constructor
        super().__init__()              # calls the parent class constructor
        print("Bird Ctor......")
        self.b = 20

    def fly(self):
        print("Birds fly......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print(cuckoo.__dict__)
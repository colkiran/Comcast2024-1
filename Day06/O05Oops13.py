
class Animal:
    def __init__(self):
        print("Animal Ctor")
        self.a = 10

    def eat(self):
        print("Animals eat......")

class Bird(Animal):
    def fly(self):
        print("Birds fly......")


class Fish(Animal):
    def swim(self):
        print("Fishes swim.......")

#------------------------------
cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print(cuckoo.__dict__)

print("-" * 60)
dolphin  = Fish()
dolphin.eat()
dolphin.swim()
print(dolphin.__dict__)

print("-" * 60)
print("cuckooo & Bird   :", isinstance(cuckoo, Bird))
print("cuckooo & Animal :", isinstance(cuckoo, Animal))
print("cuckooo & object :", isinstance(cuckoo, object))
print("-" * 60)
print("dolphin & Fish   :", isinstance(dolphin, Fish))
print("dolphin & Animal :", isinstance(dolphin, Animal))
print("dolphin & object :", isinstance(dolphin, object))

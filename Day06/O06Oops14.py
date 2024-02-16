
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.a = 10

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("birds fly......")

class Chicken(Bird):

    def Msg(self):
        print("Chickens are breeded for consumption.......")

    def fly(self):
        print("Chickens seldom fly.........")



chic = Chicken()
chic.eat()
chic.fly()
chic.Msg()

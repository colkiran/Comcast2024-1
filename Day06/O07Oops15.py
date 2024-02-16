
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.a = 10

    def eat(self):
        print("Animals eat.......")

    def fun(self):
        print("fun method of animal class.......")

class Person:

    def __init__(self):
        print("Person Ctor......")
        self.p = 20

    def talk(self):
        print("person talks.........")

    def fun(self):
        print("fun method of person class......")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # calls the parent class
        Person.__init__(self)
        print("Girl Ctor......")
        self.g = 30

    def walk(self):
        print("Girls walk......")

tina = Girl()
tina.eat()
tina.talk()
tina.walk()
tina.fun()      # which fun method should it call and why?
print(tina.__dict__)
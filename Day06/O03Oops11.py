

class Product:
    def __init__(self, price):
        self.setprice(price)

    def getprice(self):
        print("getter called......")
        return self.__price             # private variable

    def setprice(self, prc):
        print("setter called......")
        self.__price = prc

    def delprice(self):
        print("deleter called.....")
        self.__price = 0

    price = property(getprice, setprice, delprice)

coke = Product(60)
print(coke.price)
coke.price = 125
print(coke.price)
del coke.price
print(coke.price)

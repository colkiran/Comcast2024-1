
class Product:
    def __init__(self, price):
        self.setprice(price)

    def getprice(self):
        return self.__price             # private variable

    def setprice(self, prc):
        if prc < 0:
            raise ValueError("Price cannot be less than zero....")
        else:
            self.__price = prc

    def delprice(self):
        self.__price = 0


import sys
try:
    pepsi = Product(50)
    print(pepsi.getprice())
    pepsi.setprice(80)
    print(pepsi.getprice())
    pepsi.delprice()
    print(pepsi.getprice())

except:
    print("Exception raised.....")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

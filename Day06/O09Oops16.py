
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def checkBalance(self):
        pass

    def deposit(self, amt):
        print("Amount credited....")


class Savings(Account):

    def checkBalance(self):
        print("The balance in the account is  ######")
    def withDraw(self):
        print("Amount ##### debited from the account......")

sav = Savings()
sav.checkBalance()
sav.deposit(45000)
sav.withDraw()
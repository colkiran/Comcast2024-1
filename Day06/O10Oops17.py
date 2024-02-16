
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Managers")


class Developer(Employee):

    def doJob(self):
        print("Developers Job........")


def BankJob(obj):
    print("Bank job started........")
    obj.doJob()
    print("Bank job ended.........")
    print("-" * 60)


Mike  = Manager()
David = Developer()

BankJob(Mike)
BankJob(David)
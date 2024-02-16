
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # works fot not equal to also (!=)
    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than also (<)
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Kevin", 45000)
print(emp1)
print("-" * 60)

emp2 = Employee("Richard", 40000)
print(emp2)
print("-" * 60)

# print(emp1 == emp2)     # comparing the addresses
if (emp1 != emp2):
    print("{}'s salary {} is NOT equal to  {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary {} is equal to  {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

print(emp1 > emp2)

if (emp1 < emp2):
    print("{}'s salary {} is less than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary {} is NOT less than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

print(emp1 >= emp2)

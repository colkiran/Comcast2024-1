
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C', 'C++', 'JAVA', 'Spring', 'Hibernare', 'AngularJS']

    def __str__(self):
        return f"Name is {self.name}"

    def append(self, val):
        self.tech.append(val)

    def __iter__(self):
        return iter(self.tech)   # self.tech.__iter__()

    def __len__(self):
        return len(self.tech)


emp1 = Employee("Peter")
print(emp1)
print("-" * 60)

emp1.append("Python")
print([i for i in emp1])        # list comprehension

print("-" * 60)
print(len(emp1))

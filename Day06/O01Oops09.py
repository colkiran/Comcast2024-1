
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'JAVA', 'Spring', 'Hibernate', 'Angular', 'React JS']
    def __str__(self):
        return f"Name is :{self.name}\nSalary is {self.salary}"
    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self,idx, val):
        self.tech[idx] = val

emp1 = Employee('Daniel', 75000)
print(emp1)

print("-" * 60)
print([i for i in emp1])

print("-" * 60)
print(len(emp1))

print("-" * 60)
emp1.append("Python")
print([i for i in emp1])

print("-" * 60)
x = emp1[2]
print(x)
print([i for i in emp1])

print("-" * 60)
emp1[3] = "SOA"
print([i for i in emp1])

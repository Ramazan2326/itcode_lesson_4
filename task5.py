class Employee:

    def __init__(self, name, age, salary=30000):
        self.name = name
        self.age = age
        self.salary = salary

    def get_paid(self):
        return self.salary


class Manager(Employee):

    def __init__(self, name, age):
        super().__init__(name, age, salary=150000)

    def get_paid(self):
        return self.salary


class Worker(Employee):

    def __init__(self, name, age):
        super().__init__(name, age, salary=50000)

    def get_paid(self):
        return self.salary


print(Employee('Bob', 25).get_paid())
print(Manager('Sam', 35).get_paid())
print(Worker('Peter', 30).get_paid())
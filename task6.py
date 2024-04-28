class MixinEmploee:
    def __init__(self, name, hours_of_work, salary_per_hour):
        self.name = name
        self.hours = hours_of_work
        self.salary = salary_per_hour

    def get_month_salary(self):
        return f"моя зарплата в месяц: {self.hours * self.salary}"


class Driver:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Меня зовут {self.name}, я работаю водителем"


class Person(MixinEmploee, Driver):
    def __init__(self, name, hours, salary):
        self.name = name
        self.hours = hours
        self.salary = salary
        super().__init__(self.name, self.hours, self.salary)


peter, peters_work = Person('Peter', 160, 500).get_month_salary(), Person('Peter', 160, 500).__str__()
bob, bobs_work = Person('Bob', 120, 700).get_month_salary(), Person('Bob', 120, 700).__str__()
print(f"{peters_work}, {peter}")
print(f"{bobs_work}, {bob}")

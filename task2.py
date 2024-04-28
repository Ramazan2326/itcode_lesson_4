class Person:

    CURRENT_YEAR = 2024

    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def get_person_age(self):
        return Person.CURRENT_YEAR - self.birth_year


tom = Person('Tom', 'Dublin', 2003)
print(tom.get_person_age())

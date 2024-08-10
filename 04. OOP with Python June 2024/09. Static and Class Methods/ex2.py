class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate_age(cls, value):
        if value < cls.min_age or value > cls.max_age:
            raise ValueError

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value


class Employee(Person):
    min_age = 16
    max_age = 150

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary



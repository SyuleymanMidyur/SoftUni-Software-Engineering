from abc import ABC, abstractmethod  # cant make objects


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError('Name must be at least 2 characters')
        self.__name = value

    @abstractmethod
    def go_to_work(self):
        pass


class Teacher(Person):
    def go_to_work(self):
        return "going to school"


class Student(Person):
    def go_to_work(self):
        return "going to libary"


class Actor(Person):
    def go_to_work(self):
        return "going to theater"
# must implement all abc methods

# # # # Encapsluation
# # #
# # # class BankAccount:
# # #     def __init__(self, account_number, balance):
# # #         self._account_number = account_number # private atributes / ne mogat da bydat dostypeni izvyn klasa no moje da sa vyv clasa chrez metodi i kotroliran nachin
# # #         self._balance = balance
# # #
# # #     def balance(self):
# # #         return self._balance
# # #
# # #     def deposit(self, amount):
# # #         self._balance += amount
# # #
# # #     def withdraw(self, amount):
# # #         if self._balance >= amount:
# # #             self._balance -= amount
# # #         else:
# # #             print('Insufficient funds')
# # #
# # #
# # # account = BankAccount('00', 100)
# # # print(account.balance())
# # # account.deposit(100)
# # # print(account.balance())
# # # account.withdraw(100)
# # # print(account.balance())
# #
# # # Abstraction - ne moje da bude instanciran directno, can have lot of abstract methods
# #
# # from abc import ABC, abstractmethod
# #
# #
# # class Animal(ABC):
# #     @abstractmethod
# #     def make_sound(self):
# #         pass
# #
# #
# # class Dog(Animal):
# #     def make_sound(self):
# #         print('My dog sound')
# #
# #
# # class Cat(Animal):
# #     def make_sound(self):
# #         print('My cat sound')
# #
# #
# # class Bird(Animal):
# #     def make_sound(self):
# #         print('My bird sound')
# #
# #
# # cat = Cat()
# # dog = Dog()
# # bird = Bird()
# #
# # cat.make_sound()
# # dog.make_sound()
# # cat.make_sound()
# #
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.hobbies = []
#
#     def add_hobby(self, hobby):
#         self.hobbies.append(hobby)
#
#     def __str__(self):
#         return f'{self.name} has {self.hobbies} hobbies'
#
#
# class FootballPlayer(Person):
#     def __init__(self, name):
#         super().__init__(name)
#         self.add_hobby('Football')
#         self.add_hobby('Power Lifting')
#
#
# mike = FootballPlayer('Mike')
# print(mike)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_details(self):
#         return f'Name: {self.name}, Age: {self.age}'
#
#
# class Student(Person):
#     def __init__(self, name, age, rollnum):
#         super().__init__(name, age)  # preizpolzvame metoda init na bazoviq class
#         # obj = super()
#         # obj.__init__(self, name) # referenciq kym roditelskiq class
#         self.rollnum = rollnum
#
#     def get_details(self):
#         return f'Name: {self.name}, Age: {self.age}, Roll: {self.rollnum}'
#
#
# person = Person('John', 25)
# student = Student('Mike', 25, 19)
# print(person.get_details())
# print(student.get_details())

#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f'{self.name} make a sound')
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#     def speak(self):
#         super().speak()
#         print(f'{self.name} barks')
#
#
# dog = Dog('Bob', 'Labrador')
# dog.speak()


# class Vehicle:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#
# class Car(Vehicle):
#     def __init__(self, name, color, model):
#         super().__init__(name, color)
#         self.model = model
#
#
# class ElectricCar(Car, Vehicle):
#     def __init__(self, name, color, model, battery_capacity):
#         super().__init__(name, color, model)
#         self.battery_capacity = battery_capacity
#
#     def display_info(self):
#         print(f"{self.name} {self.model} in {self.color} color with battery capacity {self.battery_capacity}")
#
#
# my_car = ElectricCar('BMW', 'black', "M3", 100)
# my_car.display_info()

# class Person:
#     pass
#
#
# class SoftwareDeveloper(Person):
#     pass
#
#
# class TechnicalLead(SoftwareDeveloper):
#     pass
#
#
# class CTO(TechnicalLead):
#     pass
#
#
# print(CTO.mro)


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name} eats')
#
#
# class Mammal(Animal):
#     def walk(self):
#         print(f'{self.name} walks')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print(f'{self.name} barks')
#
#
# class Labrador(Dog):
#     def petch(self):
#         print(f'{self.name} petchs')
#
#
# dog = Labrador('Buddy') # class Labrador nasledqva vs ostanali classes
# dog.bark()
# dog.petch()
# dog.bark()
# dog.eat()
# dog.walk()


# MRO

# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B, C):
#     pass
#
#
# print(D.__mro__) # showing the way of inheritance

# MIXIN

class PrintableMixin:
    def print_info(self):
        print(f'Object of class {type(self).__name__}')
        for attr, value in self.__dict__.items():
            print(f'{attr}: {value}')


class Person(PrintableMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is  {self.name} and I am {self.age} years old.')


p = Person('John', 23)
p.say_hello()
p.print_info()

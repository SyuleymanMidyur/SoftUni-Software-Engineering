# class Car:
#     def __init__(self, make, model, year): # init avtomatichno se izvikva i gi inicializira /
#         # inicializira nachalnite atributi na nqkyv obekt
#         self.make = make
#         self.model = model  # <=== Atributi
#         self.year = year
#
#     def start_engine(self):  # <=== Metodi
#         return f"The {self.make} {self.model}'s engine starting"
#
#     def drive(self, distance):
#         return f"The {self.make} {self.model} is driving {distance} kilometers"
#
#     def stop_engine(self):
#         return f" The {self.make} {self.model}'s engine is stopping"
#
#
# car1 = Car('Mercedes', 'ML350', '2006') # <=== make, model, year stoinosti na atributite
# car2 = Car('BMW', '320d', '2001')  <== instanciq sys sobstveno povedenie
#
# garage = [car1, car2]
# for car in garage:
#     print(car.start_engine())
#     print(car.drive(100))
#     print(car.stop_engine())
# print(car1.make)
# print(car1.model)
# print(car1.year)


# class Person:
#     def __init__(self, name, last_name, age=0): # age ne e zadyljitelen i ima stoinost 0
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
#     def introduce(self):
#         return f"My name is {self.name} {self.last_name} and I am {self.age} years old"
#
#
# person1 = Person('Syuleyman', 'Midyur')
# print(person1.introduce())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         return f"Hello, {self.name}"
#
#
# person1 = Person('Syuleyman', 29)
# person2 = Person('Nabi', 25)
# person3 = Person('Amaya', 1)
#
# print(person1.say_hello())


# class Person:
#     species = 'Human'  # calss atribut koito ostava za vsichki obekti ednakyv
#
#     def __init__(self, name):
#         self.name = name
#
#
# Person.species = 'Homo sapiens' # <== aktualizirame
# person1 = Person('Ketio')
# person2 = Person('John')


# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def calculate_area(self):
#         return self.width * self.length
#                                          # INSTANCE FUNKCII
#     def resize(self, new_width, new_length):
#         self.width = new_width
#         self.length = new_length
#
#
# rect = Rectangle(6, 7) # <=== instancirane
# rect.resize(8, 9)
#
# print(rect.length)
# print(rect.width)



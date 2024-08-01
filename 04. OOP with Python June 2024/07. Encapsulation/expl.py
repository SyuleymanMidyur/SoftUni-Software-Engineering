# class Person:
#     def __init__(self, name, age):
#         if not name:
#             raise ValueError('Name is required')
#         self.__name = name  # private atribute / vidim samo v classa with one under score we can use in inheritance
#         self._age = age
#
#     def get_info(self):
#         return f'Hello, my name is {self.__name}'
#
#
# p = Person('John')
#
#
# class Student(Person):
#     def __init__(self, number):
#         self.number = number
#         super().__init__("Test", 20)
#

# class Person:
#     def __init__(self, name, identification_number):
#         self.name = name
#         self.__identification_number = identification_number
#
#     def get_identification_number(self):
#         return self.__identification_number
#         # return ''.join(self.__identification_number[:2]) + "****"
#
#     def set_identification_number(self, new_identification_number):
#         if len(new_identification_number) == 10 and new_identification_number.startswith('94'):
#             self.__identification_number = new_identification_number
#         else:
#             raise ValueError('Number must be 10 digits and starts with 94')
#
#
# p1 = Person('John', '9404040006')
# print(p1.get_identification_number())
# p1.set_identification_number('9404050006')
# print(p1.get_identification_number())

# class Person:
#     def __init__(self, age=0):
#         self.age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age < 18:
#             self.__age = 18
#         else:
#             self.__age = age


# class Car:
#     def __init__(self, max_speed: int):
#         self.max_speed = max_speed
#
#     def drive(self):
#         print('driving max speed ' + str(self.max_speed))
#
#     @property
#     def max_speed(self):
#         return self.__max_speed
#
#     @max_speed.setter
#     def max_speed(self, value):
#         if value > 447:
#             value = 447
#         self.__max_speed = value
#
#
# red_car = Car(200)
# red_car.drive()
# red_car.max_speed = 500
# red_car.drive()


# Name Mangling Method

# class Person:
#     def __init__(self):
#         self.first_name = 'John'
#         self.last_name = 'Wick'
#
#     def __full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def info(self):
#         return self.__full_name()
#
#
# p = Person()
# print(p.info())
# print(p.__full_name()) # attribute error
# print(p.Person__full_name())


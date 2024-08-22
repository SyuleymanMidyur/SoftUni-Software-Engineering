# class Shape:
#     def get_area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height / 2
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def get_area(self):
#         return self.side * self.side
#
#
# # same method different implements
#
# shapes = [Rectangle(5, 5), Square(3), Square(4)]
#
# for shape in shapes:
#     print(shape.get_area())
#
# # Same interface for different underlying forms


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.name + other.name

    def __lt__(self, other):
        return self.age < other.age


p = Person('John', 25)
person2 = Person('Cinio', 35)
print(p + person2)  # print(p.__add__(p2))
print(p > person2)
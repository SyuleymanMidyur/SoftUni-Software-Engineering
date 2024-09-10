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

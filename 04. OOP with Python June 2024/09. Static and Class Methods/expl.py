# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
#
# p1 = Person('Test')
# print(p1.name)
# p1.change_name('new test')
# print(p1.name)
# print(p1.is_adult(16))

# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def peperoni(cls, additional_ingredients=[]):
#         all_ingredients = ["tomato sauce", "permagiano", "peperoni"] + additional_ingredients
#         return cls(all_ingredients)
#
#     @classmethod
#     def quatro_formagggi(cls):
#         return cls(["mozzarella", "permagiano", "fontina", "gorogonzola"])
#
#
# second_pizza = Pizza.quatro_formagggi()
# personal_pizza = Pizza(["cheese", "tomato", "salami"])
# peperoni1 = Pizza.peperoni()
# print(peperoni1.ingredients)
# peperoni2 = Pizza.peperoni(["cheese", "mozzarella", "salami"])
# print(peperoni2.ingredients)

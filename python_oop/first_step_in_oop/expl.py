class Building():
    def __init__(self, floors_count, color, material): # <-- method
        self.floors_count = floors_count
        self.color = color
        self.material = material


    def obtain_license(self):
        print('Obtaining license')

sofia_building = Building(5, 'silver', 'xg') # instance - instancirame obekt
print(sofia_building.floors_count)
print(sofia_building.color)
print(sofia_building.material)
plovdiv_building = Building(12, 'white', 'xz')

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person1 = Person('John', 25)
# person2 = Person('Jack', 30)
# person3 = Person('Person', 23)
#
# print(id(person1))
# print(id(person2))

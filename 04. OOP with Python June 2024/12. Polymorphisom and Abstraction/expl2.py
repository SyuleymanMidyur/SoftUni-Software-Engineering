class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "bark"


class Cat(Animal):
    def make_sound(self):
        return "myau"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())
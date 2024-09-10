from typing import Type

from animals.animal import Mammal
from food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    @property
    def food_that_eat(self) -> list[Type[Fruit] | Type[Vegetable]]:
        return [Fruit, Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    @property
    def food_that_eat(self) -> list[Type[Meat]]:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    @property
    def food_that_eat(self) -> list[Type[Meat] | Type[Vegetable]]:
        return [Meat, Vegetable]

    @property
    def gained_weight(self) -> float:
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    @property
    def food_that_eat(self) -> list[Type[Meat]]:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

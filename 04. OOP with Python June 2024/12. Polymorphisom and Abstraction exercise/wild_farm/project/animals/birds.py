from typing import List, Type

from animals.animal import Bird
from food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def food_that_eat(self) -> list[Type[Meat]]:
        return [Meat]

    @property
    def gained_weight(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def food_that_eat(self) -> list[[Type[Meat] | Type[Vegetable] | Type[Fruit] | Type[Seed]]]:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self) -> float:
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

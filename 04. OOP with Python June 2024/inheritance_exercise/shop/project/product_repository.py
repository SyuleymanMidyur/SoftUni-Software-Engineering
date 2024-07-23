from typing import List

from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Food, Drink] = []

    def add(self, product: Food or Drink) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Food or Drink:
        # try:
        #     found_product = next(filter(lambda p: p.name == product_name, self.products), None)
        #     return found_product
        # except StopIteration:
        #     return None
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = list(items)

    def get_items_count(self):
        return len(self.items)


shop = Shop("fruitsShop", ["apple", "banana"])
print(shop.get_items_count())
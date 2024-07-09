class Glass:
    capacity = 250

    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml: float) -> str:
        if (self.content + ml) >= ml:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Glass cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        space_left = self.capacity - self.content
        return f"{space_left} ml left"


glass = Glass()

print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

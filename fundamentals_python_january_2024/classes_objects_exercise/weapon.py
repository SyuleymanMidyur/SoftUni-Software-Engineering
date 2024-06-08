class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shooting(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets left: {self.bullets}"


weapon = Weapon(5)
print(weapon.shooting)
print(weapon.shooting)
print(weapon)
print(weapon.shooting)
print(weapon.shooting)
print(weapon.shooting)
print(weapon.shooting)
print(weapon)

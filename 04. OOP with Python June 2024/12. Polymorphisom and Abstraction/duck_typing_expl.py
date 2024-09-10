# if it looks like a duke and quacks like a duck, it's a duck :)
# we don't care about the objects' types, but whether they have methods we need
class Cat:

    def sound(self):
        print("Cat sound")


class Train:
    def sound(self):
        print("Train sound")


for any_type in Cat(), Train():
    any_type.sound()

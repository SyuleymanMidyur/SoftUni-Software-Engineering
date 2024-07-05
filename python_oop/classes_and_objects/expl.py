class MyClass(object):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, I'm {self.name}"

    # def __str__(self):
    #     return f"Hello, I'm {self.name}"

    def __repr__(self):  # debuging and prints
        return f"Hello, I'm {self.name}"


x = MyClass("John")
print(x.__dict__) # converting in dict

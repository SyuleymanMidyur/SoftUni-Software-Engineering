from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    def divide(*args):
        return reduce(lambda x, y: x / y, args)


print(Calculator.add(10, 20, 30))
print(Calculator.subtract(10, 20, 30))
print(Calculator.multiply(10, 20, 30))
print(Calculator.divide(10, 20, 30))

# def repeat_word(n, word): # <-- paramnetyr
#     for _ in range(n):
#         print(word)
#
#
# repeat_word(5, "hello") #< - argument

# def repeat_word(n=5, word="test"): # default / ako ne se podade stoinost pri izvikvane
#     for _ in range(n):
#         print(word)
#
#
# repeat_word(5, "hello")


# def sum_nums(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# result = sum_nums(3, 4, 5)
# print(result)


# def sum_nums(*args):  # * opakova vs elementi, dava gi kato tuple
#     total = 0
#     for num in args:
#         total += num
#     return total
#
#
# result = sum_nums(5, 4, 2) # <-- moje da podavame kolkoto iskame argumenti
# print(result)

# def sum_nums(num1, num2, *args): # nums sa zaduljitelni 2 argumenta, no moje da ima i poveche
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(sum_nums(1,2,3,4))

# def kwargs_example(**kwargs): # dvete * paketirat v dict / moje da se polzvat na edno mqsto s *args
#     print(kwargs)
#
#
# kwargs_example(name="Amaya", age=1, town="Debren")


# def kwargs_example(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
#
# kwargs_example(name="Amaya", age=1, town="Debren")

# def sum_nums(num1, num2, *args, **kwargs):
#     total = num1 + num2
#     for num in args:
#         total += num
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#     return total
#
#
# sum_nums(4, 5, 6, 7, 8, name="Amaya", age=1, town="Debren")


# def sum_nums(a, b):
#     return a + b
#
#
# nums = [1, 2, ]
# print(sum(*nums))  # We can use * to unpack the list so that all elements of it can be passed as
# different parameters


# def print_info(name, age):
#     print(name, age)
#
#
# info = {"name": "John", "age": 18}
#
# print(info["name"], info["age"])
# print(print_info(**info)) # unpacking dictionaries
#
# my_dict = {'Peter': 21, 'Test': 18, 'George': 18, 'John': 45}
#
# print(sorted(my_dict.items(), key=lambda kvp: (kvp[1], kvp[0])))
# sorted first by then by

# NESTED FUNCTIONS

# def factorial(number):
#     if not isinstance(number, int) or number < 0:
#         return f"Sorry, 'number' is incorrect."
#
#     def inner_factorial(n):
#         fact = 1
#         for i in range(1, n+1):
#             fact *= i
#         return fact
#     return inner_factorial(number)

# def calculator(operator):
#     def addition(a, b):
#         a = 5
#         b = 6
#         return a + b
#
#     def subtraction(a, b):
#         return a - b
#
#     def multiplication(a, b):
#         return a * b
#
#     def division(a, b):
#         return a / b
#
#     if operator == '+':
#         return addition
#     elif operator == '-':
#         return subtraction
#     elif operator == '*':
#         return multiplication
#     elif operator == '/':
#         return division
#
#
# operation = calculator('+')
# result = operation(5, 4)
# print(result)

# def greet(name):
#     hello = 'Hello, '
#
#     def say_hi():
#         return hello + name
#
#     return say_hi
#
#
# print(greet('John')())

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# factorial(5)
# result = 5
# for i in range(2, 6):
#     result = result * i
# print(result)


# def multiply_numbers(a, b):
#     return a * b
# for _ in range(2):
#     a = int(input("Enter a value for A:"))
#     b = int(input("Enter a value for B:"))
#     res = multiply_numbers(a, b)
#     print(res)

# def calculate_square(number):
#     """
#     This function calculate the square of a given number  <=== dock string
#     """
#     return number ** 2
# # help(calculate_square)
# print(calculate_square.__doc__) #<=== printira dock stringa

# numbers = [3, 2, 4, 1, 5]
# smallest_number = min(numbers) #the same with max()
# print(smallest_number)

# numbers = [3, 2, 4, 1, 5]
# sum_num = sum(numbers)
# print(sum_num)

# def is_even(n):
#     return n % 2 == 0
#
#
# # numbers = [3, 2, 4, 1, 5]
# # even_nums = list(filter(is_even, numbers))
# # print(even_nums)
#
# def square(x):
#     return x ** 2
#
#
# numbers = [3, 2, 4, 1, 5]
# square_nums = list(map(square, numbers))
# print(square_nums)


# def greet_by_name(name):
#     print(f'Hello, {name}!')
#
#
# while True:
#     username = input('Username:')
#     if username == "Exit":
#         break
#     greet_by_name(username)


# def calculate_rectangle_area(length, width):
#     area = length * width
#     return area
#
#
# result = calculate_rectangle_area(length=4, width=5)
# print(result)


# CALCULATOR - GOOD EXPL
# def add(num1, num2):
#     return num1 + num2
#
#
# def subtract(num1, num2):
#     return num1 - num2
#
#
# def multiply(num1, num2):
#     return num1 * num2
#
#
# def divide(num1, num2):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         print('Error: Division by Zero!')
#
#
# def calculator():
#     operation = input('Enter the operator (+, -, *, /)')
#     num1 = float(input('Enter the first number:'))
#     num2 = float(input('Enter the second number:'))
#
#     if operation == '+':
#         result = add(num1, num2)
#     if operation == '-':
#         result = subtract(num1, num2)
#     if operation == '*':
#         result = multiply(num1, num2)
#     if operation == '/':
#         result = divide(num1, num2)
#     else:
#         print('Error: Invalid operation!')
#     return
#
#     print('Result:', result)
#
#
# calculator()


# RECURSION

# def count_numbers(num):
#     if num <= 10:
#         print(num)
#         count_numbers(num + 1)
#
#
# count_numbers(1)

# def sum_numbers():
#     a = int(input())
#     b = int(input())
#
#     return a + b
#
#
# print(sum_numbers())


# def calculate_rectangle_properties(length, width):
#     area = length * width
#     diagonals = (length ** 2 + width ** 2) ** 0.25
#     perimeter = 2 * (length + width)
#
#     return area, diagonals, perimeter
#
#
# area, diagonals, perimeter = calculate_rectangle_properties(length=10, width=3)
# print('Area', area)
# print('Diagonals', diagonals)
# print('Perimeter', perimeter)
# result = calculate_rectangle_properties(length=10, width=3)
# print(result)


# def great_by_name(name, greeting='Hello'):
#     print(greeting, name, '!')
#
#
# great_by_name('Alice', 'Hi')

# LAMbDA

# square = lambda x: x ** 2
# add = lambda a, b: a + b
# print(add(2, 3))
#
# multiply = lambda a, b, c: a * b * c
# print(multiply(200, 23, 23))

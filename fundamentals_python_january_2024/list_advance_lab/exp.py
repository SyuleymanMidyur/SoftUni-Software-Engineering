# numbers = [1, 2, 3, 4, 5, 6]
# squares = [num ** 2 for num in numbers]
# print(squares)

# numbers = [1, 2, 3, 4, 5, 6]
# even_nums = [num for num in numbers if num % 2 == 0]
# print(even_nums)
#        ^
#        |
# alternative

# numbers = [1, 2, 3, 4, 5, 6]
# even_nums = []
#
# for num in numbers:
#     if num % 2 == 0:
#         even_nums.append(num)
# print(even_nums)


# words = ['hello', 'world', 'python', 'programing']
# filter_words = [word.upper() for word in words if 'o' in word]
#
# print(filter_words)

# numbers = [1, 2, 3, 4, 5, 6]
# squared_dict = {num: num ** 2 for num in numbers}
# print(squared_dict)

# keys = ['name', 'age', 'city']
# values = ['ketio', 33, 'Sofia']
# info_dict = {k: v for k, v in zip(keys, values)}
# print(info_dict)

# string_list = ['1', '2', '3', '4']
# number_list = list(map(int, string_list))

# number_list = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda num: num % 2 == 0, number_list))

# names = ['Amaya', 'Nabi', 'Syuleyman']
# filtered_names = filter(lambda name: name.startswith('A'), names)
# print(list(filtered_names))

# numbers = [1, 2, 3, 4, 5]
# index1 = 0
# index2 = 2
# index3 = 4
#
# numbers[index1], numbers[index2], numbers[index3] = numbers[index3], numbers[index1], numbers[index2]
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# aditional_nums = [9, 8]
# total = numbers + aditional_nums konokatenirane na listove
# print(total)

# numbers = [1, 2, 3, 4, 5, 2, 3, 5]
# unique_nums = set(numbers)  printira samo unikalnite chisla bez da promenq poziciite
# print(unique_nums)

# exmp = 'hello'
# unique = set(exmp) prehamva povtarqshtite se no ne zapazva poziciite, printira vseki pyt razlichno
# print(unique)

# from functools import reduce
#
# list = [1, 3, 5, 6, 2]
#
# sum_maxnumber = reduce(lambda a, b: a + b, list)
# maxnumber = reduce(lambda a, b: a if a > b else b, list)
#
# print(maxnumber)

# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# result = reduce(lambda x, y: x * y, squared)
# print(result)

# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, nums)
# print(result)

# data = [1, 2, 3, 4, 5]
# result = [x**2 if x % 2 == 0 else x**3 for x in data if x > 2]
# print(result)

# from functools import reduce
#
#
# def custom_func(x):
#     return x if x % 2 == 0 else x**2
#
# data = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, map(custom_func, filter(lambda x: x < 5, data)))
# print(result)

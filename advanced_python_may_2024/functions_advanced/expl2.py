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

def sum_nums(num1, num2, *args, **kwargs):
    total = num1 + num2
    for num in args:
        total += num
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    return total


sum_nums(4, 5, 6, 7, 8, name="Amaya", age=1, town="Debren")

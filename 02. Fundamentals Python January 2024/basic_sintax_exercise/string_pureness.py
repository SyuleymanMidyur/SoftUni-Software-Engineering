number_of_strings = int(input())

for _ in range(number_of_strings):
    current_string = input()
    for index, string in enumerate(current_string):
        print(f'{index} has {current_string}')

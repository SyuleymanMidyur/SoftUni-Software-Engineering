first_string, second_string = input().split()
total_sum = 0

if len(first_string) > len(second_string):
    # here we have multiplication
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
        # here we are adding the rest of the 1st string
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    # here we have multiplication
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
        # here we are adding the rest of the 1st string
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
else:  # len(first_string) == len(second_string)
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)

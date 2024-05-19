CONSTANT_NUMBER = int(input())
total_sum = 0

while True:
    current_number = int(input())
    total_sum += current_number

    if total_sum >= CONSTANT_NUMBER:
        print(total_sum)
        break

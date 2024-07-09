start_interval = int(input())
final_interval = int(input())
magic_number = int(input())

counter_combination = 0
condition = False
text_info = ''
for num1 in range(start_interval, final_interval + 1):
    for num2 in range(start_interval, final_interval + 1):
        counter_combination += 1

        if num1 + num2 == magic_number:
            condition = True
            text_info = f'Combination N:{counter_combination} ({num1} + {num2} = {magic_number})'
            break

    if condition:
        break

if condition:
    print(text_info)
else:
    print(f"{counter_combination} combinations - neither equals {magic_number}")

number = int(input())

for firs_symbol in range(number):
    for second_symbol in range(number):
        for third_symbol in range(number):
            print(f"{chr(firs_symbol +97)}{chr(second_symbol +97)}{chr(third_symbol +97)}")

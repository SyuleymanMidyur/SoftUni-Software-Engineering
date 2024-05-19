from sys import maxsize

count_of_nums = int(input())
sum_nums = 0
max_num = -maxsize

for number in range(count_of_nums):
    num = int(input())
    sum_nums += num
    if num > max_num:
        max_num = num

if max_num == sum_nums - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (sum_nums - max_num))
    print('No')
    print(f'Diff = {diff}')
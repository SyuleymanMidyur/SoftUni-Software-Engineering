num = int(input())

left_sum = 0
right_sum = 0

for _ in range(2):
    first_number = int(input())
    left_sum += first_number


for _ in range(2):
    second_number = int(input())
    right_sum += second_number


if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')

else:
    difference = abs(left_sum - right_sum)
    print(f'No, diff = {difference}')
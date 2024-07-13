# money_as_string = input().split(", ")
# number_of_beggars = int(input())
# # money_as_integers = [int(money) for money in input().split(", ")]
# money_as_int = []
# for money in money_as_string:
#     money_as_int.append(int(money))
# final_sums = []
# start_index = 0
# for beggar in range(number_of_beggars):
#     current_beggar_sum = 0
#     for current_index in range(start_index, len(money_as_int), number_of_beggars):
#         current_beggar_sum += money_as_int[current_index]
#     final_sums.append(current_beggar_sum)
#     start_index += 1
# print(final_sums)
import money as money

money_as_int = [int(money) for money in input().split(", ")]
number_of_beggars = int(input())
sums = [0] * number_of_beggars

for index, current_money in enumerate(money_as_int):
    sums[index % number_of_beggars] += current_money

print(sums)


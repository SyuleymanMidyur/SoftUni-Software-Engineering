# data = input().split(", ")
# row_num, col_num = map(int, data)
#
# matrix = []
# sum_nums = 0
#
# for i in range(row_num):
#     data_row = [int(el) for el in input().split(", ")]
#     row_numbers = []
#     for index in range(len(data_row)):
#         row_numbers.append(data_row[index])
#         sum_nums += data_row[index]
#     matrix.append(row_numbers)
#
# print(sum_nums)
# print(matrix)


data = input().split(", ")
row_num, col_num = map(int, data)

matrix = []
sum_nums = 0

for i in range(row_num):
    row_data = [int(el) for el in input().split(", ")]
    sum_nums += sum(row_data)
    matrix.append(row_data)

print(sum_nums)
print(matrix)

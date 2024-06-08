nums_of_row_col = int(input())

matrix = []

for _ in range(nums_of_row_col):
    row_data = list(map(int, input().split()))
    matrix.append(row_data)

diagonal_sum = 0

# for row_index in range(nums_of_row_col):
#     for col_index in range(nums_of_row_col):
#         if row_index == col_index:
#             diagonal_sum += matrix[row_index][col_index]
for i in range(nums_of_row_col):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
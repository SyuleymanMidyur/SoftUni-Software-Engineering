num = int(input())

# matrix = []
#
# for _ in range(nums_of_row_col):
#     row_data = list(map(int, input().split(', ')))
#     matrix.append(row_data)
#
# primary_nums = []
# secondary_nums = []
# primary_diagonal_sum = 0
# secondary_diagonal_sum = 0
#
# for i in range(nums_of_row_col):
#     primary_diagonal_sum += matrix[i][i]
#     primary_nums.append(matrix[i][i])
#
# for i in range(nums_of_row_col):
#     secondary_diagonal_sum += matrix[i][nums_of_row_col - i - 1]
#     secondary_nums.append(matrix[i][nums_of_row_col - i - 1])

matrix = [[int(el) for el in input().split(", ")] for _ in range(num)]
primary = [matrix[r][r] for r in range(num)]
secondary = [matrix[r][num -r -1] for r in range(num)]

print(f'Primary diagonal: {", ".join(str(x) for x in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary)}. Sum: {sum(secondary)}')

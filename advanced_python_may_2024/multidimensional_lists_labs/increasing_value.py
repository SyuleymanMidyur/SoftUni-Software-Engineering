matrix = [
    [1, 2, 3,],
    [4, 5, 6,],
    [7, 8, 9,]
]

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        matrix[row_index][col_index] += 1
print(matrix)
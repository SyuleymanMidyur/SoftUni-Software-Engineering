rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

equal_blocks = 0

for row in range(rows -1):
    for col in range(cols -1):
        if matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col + 1]:
            equal_blocks += 1

print(equal_blocks)
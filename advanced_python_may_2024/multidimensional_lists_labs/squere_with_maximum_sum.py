row_count, col_count = map(int, input().split(', '))

matrix = []
max_sum = float('-inf')
sub_matrix = None

for _ in range(row_count):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)

for row_index in range(row_count -1):
    for col_index in range(col_count -1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        el_below = matrix[row_index + 1][col_index]
        el_diagonal = matrix[row_index + 1][col_index + 1]
        current_sum = sum((current_el, next_el, el_diagonal, el_below))

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_el, next_el], [el_below, el_diagonal]]
if sub_matrix:
    print(*sub_matrix[0])
    print(*sub_matrix[1])
print(max_sum)

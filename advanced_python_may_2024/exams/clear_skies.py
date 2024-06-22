def print_matrix(matrix):
    for row in matrix:
        print(f'{"".join(row)}')


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())

matrix = []
jet_position = None
enemy_count = 4
for row_index in range(n):
    row_data = list(input())

    if "Jet" in row_data:
        column_index = row_data.index("J")
        jet_position = (row_index, column_index)

while enemy_count:
    direction = input()
    current_row, current_col = jet_position
    row_index_movement, column_index_movement = direction_mapper[direction]
    next_row_index = current_row + row_index_movement
    next_col_index = current_col + column_index_movement

    element = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = "J"
    matrix[current_row][current_col] = "-"
    jet_position = (next_row_index, next_col_index)

    if element == "E":
        enemy_count -= 1
        if enemy_count == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            print_matrix(matrix)
            exit()
            

n = int(input())

matrix = []

for i in range(n):
    row_data = list(input())
    matrix.append(row_data)

symbol = input()
position = None

for row_index in range(n):
    # if position:
    #     break
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            position = (row_index, col_index)
            print(position)
            exit()
            # break


# if position is not None:
#     print(position)
# else:
print(f"{symbol} does not occur in the matrix")

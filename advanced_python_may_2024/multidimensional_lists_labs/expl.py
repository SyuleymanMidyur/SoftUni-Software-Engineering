# balance = [
#     [1000, 300, 200, 200, 100],  # kolonite sa indexite na elementite v lista na chiito red sme
#     [1500, 300, 250, 200, 150],
#     [900, 350, 250, 200, 80]
# ]
#
# print(balance[0][3])
# print(balance[1])
# print(balance[2])

# matrix = []
#
# for row in range(4):
#     row_data = []
#     for col in range(1, 7):
#         row_data.append(col)
#     matrix.append(row_data)
# print(matrix)

# matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range(2):
#         matrix[i].append(0)
# print(matrix)

# matrix = []
# for i in range(3):
#     matrix.append([])
#     for j in range(1, 4):
#         matrix[i].append(j)
# print(matrix)

# MD LIST COMPREHENSION

# matrix = [[0 for j in range(2)] for i in range(3)] # ot dqsno vinagi e cikyla za redovete

# matrix = [
#     [1, 2, 3,],
#     [4, 5, 6,],
# ]
#
# flattened_matrix = [num for sublist in matrix for num in sublist] # vinagi golqmiq forloop stoi od lqvo
# #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# # for row in matrix:
# #     for el in row:
# #         flattened_matrix.append(el)
# print(flattened_matrix)

# Traversing and Manipulation

# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
#
# print(matrix[-1][0])

matrix = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(matrix[0][1][1])
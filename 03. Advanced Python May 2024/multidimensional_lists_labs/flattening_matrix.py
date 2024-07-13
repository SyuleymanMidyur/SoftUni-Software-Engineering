# rows_count = int(input())
#
# matrix = []
#
# for i in range(rows_count):
#     row_data = [int(el) for el in input().split(", ")]
#     matrix.append(row_data)
#
# flattened_matrix = []
#
# for row in matrix:
#     for el in row:
#         flattened_matrix.append(el)
#
# print(flattened_matrix)

rows_count = int(input())

flattened_matrix = []

for i in range(rows_count):
    row_data = [int(el) for el in input().split(", ")]
    flattened_matrix.extend(row_data) # extend shte razarhivira i shte sloji samo elms ne kato list

print(flattened_matrix)
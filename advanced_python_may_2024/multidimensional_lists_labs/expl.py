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

# matrix = [
#     [[1, 2], [3, 4]],
#     [[5, 6], [7, 8]]
# ]
#
# print(matrix[0][1][1])

def cookbook(*args):
    from collections import defaultdict

    recipes_by_cuisine = defaultdict(list)

    for recipe_name, cuisine, ingredients in args:
        recipes_by_cuisine[cuisine].append((recipe_name, ingredients))

    sorted_cuisines = sorted(recipes_by_cuisine.items(), key=lambda item: (-len(item[1]), item[0]))

    result = []

    for cuisine, recipes in sorted_cuisines:
        result.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")

        sorted_recipes = sorted(recipes, key=lambda x: x[0])

        for recipe_name, ingredients in sorted_recipes:
            ingredients_list = ", ".join(ingredients)
            result.append(f"  * {recipe_name} -> Ingredients: {ingredients_list}")

    return "\n".join(result)


# Example usage
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

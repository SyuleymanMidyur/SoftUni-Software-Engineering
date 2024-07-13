food_and_quantities = input().split()
final_products = dict()

for index in range(0, len(food_and_quantities), 2):
    product = food_and_quantities[index]
    quantity = int(food_and_quantities[index + 1])
    final_products[product] = quantity
print(final_products)


num_of_cats = int(input())

group1 = 0
group2 = 0
group3 = 0
total_grams_food_day = 0

for _ in range(num_of_cats):
    current_food = float(input())
    if 100 <= current_food < 200:
        group1 += 1
        total_grams_food_day += current_food
    elif 200 <= current_food < 300:
        group2 += 1
        total_grams_food_day += current_food
    elif 300 <= current_food < 400:
        group3 += 1
        total_grams_food_day += current_food

total_kg_foods = total_grams_food_day / 1000
price_for_food_day = total_kg_foods * 12.45

print(f'Group 1: {group1} cats.')
print(f'Group 2: {group2} cats.')
print(f'Group 3: {group3} cats.')
print(f'Price for food per day: {price_for_food_day:.2f} lv.')


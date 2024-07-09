quantity_of_decoration = int(input())
remaining_days = int(input())

cost = 0
spirit = 0
ornament_set_price = 2
skirt_tree_price = 5
garland_tree_price = 3
lights_tree_price = 15
for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        cost += quantity_of_decoration * ornament_set_price
        spirit += 5
    if current_day % 3 == 0:
        cost += quantity_of_decoration * (skirt_tree_price + garland_tree_price)
        spirit += 3 + 10
    if current_day % 5 == 0:
        cost += quantity_of_decoration * lights_tree_price
        spirit += 17
        if current_day % 3 == 0:
            spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        cost += skirt_tree_price + garland_tree_price + lights_tree_price
if remaining_days % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")

nums_chicken = int(input())
nums_fishes = int(input())
nums_vegetarians = int(input())

price_for_chicken = nums_chicken *10.35
price_for_fishes = nums_fishes * 12.40
price_for_vegetarians = nums_vegetarians * 8.15
total_price_for_menus = price_for_vegetarians + price_for_chicken + price_for_fishes
dessert_price = total_price_for_menus * 0.20
delivery_price = 2.50
final_price = total_price_for_menus + dessert_price + delivery_price

print(final_price)
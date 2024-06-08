items_and_prices = input().split("|")
budget = float(input())
false_budget = budget
total_profit = 0
bought_items_new_price = []
for items in items_and_prices:
    type_of_item, price_of_item = items.split("->")
    price_of_item = float(price_of_item)
    valid_price = False
    if type_of_item == "Clothes":
        if price_of_item <= 50.00:
            valid_price = True
    elif type_of_item == "Shoes":
        if price_of_item <= 35.00:
            valid_price = True
    elif type_of_item == "Accessories":
        if price_of_item <= 20.50:
            valid_price = True
    if valid_price:
        if false_budget >= price_of_item:
            false_budget -= price_of_item
            total_profit += price_of_item * 0.40
            price_of_item += price_of_item * 0.40
            bought_items_new_price.append(price_of_item)
for price in bought_items_new_price:
    print(f'{price:.2f}', end=" ")
print()

print(f'Profit: {total_profit:.2f}')
if budget + total_profit >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')

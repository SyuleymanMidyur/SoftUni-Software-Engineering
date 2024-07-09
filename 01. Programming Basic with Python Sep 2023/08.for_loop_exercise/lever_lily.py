age_of_lily = int(input())
laundry_price = float(input())
price_of_1toy = int(input())

total_money = 0
total_toys = 0
current_sum = 0

for birthday in range(1, age_of_lily + 1):
    if birthday % 2 == 0:
        current_sum += 10
        total_money += current_sum - 1
    else:
        total_toys += 1

total_money += total_toys * price_of_1toy
difference = abs(total_money - laundry_price)

if total_money >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
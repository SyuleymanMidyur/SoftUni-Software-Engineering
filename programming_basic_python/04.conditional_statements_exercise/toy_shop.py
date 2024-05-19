price_for_vacation = float(input())
puzzles_nums = int(input())
talking_dolls_nums = int(input())
teddy_bears_nums = int(input())
minions_nums = int(input())
truck_toy_nums = int(input())

puzzle_price = puzzles_nums * 2.60
talking_doll_price = talking_dolls_nums * 3
teddy_bears_price = teddy_bears_nums * 4.10
minion_price = minions_nums * 8.20
truck_toy_price = truck_toy_nums * 2

total_order_toys = puzzles_nums + talking_dolls_nums + teddy_bears_nums + minions_nums + truck_toy_nums
total_amount = puzzle_price + talking_doll_price + teddy_bears_price + minion_price + truck_toy_price


if total_order_toys > 50:
    total_amount -= 0.25 * total_amount

rent = total_amount * 0.10
profit = total_amount - rent
left_money = profit - price_for_vacation
needed_sum = price_for_vacation - profit

if profit >= price_for_vacation:
    print(f"Yes! {left_money:.02f} lv left.")
else:
    print(f"Not enough money! {needed_sum:.02f} lv needed.")
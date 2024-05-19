budget_for_movie = float(input())
nums_of_statists = int(input())
price_for_clothes_1statist = float(input())

decor_for_movie = budget_for_movie * 0.10  #10% from budget
sum_for_clothes_all = price_for_clothes_1statist * nums_of_statists

if nums_of_statists > 150:
    sum_for_clothes_all -= 0.10 * sum_for_clothes_all #10% discount

price_for_movie = sum_for_clothes_all + decor_for_movie
left_sum = budget_for_movie - price_for_movie
short_sum = price_for_movie - budget_for_movie

if budget_for_movie >= price_for_movie:
    print("Action!")
    print(f"Wingard starts filming with {left_sum:.02f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {short_sum:.02f} leva more.")
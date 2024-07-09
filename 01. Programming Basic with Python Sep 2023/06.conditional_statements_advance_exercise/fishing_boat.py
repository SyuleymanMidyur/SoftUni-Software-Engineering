budget = int(input())
season = input()
nums_of_fisherman = int(input())

rent_price = 0

if season == 'Spring':
    rent_price = 3000
    if nums_of_fisherman <= 6:
        rent_price *= 0.90
    elif nums_of_fisherman == 7 or nums_of_fisherman <= 11:
        rent_price *= 0.85
    else:
        rent_price *= 0.75

elif season == 'Summer'or season == 'Autumn':
    rent_price = 4200
    if nums_of_fisherman <= 6:
        rent_price *= 0.90
    elif nums_of_fisherman == 7 or nums_of_fisherman <= 11:
        rent_price *= 0.85
    else:
        rent_price *= 0.75

elif season == 'Winter':
    rent_price = 2600
    if nums_of_fisherman <= 6:
        rent_price *= 0.90
    elif nums_of_fisherman == 7 or nums_of_fisherman <= 11:
        rent_price *= 0.85
    else:
        rent_price *= 0.75

if nums_of_fisherman % 2 == 0 and season != 'Autumn':
    rent_price *= 0.95

difference = abs(rent_price - budget)

if budget >= rent_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
type_of_flowers = input()
nums_of_flowers = int(input())
budget = int(input())
price_per_flower = 0

if type_of_flowers == 'Roses':
    price_per_flower = 5
    if nums_of_flowers > 80:
        price_per_flower *= 0.90 #10% discount

elif type_of_flowers == 'Dahlias':
    price_per_flower = 3.80
    if nums_of_flowers > 90:
        price_per_flower *= 0.85

elif type_of_flowers == 'Tulips':
    price_per_flower = 2.80
    if nums_of_flowers > 80:
        price_per_flower *= 0.85

elif type_of_flowers == 'Narcissus':
    price_per_flower = 3
    if nums_of_flowers < 120:
        price_per_flower *= 1.15

elif type_of_flowers == 'Gladiolus':
    price_per_flower = 2.50
    if nums_of_flowers < 80:
        price_per_flower *= 1.20

total_amount = price_per_flower * nums_of_flowers
difference = abs(total_amount - budget)

if budget >= total_amount:
    print(f"Hey, you have a great garden with {nums_of_flowers} {type_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
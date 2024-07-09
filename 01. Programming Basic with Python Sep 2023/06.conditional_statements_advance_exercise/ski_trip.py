days_of_stay = int(input())
type_of_room = input()
feedback = input()
price = 0

if type_of_room == 'room for one person':
    price = 18
elif type_of_room == 'apartment':
    price = 25
    if days_of_stay < 10:
        price *= 0.70
    elif 10 <= days_of_stay <= 15:
        price *= 0.65
    else:
        price *= 0.50
elif type_of_room == 'president apartment':
    price = 35
    if days_of_stay < 10:
        price *= 0.90
    elif 10 <= days_of_stay <= 15:
        price *= 0.85
    else:
        price *= 0.80

total_price = (price * days_of_stay) - price

if feedback == 'positive':
    total_price *= 1.25
elif feedback == 'negative':
    total_price *= 0.90

print(f'{total_price:.2f}')
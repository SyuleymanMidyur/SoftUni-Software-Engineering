budget = float(input())
season = input()

destination = ''
type_of_vaccination = ''
vaccination_price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vaccination_price = budget * 0.30
        type_of_vaccination = 'Camp'
    elif season == 'winter':
        vaccination_price = budget * 0.70
        type_of_vaccination = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vaccination_price = budget * 0.40
        type_of_vaccination = 'Camp'
    elif season == 'winter':
        vaccination_price = budget * 0.80
        type_of_vaccination = 'Hotel'
else:
    vaccination_price = budget * 0.90
    type_of_vaccination = 'Hotel'
    destination = 'Europe'

print(f'Somewhere in {destination}')
print(f'{type_of_vaccination} - {vaccination_price:.2f}')
if month == 'march' or month == 'april' or month == 'may':
    if time_of_day == 'day':
        price_per_hour = 10.50
    elif time_of_day == 'night':
        price_per_hour = 8.40
        if num_of_group >= 4:
            price_per_hour *= 0.90
    elif spent_hours >= 5:
        price_per_hour += 0.50
elif month == 'june' or month == 'july' or month == 'august':
    if time_of_day == 'day':
        price_per_hour = 12.60
    elif time_of_day == 'night':
        price_per_hour = 10.20
        if num_of_group >= 4:
            price_per_hour *= 0.90
    elif spent_hours >= 5:
        price_per_hour += 0.50


if month == 'march' or month == 'april' or month == 'may':
    if time_of_day == 'day':
        price_per_hour = 10.50
    elif time_of_day == 'night':
        price_per_hour = 8.40

elif month == 'june' or month == 'july' or month == 'august':
    if time_of_day == 'day':
        price_per_hour = 12.60
    elif time_of_day == 'night':
        price_per_hour = 10.20


if num_of_group >= 4:
    price_per_hour *= 0.90
    if spent_hours >= 5:
        price_per_hour *= 0.50

type_of_fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
error_date = False

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday' or day_of_week == 'Friday':
    if type_of_fruit == 'banana':
        price = 2.50 * quantity
    elif type_of_fruit == 'apple':
        price = 1.20 * quantity
    elif type_of_fruit == 'orange':
        price = 0.85 * quantity
    elif type_of_fruit == 'grapefruit':
        price = 1.45 * quantity
    elif type_of_fruit == 'kiwi':
        price = 2.70 * quantity
    elif type_of_fruit == 'pineapple':
        price = 5.50 * quantity
    elif type_of_fruit == 'grapes':
        price = 3.85 * quantity
    else:
        error_date = True


elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if type_of_fruit == 'banana':
        price = 2.70 * quantity
    elif type_of_fruit == 'apple':
        price = 1.25 * quantity
    elif type_of_fruit == 'orange':
        price = 0.90 * quantity
    elif type_of_fruit == 'grapefruit':
        price = 1.60 * quantity
    elif type_of_fruit == 'kiwi':
        price = 3.00 * quantity
    elif type_of_fruit == 'pineapple':
        price = 5.60 * quantity
    elif type_of_fruit == 'grapes':
        price = 4.20 * quantity
    else:
        error_date = True
else:
    error_date = True

if not error_date:
    print(f'{price:.2f}')
else:
    print('error')

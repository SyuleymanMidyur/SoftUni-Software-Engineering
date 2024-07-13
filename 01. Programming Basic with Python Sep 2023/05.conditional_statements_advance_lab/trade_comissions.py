city = input()
sale_volume = float(input())
comissions = 0
error_date = False

if city == 'Sofia':
    if 0 < sale_volume <= 500:
        comissions = sale_volume * 0.05
    elif 500 < sale_volume <= 1000:
        comissions = sale_volume * 0.07
    elif 1000 < sale_volume <= 10000:
        comissions = sale_volume * 0.08
    elif sale_volume > 10000:
        comissions = sale_volume * 0.12
    else:
         error_date = True

elif city == 'Varna':
    if 0 < sale_volume <= 500:
        comissions = sale_volume * 0.045
    elif 500 < sale_volume <= 1000:
        comissions = sale_volume * 0.075
    elif 1000 < sale_volume <= 10000:
        comissions = sale_volume * 0.10
    elif sale_volume > 10000:
        comissions = sale_volume * 0.13
    else:
        error_date = True

elif city == 'Plovdiv':
    if 0 < sale_volume <= 500:
        comissions = sale_volume * 0.055
    elif 500 < sale_volume <= 1000:
        comissions = sale_volume * 0.08
    elif 1000 < sale_volume <= 10000:
        comissions = sale_volume * 0.12
    elif sale_volume > 10000:
        comissions = sale_volume * 0.145
    else:
        error_date = True
else:
    error_date = True


if not error_date:
    print((f'{comissions:.2f}'))
else:
    print('error')
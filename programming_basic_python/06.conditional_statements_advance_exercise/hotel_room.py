mount = input()
nights = int(input())

studio = 0
apartment = 0

if mount == 'May' or mount == 'October':
    studio = 50
    apartment = 65
    if nights > 7 and nights <= 14:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.70
        apartment *= 0.90
elif mount == 'June' or mount == 'September':
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio *= 0.80
        apartment *= 0.90
elif mount == 'July' or mount == 'August':
    studio = 76
    apartment = 77
    if nights > 14:
        apartment *= 0.90

total_price_for_studio = nights * studio
total_price_for_apartment = nights * apartment

print(f"Apartment: {total_price_for_apartment:.2f} lv.")
print(f"Studio: {total_price_for_studio:.2f} lv.")
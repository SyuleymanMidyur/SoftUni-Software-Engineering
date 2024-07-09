# family = 50
# heavy_duty = 80
# sport = 100

cars = input().split('>>')
final_taxes = 0
for vehicle in cars:
    car_type, years, kilometers = vehicle.split()
    years = int(years)
    kilometers = int(kilometers)
    if car_type != 'family' and car_type != 'heavyDuty' and car_type != 'sports':
        print("Invalid car type.")
        continue
    elif car_type == 'family':
        taxes = 50 - (years * 5)
        additional_taxes = kilometers // 3000
        total_taxes = taxes + additional_taxes * 12

    elif car_type == 'heavyDuty':
        taxes = 80 - (years * 8)
        additional_taxes = kilometers // 9000
        total_taxes = taxes + additional_taxes * 14
    elif car_type == 'sports':
        taxes = 100 - (years * 9)
        additional_taxes = kilometers // 2000
        total_taxes = taxes + additional_taxes * 18
    final_taxes += total_taxes
    print(f"A {car_type} car will pay {total_taxes:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {final_taxes:.2f} euros in taxes.")

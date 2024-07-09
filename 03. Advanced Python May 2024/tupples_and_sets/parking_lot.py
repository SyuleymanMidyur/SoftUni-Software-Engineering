num_of_cars = int(input())

parking = set()

for _ in range(num_of_cars):
    direction, car_platte = input().split(', ')
    if direction == "IN":
        parking.add(car_platte)
    elif direction == "OUT":
        if car_platte in parking:
            parking.remove(car_platte)
if parking:
    print(*parking, sep="\n")
else:
    print('Parking Lot is Empty')

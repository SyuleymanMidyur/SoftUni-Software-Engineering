from collections import deque

packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])

total_weight = 0

while packages and couriers:
    if packages[-1] == couriers[0]:
        total_weight += packages.pop()
        couriers.popleft()

    elif packages[-1] < couriers[0]:
        total_weight += packages[-1]
        remaining_capacity = couriers[0] - packages.pop() * 2
        if couriers[-2] > 0:
            couriers[-2] += remaining_capacity
        else:
            couriers[-2].popleft()
    else:
        total_weight += couriers[0]
        packages[-1] -= couriers[0]
        couriers.popleft()

print(f"Total weight: {total_weight} kg")

if not couriers and not packages:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
else:
    print(f"Couriers are still on duty: {', '.join(*couriers)} but there are no more packages to deliver.")
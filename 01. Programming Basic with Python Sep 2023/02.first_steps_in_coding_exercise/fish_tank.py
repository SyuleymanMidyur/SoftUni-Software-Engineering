long_of_tank = int(input())
wide_of_tank = int(input())
high_of_tank = int(input())
occupied_space = float(input())

volume_of_the_tank = long_of_tank * wide_of_tank * high_of_tank
volume_in_liters = volume_of_the_tank / 1000
needed_liters = volume_in_liters - (volume_in_liters * occupied_space / 100)

print(needed_liters)

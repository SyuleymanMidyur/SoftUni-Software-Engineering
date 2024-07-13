number_of_lines = int(input())
capacity = 255

for line in range(number_of_lines):
    current_liters = int(input())
    if capacity - current_liters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= current_liters
print(255 - capacity)

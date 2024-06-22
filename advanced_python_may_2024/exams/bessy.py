def move_bee(row, col, direction, n):
    if direction == "up":
        row = (row - 1 + n) % n
    elif direction == "down":
        row = (row + 1) % n
    elif direction == "left":
        col = (col - 1 + n) % n
    elif direction == "right":
        col = (col + 1) % n
    return row, col


def find_bee(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] == 'B':
                return i, j
    return -1, -1


def print_field(field):
    for row in field:
        print(''.join(row))


# Read input
n = int(input())
field = [list(input()) for _ in range(n)]

bee_row, bee_col = find_bee(field)
energy = 15
nectar = 0
energy_restored = False

while True:
    command = input()

    # Move the bee
    field[bee_row][bee_col] = '-'
    bee_row, bee_col = move_bee(bee_row, bee_col, command, n)

    energy -= 1

    # Check if the bee is on a flower
    if field[bee_row][bee_col].isdigit():
        nectar += int(field[bee_row][bee_col])
        field[bee_row][bee_col] = '-'

    # Check if the bee reached the hive
    if field[bee_row][bee_col] == 'H':
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        field[bee_row][bee_col] = 'B'
        break

    # Check if the bee ran out of energy
    if energy == 0:
        if nectar >= 30 and not energy_restored:
            energy = nectar - 30
            nectar = 30
            energy_restored = True
            if energy == 0:
                print("This is the end! Beesy ran out of energy.")
                field[bee_row][bee_col] = 'B'
                break
        else:
            print("This is the end! Beesy ran out of energy.")
            field[bee_row][bee_col] = 'B'
            break

    field[bee_row][bee_col] = 'B'

print_field(field)

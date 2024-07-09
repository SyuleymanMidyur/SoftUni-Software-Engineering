cells = input().split("#")
total_water = int(input())

total_seized_fire = 0
total_effort = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
for cell in cells:
    level_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False
    if level_of_fire == "High":
        if cell_value in high:
            cell_is_valid = True
    elif level_of_fire == "Medium":
        if cell_value in medium:
            cell_is_valid = True
    elif level_of_fire == "Low":
        if cell_value in low:
            cell_is_valid = True
    if cell_is_valid: #cell is valid = True
        if total_water >= cell_value:
            total_water -= cell_value
            fire_out_cells.append(cell_value)
            total_effort += cell_value * 0.25
            total_seized_fire += cell_value

print('Cells:')
for fire_cell in fire_out_cells:
    print(f' - {fire_cell}')
print(f"Effort: {total_effort:.2f}")
print(f'Total Fire: {total_seized_fire}')

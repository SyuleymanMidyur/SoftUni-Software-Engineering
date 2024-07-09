numbers_of_electrons = int(input())
shells = []

for shell in range(1, numbers_of_electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if numbers_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        numbers_of_electrons -= max_electrons_in_current_shell
        if numbers_of_electrons == 0:
            break
    else:
        shells.append(numbers_of_electrons)
        break

print(shells)

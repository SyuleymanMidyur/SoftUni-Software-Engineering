num_of_groups = int(input())

musala = 0
monblan = 0
kilimandzharo = 0
k2 = 0
everest = 0

for _ in range(num_of_groups):
    persons_in_group = int(input())
    if persons_in_group <= 5:
        musala += persons_in_group
    elif 5 < persons_in_group <= 12:
        monblan += persons_in_group
    elif 12 < persons_in_group <= 25:
        kilimandzharo += persons_in_group
    elif 25 < persons_in_group <= 40:
        k2 += persons_in_group
    else:
        everest += persons_in_group

total_people = musala + monblan + kilimandzharo + k2 + everest
musala_percent = musala / total_people * 100
monblan_percent = monblan / total_people * 100
kilimandzharo_percent = kilimandzharo / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimandzharo_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')

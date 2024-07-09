needed_experience = float(input())
count_of_battles = int(input())
total_experience = 0
battle_counter = 0
player_successfully_collect_exp = False

for battle in range(1, count_of_battles + 1):
    current_experience = float(input())
    if battle % 3 == 0:
        total_experience += current_experience * 0.15

    if battle % 5 == 0:
        total_experience -= current_experience * 0.10

    if battle % 15 == 0:
        total_experience += current_experience * 0.05

    battle_counter += 1
    total_experience += current_experience

    if total_experience >= needed_experience:
        player_successfully_collect_exp = True
        break


more_needed_exp = needed_experience - total_experience
if player_successfully_collect_exp:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {more_needed_exp:.2f} more needed.")

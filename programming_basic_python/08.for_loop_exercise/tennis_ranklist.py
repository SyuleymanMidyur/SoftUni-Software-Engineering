import math
from math import floor
nums_of_tournament = int(input())
start_points = int(input())
current_points = 0
win_tournaments = 0
for _ in range(nums_of_tournament):
    tournament = input()
    if tournament == 'W':
        current_points += 2000
        win_tournaments += 1
    elif tournament == 'F':
        current_points += 1200
    elif tournament == 'SF':
        current_points += 720

final_points = current_points + start_points
average_points = current_points / nums_of_tournament
percent_win_tournaments = win_tournaments / nums_of_tournament * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f'{percent_win_tournaments:.2f}%')


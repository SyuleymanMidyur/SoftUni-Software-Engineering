from math import ceil
name_of_series = str(input())
time_of_episode = int(input())
time_for_break= int(input())

time_for_lunch = time_for_break / 8
time_for_chill = time_for_break / 4
free_time = time_for_break - time_for_chill - time_for_lunch
difference_time = abs(free_time - time_of_episode)
difference_time = ceil(difference_time)

if free_time >= time_of_episode:
    print(f"You have enough time to watch {name_of_series} and left with {difference_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {difference_time} more minutes.")
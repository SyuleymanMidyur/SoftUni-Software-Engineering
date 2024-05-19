name_of_actor = input()
points__academy = float(input())
nums_of_assessors = int(input())
current_points = 0
total_points = 0
needed_points = 1250.5
for assessors in range(nums_of_assessors):
    name_of_assessor = input()
    point_from_assessor = float(input())
    current_points += (len(name_of_assessor) * point_from_assessor / 2)
    total_points = current_points + points__academy
    if total_points >= needed_points:
        break
difference = abs(total_points - needed_points)

if total_points >= needed_points:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")
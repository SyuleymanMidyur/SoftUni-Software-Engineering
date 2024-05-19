nums_of_jury = int(input())
command = input()

final_grade = 0
nums_of_presentations = 0

while command != "Finish":
    current_present_name = command
    current_presents_grades = 0
    nums_of_presentations += 1
    for command in range(nums_of_jury):
        current_grade = float(input())
        current_presents_grades += current_grade
        current_average_grade = current_presents_grades / nums_of_jury
    print(f'{current_present_name} - {current_average_grade:.2f}.')
    final_grade += current_average_grade
    command = input()

final_average_grade = final_grade / nums_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")

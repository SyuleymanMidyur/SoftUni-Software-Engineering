maximum_bad_grades = int(input())
total_score = 0
total_problems_solved = 0
last_problem_solved = ""
bad_grades_counter = 0
to_many_bad_grades = False
current_problem = input()

while current_problem != 'Enough':
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == maximum_bad_grades:
            to_many_bad_grades = True
            break
    total_score += current_grade
    total_problems_solved += 1
    last_problem_solved = current_problem
    current_problem = input()

average_score = total_score / total_problems_solved\

if to_many_bad_grades:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem_solved}")


n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []

    students[name].append(grade)

student_above_average = {name: sum(grade) / len(grade) for name, grade in students.items()
                         if sum(grade) / len(grade) >= 4.50}

for name, avarage_grade in student_above_average.items():
    print(f'{name} -> {avarage_grade:.2f}')

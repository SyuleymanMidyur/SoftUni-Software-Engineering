number_of_students = int(input())

students = {}

for i in range(number_of_students):
    data = tuple(input().split())
    name, grade = data[0], float(data[1])

    if name not in students:
        students[name] = []
    students[name].append(grade)

for students, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{students} -> {' '.join([f'{g:.2f}' for g in grades])} (avg: {avg:.2f})")

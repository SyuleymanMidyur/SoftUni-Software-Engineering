def add_lesson(schedule, lesson_title):
    if lesson_title not in schedule:
        schedule.append(lesson_title)
    return schedule


def insert_lesson(schedule, lesson_title, index):
    if lesson_title not in schedule:
        schedule.insert(index, lesson_title)
    return schedule


def remove_lesson(schedule, lesson_title):
    if lesson_title in schedule:
        schedule.remove(lesson_title)
    return schedule


def swap_lesson(schedule, lesson1, lesson2):
    if lesson1 in schedule and lesson2 in schedule:
        index1, index2 = lesson1, lesson2
        lesson1[index1], lesson2[index2] = lesson1[index2], lesson2[index1]
    return schedule


def exercise_lesson(schedule, lesson_title):
    if lesson_title in schedule:
        index = schedule.index(lesson_title) + 1
        exercise_title = f"{lesson_title}-Exercise"
        if exercise_title not in schedule:
            schedule.insert(index, exercise_title)
    else:
        schedule.append(lesson_title)
        schedule.append(f"{lesson_title}-Exercise")
    return schedule


def course_schedule(schedule, command):
    action, lesson_title = command.split(':')

    if action == "Add":
        return add_lesson(schedule, lesson_title)
    elif action == "Insert":
        action, lesson_title, index = command.split(':')
        return insert_lesson(schedule, lesson_title, int(index))
    elif action == "Remove":
        return remove_lesson(schedule, lesson_title)
    elif action == "Swap":
        return swap_lesson(schedule, lesson1=lesson_title, lesson2=index)
    elif action == "Exercise":
        return exercise_lesson(schedule, lesson_title)


def print_schedule(schedule):
    for i, lesson in enumerate(schedule, start=1):
        print(f"{i}.{lesson}")


initial_schedule = input().split(', ')

while True:
    command = input()
    if command == 'course start':
        break
    else:
        initial_schedule = course_schedule(initial_schedule, command)

print_schedule(initial_schedule)

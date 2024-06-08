import math

number_of_persons = int(input())
elevator_capacity = int(input())

courses = math.ceil(number_of_persons / elevator_capacity)

print(courses)

hour_for_exam = int(input())
minutes_for_exam = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

time_of_exam = hour_for_exam * 60 + minutes_for_exam
time_of_arrival = arrival_hour * 60 + arrival_minutes

if time_of_arrival > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print('On time')
elif time_of_exam - 30 > time_of_arrival:
    print('Early')

difference = abs(time_of_exam - time_of_arrival)
hour = difference // 60
minutes = difference % 60

if time_of_exam - 60 < time_of_arrival < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_of_arrival <= time_of_exam - 60:
    print(f'{hour}:{minutes:02d} hours before the start')
elif time_of_exam < time_of_arrival < time_of_exam + 60:
    print(f'{minutes:02d} minutes after the start')
elif time_of_exam + 60 <= time_of_arrival:
    print(f'{hour}:{minutes:02d} hours after the start')
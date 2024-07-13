from math import floor
from math import ceil

world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1meter = float(input())

delay = (distance_in_meters // 15) * 12.5
total_time = distance_in_meters * time_in_seconds_for_1meter + delay
missing_seconds = total_time - world_record_in_seconds

if missing_seconds == 0:
    missing_seconds = ceil(missing_seconds)

if total_time >= world_record_in_seconds:
    print(f"No, he failed! He was {missing_seconds:.02f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.02f} seconds.")
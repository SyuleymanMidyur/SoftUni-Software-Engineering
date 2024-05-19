from math import floor
num_cpus_needed = int(input())
num_employers = int(input())
work_days = int(input())

total_work_hours = num_employers * work_days * 8
made_cpus = floor(total_work_hours / 3)
difference = abs((num_cpus_needed - made_cpus) * 110.10)
if made_cpus >= num_cpus_needed:
    print(f"Profit: -> {difference:.2f} BGN")
else:
    print(f"Losses: -> {difference:.2f} BGN")

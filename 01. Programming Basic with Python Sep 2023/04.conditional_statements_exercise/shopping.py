budget = float(input())
gpus = int(input())
cpus = int(input())
rams = int(input())

all_gpu = gpus * 250
one_cpu = all_gpu * 0.35
all_cpu = cpus * one_cpu
one_ram = all_gpu * 0.10
all_ram = rams * one_ram
needed_amount = all_ram + all_cpu + all_gpu

if gpus > cpus:
    needed_amount *= 0.85 #15% discount

difference = abs(needed_amount - budget)

if budget >= needed_amount:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
import math

price_for_1gpu = int(input())
price_for_1transition = int(input())
price_1gpu_power_day = float(input())
income_1gpu_day = float(input())

total_price_gpus = price_for_1gpu * 13
total_price_transitions = price_for_1transition * 13
total_price_rig = total_price_gpus + total_price_transitions + 1000
total_income_gpu_day = income_1gpu_day - price_1gpu_power_day
total_income_all_gpus_day = 13 * total_income_gpu_day

cashback_days = total_price_rig / total_income_all_gpus_day

print(total_price_rig)
print(math.ceil(cashback_days))

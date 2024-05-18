nylon_in_m2_needed = int(input())
paint_in_liters_needed = int(input())
thinner_needed = int(input())
hours_of_work = int(input())

sum_for_nylon = (nylon_in_m2_needed + 2) * 1.50
sum_for_paint = (paint_in_liters_needed * 1.1) * 14.50
sum_for_thinner = thinner_needed * 5
sum_for_bags = 0.40
total_sum_for_tools = sum_for_nylon + sum_for_paint + sum_for_thinner + sum_for_bags
sum_for_workers_per_h = total_sum_for_tools * 0.30
final_sum = sum_for_workers_per_h * hours_of_work + total_sum_for_tools

print(final_sum)
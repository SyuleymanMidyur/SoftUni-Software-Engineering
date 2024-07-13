locations = int(input())
 
for i in range(locations):
    expected_gold_amount_per_day = float(input())
    days_for_digging = int(input())
 
    average_gold_per_day = 0
    total_gold = 0
 
    for j in range(days_for_digging):
        obtained_gold = float(input())
        total_gold += obtained_gold
 
    average_gold_per_day = total_gold / days_for_digging
 
    if average_gold_per_day >= expected_gold_amount_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(f"You need {expected_gold_amount_per_day - average_gold_per_day:.2f} gold.")

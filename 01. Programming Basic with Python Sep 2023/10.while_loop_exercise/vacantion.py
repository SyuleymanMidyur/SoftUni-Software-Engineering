needed_money_for_vacation = float(input())
available_money = float(input())
days_counter = 0
spending_counter = 0

while available_money < needed_money_for_vacation and spending_counter < 5:
    save_or_spend = input()
    money = float(input())

    if save_or_spend == 'save':
        available_money += money
        days_counter +=1
    elif save_or_spend == 'spend':
        spending_counter += 1
        days_counter += 1

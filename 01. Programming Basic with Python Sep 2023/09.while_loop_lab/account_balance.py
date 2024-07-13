account_balance = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break

    current_deposit = float(text)

    if current_deposit >= 0:
        account_balance += current_deposit
        print(f'Increase: {current_deposit:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {account_balance:.2f}')

n1 = int(input())
n2 = int(input())
operator = input()

number = ''
result = 0

if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2
    if result % 2 == 0:
        number = 'even'
    else:
        number = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {number}")

elif operator == '/':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")

elif operator == '%':
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")


number_of_kids = 0
number_of_adults = 0
money_for_toys = 0
money_for_sweaters = 0

while True:
    command = input()
    if command == "Christmas":
        break

    age = int(command)
    if age <= 16:
        number_of_kids += 1
        money_for_toys += 5
    else:
        number_of_adults += 1
        money_for_sweaters += 15

print(f'Number of adults: {number_of_adults}')
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")

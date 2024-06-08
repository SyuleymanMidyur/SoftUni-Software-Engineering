year = int(input())

while True:
    year += 1
    is_happy_year = True
    already_found_year = ""
    for digit in str(year):
        if digit in already_found_year:
            is_happy_year = False
            break
        already_found_year += digit

    if is_happy_year:
        break
print(year)


def odd_and_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for i in str(number):
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_and_even_sum(number))

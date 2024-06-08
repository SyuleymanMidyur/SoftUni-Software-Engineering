n = int(input())

positive_numbers = []
negative_numbers = []
sum_of_negatives = 0
for _ in range(n):
    current_number = int(input())

    if current_number > 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)
        sum_of_negatives += current_number
counter_positive = len(positive_numbers)
#sum_negatives = sum(negative_numbers) sumira kakvoto ima v lista
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {counter_positive}')
print(f'Sum of negatives: {sum_of_negatives}')

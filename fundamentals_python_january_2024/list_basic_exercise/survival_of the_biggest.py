# list_as_int = [int(numbers) for numbers in input().split()]
# count_of_numbers_to_remove = int(input())
# for _ in range(count_of_numbers_to_remove):
#     list_as_int.remove(min(list_as_int))
# list_as_int = str(list_as_int)
# for i in list_as_int:
#     sorted_numbers = i.split(",")

numbers = list(map(int, input().split()))
remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]

print(numbers)

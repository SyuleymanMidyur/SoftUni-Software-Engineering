length_of_first_set, length_of_second_set = input().split()

first_set = set()
second_set = set()

for _ in range(int(length_of_first_set)):
    first_set.add(input())
for _ in range(int(length_of_second_set)):
    second_set.add(input())

print(*first_set.intersection(second_set), sep='\n')

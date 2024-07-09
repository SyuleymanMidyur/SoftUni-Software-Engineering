n1 = int(input())
n2 = int(input())

my_list = list(range(1, n2 + 1))
multiples_list = []
for number in my_list:
    multiples_list.append(number * n1)
print(multiples_list)

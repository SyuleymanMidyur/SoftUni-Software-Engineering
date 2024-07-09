# my_list = [1, 2, 3, 4, 5]
# new_values = []
#
# for number in my_list:
#     new_values.append(number ** 2) #na kvadrat
# print(new_values)

# my_list = ['apple', 'banana', 'cherry', 'orange']
#print('All fruits: ', ', '.join(mylist))
# for i in range(len(my_list)):
#     print(f'Index {i} - item {my_list[i]}')

my_list = ['apple', 'banana', 'cherry', 'orange']
index = 0

while index < len(my_list):
    print(f'Index {index} - item {my_list[index]}')
    index += 1

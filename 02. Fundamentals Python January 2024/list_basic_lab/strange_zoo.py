my_list = []

for _ in range(3):
    data = input()
    my_list.append(data)
my_list[0], my_list[2] = my_list[2], my_list[0] #swap - smenqme im stoinostite

print(my_list)

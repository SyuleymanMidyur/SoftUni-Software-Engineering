# list_example = ['SoftUni', "Example", True, False, 1, 1, 2, 3.16, [], {}, dict ]
#
# set_example = {'SoftUni', "SoftUni", "SoftUni"} # premahva dublikaciite
#
# print(list_example[-1]) #always take the last element

#name = input().split(' ') #splitvame sys space / ("-") splitvame s tire

# name = list(map(int, input().split('-')))
# print(name)

# my_list = ['a', 'b', 'c']  #syedinqvane na stringove if another date type won't work
# print(''.join(my_list))

# my_list = [1, 2, 3] #append dobavq v kraq na spisuka
# for num in range(4,11):
#     my_list.append(num)
# print(my_list)

# my_list = [1, 2, 3] #chisti celiq list
# my_list.clear()

# my_list = [1, 2, 3, 2] #shte premahne pyrvoto syvpadenie koeto vidi
# my_list.remove(2)
# print(my_list)

# my_list = [1, 2, 3] #sluji da si izvurshvame nqkvi operacii no da ne promenqme struktorata na original list
# new_list = my_list.copy()
# print(new_list)

# my_list = [1, 2, 3] #obrushta spisacite moje i slice print(my_list[::-1])
# my_list.reverse()
# print(my_list)

# my_list = [1, 2, 3, 4, 5, 5, 5]
# count = my_list.count(5)   #trqbva da go prisvuime kym neshto, tyrsi syvpadeniq
# print(count)

# my_list = [1, 2, 3, 2, 4, 5, 6, 2, 5, 5, 2]
# index = my_list.index(2, 8) #tyrsi na koi index e, moje da im i start ot kyde da tyrsi value 2 / start 8
# print(index)

# my_list = [1, 2, 3, 2]
# my_list.insert(1, 8) #insertva po index index 1 insert 8
# print(my_list)

# my_list = ["Siuleiman", "Amaya", "Nabi"]
# my_list.sort()           #sortira po azbuchen red ili po cifri [1, 5, 2, 7, 3] = 1 2 3 5 7
# print(my_list) # sorted e opciq koqto prisvoqvame kym promenliva, moje da e v cikyl i shte raboti samo tam

# my_list = ['apple', 'banana', 'orange', 'cherry']
# search_element = 7
# if 'apple' in my_list:
#     print('Apple!!! ')


# my_list = ['apple', 'banana', 'orange', 6, 'cherry']
# search_element = 7
# try:
#     index = my_list.index(search_element)
#     print('Element found')
# except ValueError:
#     print('Element not found')

#extend()	Add the elements of a list (or any iterable), to the end of the current list

# numbers = [2, 4, 6, 8, 10]
# result = [i for i in numbers if all(i % j != 0 for j in range(2, i))]
# print(result)

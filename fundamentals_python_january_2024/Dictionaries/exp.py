# **********************************************************************************************************
#
# RECHNICITE SA REALIZIRANI KATO HESH TABLICI KOITO OSIGORQVAT IZKL BYRZ NACHIN NA TYRSENE
# heshirane syhranqvat i izvlichat dvoiki k, v - vremeto za izbirane na elementa ne zavisi ot goleminata na rechnika
# DINAMICHNO PREORAZMERQVANE
#
#
#
#


# my_dict = {} # empty dictionary
#
# # dictionary with string keys
# my_dict = {'fruit': 'apple', 'vegetable': 'cucumber'} # <== has key and value/ 1st element is key and 2nd value
# # kliuchovete sa unikalni, ne mogat da se povtarqt / moje da str ili int
#
# #promenqmae stoinosta
#
#
# my_dict['fruit'] = 'banana'


# dict_argumets = dict(name="George", age=22)
# print(dict_argumets)

# my_dict = {'fruit': 'apple', 'vegetable': 'cucumber'}
# print(my_dict)
# my_dict["new_key"]= my_dict["fruit"]
# print(my_dict)
# del my_dict["fruit"]
# print(my_dict)
#
#
# my_dict = {'name':'Jack', 'age':26}
# print(my_dict['name'])
# print(my_dict.get('age')) # <== safe method, vryshta None ako ne syshtestvuva koda ne gyrmi

# my_dict = {'name':'Jack', 'age':26}
# if 'name' in my_dict.keys():
#     print(my_dict['name'])


# *******************************************************************************************

# ITERIRANE PREZ KLIUCHOVE
# my_dict = {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
#
# for key in my_dict.keys():
#     print(key, end=' ')


# my_dict = {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
#
# for value in my_dict.values():
#     print(value, end=' ')


# my_dict = {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
#
# for key, value in my_dict.items():
#     print(f"Key={key}", end=" ")
#     print(f"Value={value}")

# my_dict = {1:'apple', 2:'banana'}
# #my_dict.clear() # trie celiq rechnik
# copied_dict = my_dict.copy()

# my_dict = {'fruit': 'apple', 'vegetable': 'cucumber'}
# apple = my_dict.pop("fruit")
# print(my_dict)
# print(apple)

# my_dict = {'fruit': 'apple', 'vegetable': 'cucumber'}
# print(my_dict.popitem())
# print(my_dict)


# NASTED DICTS

# students = {"name": {"age": 15, "city":"Sofia"}}
# print(students["name"]["age"])

# data = [("Syuleyman", 29), ("Amaya", 1), ("Nebi", 24)]
# dictionary = {key:value for key, value in data}
# print(dictionary)

# data1 = ["Syuleyman", "Amaya", "Nebi"]
# data2 = [29, 1, 24]
# dictionary = dict(zip(data1, data2))
# print(dictionary)


# nums = [1, 2, 3]
# cubes = {num:num ** 3 for num in nums}
# print(cubes)

# my_dict = {'fruit': 'apple', 'vegetable': 'cucumber'}
# my_dict.popitem()  # <=== avt trie posledniq
# print(my_dict)

# expl_dict = {'a': 1, 'b':2}
# value = expl_dict.setdefault('c', 0) # dobavqme gi


# expl_dict = {'a': 1, 'b':2}
#
# expl_dict.update({'c':3, 'd':4}) # dobavq, podobno na append pri list
# print(expl_dict)


# lst1 = [1, 2, 3,]
# lst2 = ['apple', 'banana', 'kiwi']
#
# zip_object = dict(zip(lst1, lst2)) #vzimame stoinosti i syzdaveme rechnik, moje i tupple
# print(zip_object)



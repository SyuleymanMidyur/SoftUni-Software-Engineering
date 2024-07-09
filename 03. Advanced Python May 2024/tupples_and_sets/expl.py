# # Tupples are immuteble READONLY
#
# b = (3, 1, 2, 3)
# print(type(b))
# print(b.index(3)) # namira pyrviq i prekliuchva tyrseneto
# print(b.count(3)) # prebroqva kolko pyti ima dadeniq element / ako go nqma dava 0
#
# a = 1, 2, 3, # avtomatichno stava tupple
# print(type(a))
#
# c = (3, ) # ako e edin element trqbva da ima zapetiq za da definira kato tupple
#
# # unpacking tupples
#
# d = (1, 2)
# e, f = d

# listovete sa referentni promenlivi expl

# a = [1, 2, 3]
# b = a
#
# b.append(100)
# print(a)

# tupples
#
# result = ("name1", "name2", "name3")
#
# result2 = result
#
# result2 = tuple() # new assingment
#
# print(result)
# print(result2)
# print(list(result))

# tupples are immuteable but the object inside are if they are referent

# result = ([1, 2], [3, 4], [5,6])
#
# result[0].append(100)
# print(result)

# a = [4, 3, 200]
# print(sorted(a, reverse=True)) # vrushta gi obratno sortirani

my_dict = {'Peter': 21, 'Georgi': 18, 'John': 44}
print(sorted(my_dict.items(), key=lambda kvp: kvp[1], reverse=True))
print(sorted(my_dict.items(), key=lambda kvp: kvp[0], reverse=True))
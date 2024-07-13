# name_list = input().split(', ')
#
# sorted_list = sorted(name_list, key=lambda x: (-len(x), x))
# print(sorted_list)

def sorted_names():
    names = input().split(', ')
    sorted_names = sorted(names, key=lambda name: (-len(name), name))

    return sorted_names


result = sorted_names()
print(result)

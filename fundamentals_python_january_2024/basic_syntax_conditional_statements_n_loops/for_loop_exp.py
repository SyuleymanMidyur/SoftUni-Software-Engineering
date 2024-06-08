# name = input()
#
# for i in range(len(name)):
#     print(f'Letter index {i} -', name[i])
#
# print()
#
# for char in name:
#     print(char, end=' ')

word = input()

for i in range(len(word) - 1, -1, -1):
    print(word[i], end=' ')
print()

for char in word[::-1]:
    print(char, end=' ')

number = int(input())

for i in range(1, number + 1):
    for up in range(0, i):
        print('*', end='')
    print()

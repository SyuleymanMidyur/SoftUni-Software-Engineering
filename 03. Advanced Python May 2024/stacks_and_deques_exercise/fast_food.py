from collections import deque

food = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

for oder in orders.copy(): # instead while loop
    if food - oder >= 0:
        orders.popleft()
        food -= oder
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders])}")
        break
else: # else na for loop
    print(f"Orders complete")



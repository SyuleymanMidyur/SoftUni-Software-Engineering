from _collections import deque

data = deque(input().split())
data.reverse()

print(' '.join(data))

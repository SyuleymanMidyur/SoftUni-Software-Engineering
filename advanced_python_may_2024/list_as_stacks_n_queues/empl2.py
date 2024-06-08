# from _collections import deque
#
# expl_q = deque()
#
# expl_q.append(1)
# expl_q.append(2)
# expl_q.append(3)
# expl_q.append(4)
#
# while expl_q:
#     print(expl_q.popleft())

from _collections import deque

expl_q = deque()
expl_stack = []

for i in range(1, 6):
    expl_q.append(i)
    expl_stack.append(i)

print('Deque')
while expl_q:
    print(expl_q.popleft())

print('Stack')
while expl_stack:
    print(expl_stack.pop())

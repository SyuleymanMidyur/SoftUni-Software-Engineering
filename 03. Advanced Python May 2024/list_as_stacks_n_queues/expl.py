# my_stack = [1, 2, 3, 4, 5]
#
# print(my_stack.pop())
# print(my_stack.pop())
# print(my_stack.pop())


# my_stack = []
#
# my_stack.append(1)
# my_stack.append(2)
# my_stack.append(3)
# my_stack.append(22)
#
# while my_stack:
#     print(my_stack.pop()) # popva poslednata stoinost ot stack

class ExampleStack:
    def __init__(self):
        self.stack = []

    def push_value(self, value):
        self.stack.append(value)

    def pop_value(self):
        return self.stack.pop()

    def last_value(self):
        return self.stack[-1]


stack = ExampleStack()
stack.push_value(1)
stack.push_value(2)
stack.push_value(3)
print(stack.last_value())

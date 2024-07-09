width_cake = int(input())
length_cake = int(input())
nums_of_pieces = width_cake * length_cake
current_pieces = input()

while current_pieces != 'Stop':
    current_pieces = input()
    nums_of_pieces -= current_pieces


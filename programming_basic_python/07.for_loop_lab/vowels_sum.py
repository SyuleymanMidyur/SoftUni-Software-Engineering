word = input()

for letter in word:
    letter_sum = int(input())
    if letter == 'a':
        letter_sum = 1
    elif letter == 'e':
        letter_sum = 2

print(letter_sum)
text = input()
numbers = ''
letters = ''
chars = ''

for char in text:
    if char.isdigit():
        numbers += char
    elif char.isalpha():
        letters += char
    else:
        chars += char

print(numbers)
print(letters)
print(chars)

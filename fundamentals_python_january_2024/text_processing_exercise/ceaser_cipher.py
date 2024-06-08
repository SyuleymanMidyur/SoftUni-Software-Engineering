text = input()
encrypted_text = ""
for charecter in text:
    encrypted_char = chr(ord(charecter) + 3)
    encrypted_text += encrypted_char
print(encrypted_text)

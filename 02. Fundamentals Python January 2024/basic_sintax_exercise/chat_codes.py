number_of_msg = int(input())

for current_message in range(number_of_msg):
    current_number = int(input())
    text = ''
    if current_number == 88:
        text = 'Hello'
    elif current_number == 86:
        text = 'How are you?'
    elif current_number < 88:
        text = 'GREAT!'
    else:
        text = 'Bye.'
    print(text)

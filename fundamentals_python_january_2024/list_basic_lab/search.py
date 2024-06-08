number = int(input())
word = str(input())

all_text = []
filtered_text = []
for _ in range(number):
    current_text = input()
    all_text.append(current_text)
    if word in current_text:
        filtered_text.append(current_text)
print(all_text)
print(filtered_text)

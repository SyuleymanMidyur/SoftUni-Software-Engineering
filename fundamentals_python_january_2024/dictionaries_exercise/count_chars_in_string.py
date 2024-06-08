# def count_letters(current_text):
#     chars_dict = {}
#
#     for word in current_text:
#         for letter in word:
#             if letter not in chars_dict:
#                 chars_dict[letter] = 1
#             else:
#                 chars_dict[letter] += 1
#
#     return chars_dict
#
#
# text = input().split()
# charachters_dictionary = count_letters(text)
#
# for k, v in charachters_dictionary.items():
#     print(f"{k} -> {v}")


from collections import Counter


def counter_letter(text):
    text = ''.join(text)
    chars_dict = Counter(text)

    return chars_dict


text = input().split()
charachters_dictionary = counter_letter(text)

for k, v in charachters_dictionary.items():
    print(f"{k} -> {v}")

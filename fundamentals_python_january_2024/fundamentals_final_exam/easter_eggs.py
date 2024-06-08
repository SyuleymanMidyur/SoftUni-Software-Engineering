# import re
#
#
# def find_eggs(text):
#     pattern = r'([@#]+)([a-z]{3,})([^a-z0-9]+)?/(\d+)/'
#     matches = re.findall(pattern, text)
#
#     for match in matches:
#         color_prefix, color, _, amount = match
#         if color_prefix[0] == color_prefix[-1] and len(color_prefix) >= 1 and len(
#                 color) >= 3 and color.islower() and amount.isdigit():
#             print(f"You found {amount} {color} eggs!")
#
#
# text = input()
#
# find_eggs(text)

import re


def find_valid_eggs(text):
    pattern = r'[@#]+([a-z]{3,})[^a-z\d]*?/(\d+)/'
    matches = re.findall(pattern, text)

    for color, amount in matches:
        print(f"You found {amount} {color} eggs!")


text = input()

find_valid_eggs(text)

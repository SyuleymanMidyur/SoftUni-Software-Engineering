# boundary machva neshto konkretno s nachalo i krai

import re


def test_regex(regex, string):
    match = re.search(regex, string)
    if match:
        print(f'Match found', match.group())
    else:
        print('No match found')


test_regex('\d+', '12345')
test_regex('\D+', 'hello1234')
test_regex('\\world\\b', 'hello world')
test_regex('\s', 'Hello world')
test_regex('\S', 'Hello world')
test_regex('\w+', 'Hello world')
test_regex('\W+', 'Hello... world')

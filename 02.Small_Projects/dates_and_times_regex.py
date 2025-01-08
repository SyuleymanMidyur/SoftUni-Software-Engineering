import re

text = """
Hi,
my name is Jane and my phone number is 555-123-4567.
My email address is jane_doe@example.com.
I live on 123 Main St. Apt. #456, and I was born on January  11th, 1990.
I have an appointment on 2023-05-15 at 2:30pm at 789 Oak Ln. #3 and backup on 2023/ 05/21.
Please give me a call or send me an email to confirm. In case the dates are unavailable, please set up a meeting sometime in June.
I would love June 19th around 14:00.
Thank you!
"""

pattern = r"""
    \b(?:                                   # Word boundary
        (?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|
        Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)
        \s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{4}  # Month Day, Year
    |
        \d{4}[-/]\d{2}[-/]\d{2}               # YYYY-MM-DD or YYYY/MM/DD
    |
        \d{1,2}[-/]\d{1,2}[-/]\d{2,4}         # MM-DD-YYYY or MM/DD/YYYY
    |
        \b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|
        Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)
        \s+\d{1,2}(?:st|nd|rd|th)?            # Month Day
    |
        \d{1,2}:\d{2}(?::\d{2})?(?:am|pm|AM|PM)?  # HH:MM(:SS)(am/pm)
    |
        \d{1,2}(?:am|pm|AM|PM)                # HHam/pm
    |
        \d{2}:\d{2}                           # 24-hour time
    )
"""

matches = re.findall(pattern, text, re.VERBOSE | re.IGNORECASE)

# Print the matches
print("Dates and times found:")
for match in matches:
    print(match.strip())

# import re
#
# text = """
# Hi,
# my name is Jane and my phone number is 555-123-4567.
# My email address is jane_doe@example.com.
# I live on 123 Main St. Apt. #456, and I was born on January  11th, 1990.
# I have an appointment on 2023-05-15 at 2:30pm at 789 Oak Ln. #3 and backup on 2023/ 05/21.
# Please give me a call or send me an email to confirm. In case the dates are unavailable, please set up a meeting sometime in June.
# I would love June 19th around 14:00.
# Thank you!
# """
#
# # Simplified pattern for dates and times
# pattern = (r'\b(?:\d{4}[-/]\d{2}[-/]\d{2}|\d{1,2}:\d{2}(?:am|pm)?|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr('
#            r'?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec('
#            r'?:ember)?)\s+\d{1,2}(?:st|nd|rd|th)?,?\s*\d{4}?)')
#
# # Find all matches in the text
# matches = re.findall(pattern, text, re.IGNORECASE)
#
# # Print the matches
# print("Dates and times found:")
# for match in matches:
#     print(match.strip())
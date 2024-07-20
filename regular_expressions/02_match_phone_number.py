import re
def find_valid_phones(text):
    pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'
    matches = re.finditer(pattern, text)
    valid_phones = ", ".join(match.group(0) for match in matches)
    print(valid_phones)
input_text = input()
find_valid_phones(input_text)
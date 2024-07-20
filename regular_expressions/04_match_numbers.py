import re
pattern = r"(^|\s)-?([0-9]+)(\.[0-9]+)?($|\s)"
text = input()
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group().strip(), end=" ")
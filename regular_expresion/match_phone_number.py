import re

number = input()
regex = '\+359-2-\d{3}-\d{4}\\b|\+359 2 \d{3} \d{4}\\b'
matches = list(re.findall(regex, number))
print(', '.join(matches))

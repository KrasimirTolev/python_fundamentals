import re

text = input()
regex = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'
matches = list(re.findall(regex, text))
print(' '.join(matches))

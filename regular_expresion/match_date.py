import re

date = input()
regex = r'\\b(\d{2})(/-.)([A-Z][a-z]{2})(-./)(\d{4})'

matches = re.finditer(date, regex)
print(matches)
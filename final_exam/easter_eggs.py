import re

text = input()
regex = r"(?P<delim>[@#]+)(?P<color>[a-z]{3,})[^a-zA-Z0-9]*?[/]+(?P<qty>[0-9]+)[/]+"

eggs = re.finditer(regex, text)

for egg in eggs:
    print(f"You found {egg.group('qty')} {egg.group('color')} eggs!")
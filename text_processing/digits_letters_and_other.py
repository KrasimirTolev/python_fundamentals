symbols = input()
letters = ''
digits = ''
other = ''

for symbol in symbols:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        other += symbol

print(digits)
print(letters)
print(other)
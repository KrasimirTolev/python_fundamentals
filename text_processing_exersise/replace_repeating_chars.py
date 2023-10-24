text = input()
repeating_char = ''
filtered_text = ''

for char in text:
    if char == repeating_char:
        pass
    else:
        filtered_text += char
    repeating_char = char

print(filtered_text)
word = input()
word = [symbol for symbol in word if symbol.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(word))


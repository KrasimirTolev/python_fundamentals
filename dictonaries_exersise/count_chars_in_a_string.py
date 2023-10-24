word = input()
symbols = {}
for i in word:
    if i != ' ':
        if i not in symbols:
            symbols[i] = 1
        else:
            symbols[i] += 1

for k, v in symbols.items():
    print(f'{k} -> {v}')
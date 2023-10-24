text = input()
emojy = []

for i in range(len(text)):
    if text[i] == ':':
        emojy.append(f':{text[i + 1]}')

for e in emojy:
    print(e)

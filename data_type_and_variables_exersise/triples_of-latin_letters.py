num = int(input())
for a in range(97, (num + 97)):
    for b in range(97, (num + 97)):
        for c in range(97, (num + 97)):
            print(f'{chr(a)}{chr(b)}{chr(c)}')
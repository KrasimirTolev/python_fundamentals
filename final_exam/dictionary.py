text = input().split(' | ')
dictionary = {}
words_test = input().split(' | ')
teacher = input()

for word in text:
    k, v = word.split(': ')
    if k not in dictionary:
        dictionary[k] = [v]
    else:
        dictionary[k].append(v)

if teacher == 'Hand Over':
    print(' '.join(dictionary))
if teacher == 'Test':
    for word in words_test:
        if word in dictionary:
            print(f'{word}:')
        for k, v in dictionary.items():
            if k == word:
                for definition in v:
                    print(f' -{definition}')


n = int(input())
dict_synonym = {}
for i in range(n):
    word = input()
    synonym = input()
    if word not in dict_synonym:
        dict_synonym[word] = [synonym]
    else:
        dict_synonym[word].append(synonym)

for k, v in dict_synonym.items():
    print(f'{k} - {", ".join(v)}')

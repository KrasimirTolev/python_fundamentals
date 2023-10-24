list_chr = input().split(', ')
dict_ascii = {}

for i in list_chr:
    dict_ascii[i] = ord(i)

print(dict_ascii)
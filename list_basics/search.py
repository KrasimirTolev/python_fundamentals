n = int(input())
keyword = input()
strings = []

for _ in range(n):
    sentence = input()
    strings.append(sentence)
print(strings)

for num_of_string in range(n - 1, - 1, - 1):
    if keyword not in strings[num_of_string]:
        strings.remove(strings[num_of_string])
print(strings)
words = input().lower().split()
filtered_words = {}
odd_words = []
for word in words:
    if word not in filtered_words:
        filtered_words[word] = 1
    else:
        filtered_words[word] += 1
for k, v in filtered_words.items():
    if v % 2 != 0:
        odd_words.append(k)

print(' '.join(odd_words))
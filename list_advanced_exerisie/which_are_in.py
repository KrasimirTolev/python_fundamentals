first_words = input().split(', ')
second_words = input().split(', ')
substrings = []
for first_word in first_words:
    for second_word in second_words:
        if first_word in second_word:
            substrings.append(first_word)
            break

print(substrings)
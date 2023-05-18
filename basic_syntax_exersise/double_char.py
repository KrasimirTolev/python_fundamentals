sentence = ''


while True:
    final_sentence = ''
    sentence = input()
    if sentence == 'End':
        break
    elif sentence == 'SoftUni':
        continue
    for i in range(len(sentence)):
        final_sentence += sentence[i] * 2
    print(final_sentence)


n = int(input())

for i in range(n):
    sentence = input()
    for i in range(len(sentence)):
        if sentence[i] == ',' or sentence[i] == '.' or sentence[i] == '_':
            print(f"{sentence} is not pure!")
            break
    else:
        print(f"{sentence} is pure.")
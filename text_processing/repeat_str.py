words = input().split()
repeat_str = ''

for word in words:
    for i in range(len(word)):
        repeat_str += word

print(repeat_str)
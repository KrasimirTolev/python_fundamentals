first, second = input().split()
sum_char = 0
if len(first) > len(second):
    for i in range(len(second)):
        sum_char += ord(first[i]) * ord(second[i])
    for i in range(len(second), len(first)):
        sum_char += ord(first[i])
elif len(second) > len(first):
    for i in range(len(first)):
        sum_char += ord(first[i]) * ord(second[i])
    for i in range(len(first), len(second)):
        sum_char += ord(second[i])
else:
    for i in range(len(first)):
        sum_char += ord(first[i]) * ord(second[i])

print(sum_char)
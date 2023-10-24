some_str = input()
final_str = ''
strength = 0

for i in range(len(some_str)):
    if strength > 0 and some_str[i] != '>':
        strength -= 1
    elif some_str[i] == '>':
        final_str += some_str[i]
        strength += int(some_str[i + 1])
    else:
        final_str += some_str[i]

print(final_str)

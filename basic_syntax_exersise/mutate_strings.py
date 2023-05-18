first_string = input()
second_string = input()
last_printed_string = first_string

for char_index in range(len(first_string)):
    left_str = second_string[:char_index + 1]
    right_str = first_string[char_index + 1:]
    new_str = left_str + right_str
    if new_str == last_printed_string:
        continue
    print(new_str)
    last_printed_string = new_str





def range_char(from_char, to_char):
    chars_list = [chr(char) for char in range(ord(from_char) + 1, ord(to_char))]
    char_string = ' '.join(chars_list)
    print(char_string)


from_char = input()
to_char = input()
range_char(from_char, to_char)

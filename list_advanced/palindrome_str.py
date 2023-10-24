def palindrome(string):
    string_list = string.split()
    palindrome_word = input()
    palindrome_word_seen = 0
    palindrome_list = [word for word in string_list if word == word[::-1]]
    for _ in palindrome_list:
        if palindrome_word == _:
            palindrome_word_seen += 1
    return palindrome_list, palindrome_word_seen


list_palindrome = list(palindrome(input()))

print(list_palindrome[0])
print(f'Found palindrome {list_palindrome[1]} times')
def long_validation(password):
    if len(password) < 6 or len(password) > 10:
        return True
    return False


def letters_digit_validation(password):
    for symbol in password:
        if ord(symbol) < 48:
            return True
        if 57 < ord(symbol) < 65:
            return True
        if 90 < ord(symbol) < 97:
            return True
        if 122 < ord(symbol):
            return True
    return False


def two_digits_validation(password):
    digits = 0
    for symbol in password:
        if 48 <= ord(symbol) <= 57:
            digits += 1
    if digits < 2:
        return True
    return False


password_input = input()
list_password = [symbol for symbol in password_input]
invalid_operation = 0
if long_validation(list_password):
    invalid_operation += 1
    print('Password must be between 6 and 10 characters')
if letters_digit_validation(list_password):
    invalid_operation += 1
    print('Password must consist only of letters and digits')
if two_digits_validation(list_password):
    invalid_operation += 1
    print('Password must have at least 2 digits')
if invalid_operation == 0:
    print('Password is valid')

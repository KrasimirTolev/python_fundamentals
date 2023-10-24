def valid_lenght(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_symbols(username):
    for symbol in username:
        if not (symbol.isalnum() or symbol == '-' or symbol == '_'):
            return False
    return True


def redundant_symbols(username):
    if ' ' in username:
        return False
    return True


def is_valid(username):
    if valid_lenght(username) and valid_symbols(username) and redundant_symbols(username):
        return True
    return False


users = input().split(', ')
valid_username = []
for username in users:
    if is_valid(username):
        valid_username.append(username)

for user in valid_username:
    print(user)

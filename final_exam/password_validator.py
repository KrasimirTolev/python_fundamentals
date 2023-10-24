import re


class Password:
    def __init__(self, password):
        self.password = password

    def make_upper(self, index):
        if index > len(self.password):
            pass
        else:
            self.password[index] = self.password[index].upper()

    def make_lower(self, index):
        if index > len(self.password):
            pass
        else:
            self.password[index] = self.password[index].lower()

    def insert(self, index, char):
        if index > len(self.password):
            pass
        else:
            self.password.insert(index, char)

    def replace(self, char, index):
        for i in range(len(self.password)):
            if char == self.password[i]:
                self.password[i] = chr(ord(char) + index)

    def validation(self):
        if len(self.password) < 8:
            return "Password must be at least 8 characters long!"
        text = ''.join(self.password)
        regex = r'\w'
        text = re.findall(regex, text)
        if len(text) != len(self.password):
            return "Password must consist only of letters, digits and _!"
        text = ''.join(self.password)
        regex = r'[A-Z]'
        text = re.findall(regex, text)
        if len(text) == 0:
            return "Password must consist at least one uppercase letter!"
        text = ''.join(self.password)
        regex = r'[a-z]'
        text = re.findall(regex, text)
        if len(text) == 0:
            return "Password must consist at least one lowercase letter!"
        text = ''.join(self.password)
        regex = r'[0-9]'
        text = re.findall(regex, text)
        if len(text) == 0:
            return "Password must consist at least one digit!"


password1 = input()
list_password = []
for i in password1:
    list_password.append(i)
password1 = Password(list_password)

while True:
    command = input().split()
    if command[0] == 'Complete':
        break
    elif command[0] == 'Validation':
        if password1.validation() is None:
            pass
        else:
            print(password1.validation())
    elif command[0] == 'Insert':
        command[1] = int(command[1])
        password1.insert(command[1], command[2])
        print(''.join(password1.password))
    elif command[0] == 'Replace':
        command[2] = int(command[2])
        password1.replace(command[1], command[2])
        print(''.join(password1.password))
    if len(command) > 1:
        if command[1] == 'Upper':
            command[2] = int(command[2])
            password1.make_upper(command[2])
            print(''.join(password1.password))
        else:
            pass
    if len(command) > 1:
        if command[1] == 'Lower':
            command[2] = int(command[2])
            password1.make_lower(command[2])
            print(''.join(password1.password))
        else:
            pass

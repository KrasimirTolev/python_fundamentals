class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    info = input().split()
    if info[0] == 'Stop':
        break
    sender = info[0]
    receiver = info[1]
    content = info[2]
    # sender, receiver, content = info
    email = Email(sender, receiver, content)
    emails.append(email)

indexes = [int(index) for index in input().split(', ')]

for index in indexes:
    emails[index].send()

for i in emails:
    print(i.get_info())


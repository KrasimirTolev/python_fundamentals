class Party:
    def __init__(self):
        self.people = []

    def party_info(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


party = Party()

while True:
    person = input()

    if person == 'End':
        break

    party.people.append(person)

print(party.party_info())

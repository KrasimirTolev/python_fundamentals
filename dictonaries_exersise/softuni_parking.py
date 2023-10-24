class Parking:
    def __init__(self):
        self.registered = {}

    def registering(self, name, plate):
        if name not in self.registered:
            self.registered[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {self.registered[name]}")

    def unregistering(self, name):
        if name not in self.registered:
            print(f"ERROR: user {name} not found")
        else:
            del self.registered[name]
            print(f"{name} unregistered successfully")


parking = Parking()
n = int(input())
for i in range(n):
    username = input().split()
    if username[0] == 'register':
        parking.registering(username[1], username[2])
    elif username[0] == 'unregister':
        parking.unregistering(username[1])

for k, v in parking.registered.items():
    print(f'{k} => {v}')
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_cost = 0
shield_brake = 0


for lost_fight in range(1, lost_fights_count + 1):
    if lost_fight % 2 == 0:
        total_cost += helmet_price
    if lost_fight % 3 == 0:
        total_cost += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        total_cost += shield_price
        shield_brake += 1
        if shield_brake % 2 == 0:
            total_cost += armor_price

print(f'Gladiator expenses: {total_cost:.2f} aureus')

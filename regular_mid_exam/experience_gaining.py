exp_needed = float(input())
count_battle = int(input())
battle_earned_exp = 0
exp = 0


for battle in range(1, count_battle + 1):
    exp_earned = float(input())
    if battle % 3 == 0:
        exp_earned *= 1.15
    if battle % 5 == 0:
        exp_earned *= 0.9
    if battle % 3 == 0 and battle % 5 == 0:
        exp_earned *= 1.05
    exp += exp_earned
    battle_earned_exp = battle
    if exp >= exp_needed:
        print(f'Player successfully collected his needed experience for {battle_earned_exp} battles.')
        break

if exp_needed > exp:
    print(f'Player was not able to collect the needed experience, {exp_needed - exp:.2f} more needed.')


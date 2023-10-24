def free_spots(n, wagons):
    for wagon in range(len(wagons)):
        while True:
            if wagons[wagon] < 4 and n > 0:
                wagons[wagon] += 1
                n -= 1
            else:
                break
    wagons_str = ' '.join(str(_) for _ in wagons)
    if wagons[-1] < 4:
        print('The lift has empty spots!')
        print(wagons_str)
    elif wagons[-1] == 4 and n > 0:
        print(f"There isn't enough space! {n} people in a queue!")
        print(wagons_str)
    elif wagons[-1] == 4 and n == 0:
        print(wagons_str)


people = int(input())
wagons_input = list(map(int, input().split()))
free_spots(people, wagons_input)

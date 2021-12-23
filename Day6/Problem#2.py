file_name = "Day6/Day6Input.txt"
days = 80

with open(file_name) as file:
    line = file.readline().strip().split(',')
    all_fish = {t: line.count(str(t)) for t in range(9)}

    for day in range(1, days + 1):
        new_fish = 0
        for timer, value in all_fish.items():
            if timer > 1:
                if value != 0:
                    all_fish[timer - 1] = value
                    all_fish[timer] = 0
            elif timer == 0:
                if value != 0:
                    new_fish += value
            elif timer == 1:
                if value != 0:
                    all_fish[0] = value
                    all_fish[1] = 0
                else:
                    all_fish[0] = 0

        if new_fish:
            all_fish[8] += new_fish
            all_fish[6] += new_fish

        # print(f"Day {day} ({sum(all_fish.values())}): {all_fish}\n")  # Uncomment this line to see the fish populace changing each day

    print(f"\nAfter {days} days, the total number of lanternfish is: {sum(all_fish.values())}")

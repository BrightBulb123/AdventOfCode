file_name = "Day6/Day6Input.txt"
days = 80

with open(file_name) as file:
    all_fish = file.readline().strip().split(',')

    for _ in range(1, days+1):
        temp = all_fish.copy()
        for idx, fish in enumerate(all_fish):
            fish = int(fish) - 1
            if fish == -1:
                temp.append('8')
                fish = 6

            temp[idx] = str(fish)

        all_fish = temp.copy()
    print(f"\nAfter {days} days, the total number of lanternfish is: {len(all_fish)}")

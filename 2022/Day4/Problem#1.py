file_name = "2022/Day4/Day4Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

pairs = [pair.split(',') for pair in lines]

total = 0
for range_1, range_2 in pairs:
    range_1 = list(map(int, range_1.split('-')))
    range_1 = range(range_1[0], range_1[1]+1)
    range_2 = list(map(int, range_2.split('-')))
    range_2 = range(range_2[0], range_2[1]+1)

    if set(range_1).issubset(set(range_2)) or set(range_2).issubset(set(range_1)):
        total += 1

print(total)

import string

file_name = "2022/Day3/Day3Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

total = 0
for line1, line2, line3 in zip(lines[::3], lines[1::3], lines[2::3]):
    group = [line1, line2, line3]
    l_s_1, l_s_2, l_s_3 = set(group[0]), set(group[1]), set(group[2])
    letter = list(l_s_1 & l_s_2 & l_s_3)[0]
    total += (
        (string.ascii_lowercase.index(letter) + 1)
        if letter.islower()
        else (26 + (string.ascii_uppercase.index(letter) + 1))
    )

print(total)

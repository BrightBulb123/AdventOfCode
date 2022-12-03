import string

file_name = "2022/Day3/Day3Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

total = 0
for line in lines:
    l_s = [line[: len(line) // 2], line[len(line) // 2 :]]
    l_s_1, l_s_2 = set(l_s[0]), set(l_s[1])
    letter = list(l_s_1.intersection(l_s_2))[0]
    total += (
        (string.ascii_lowercase.index(letter) + 1)
        if letter.islower()
        else (26 + (string.ascii_uppercase.index(letter) + 1))
    )

print(total)

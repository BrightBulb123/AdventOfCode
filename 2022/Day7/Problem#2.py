file_name = "2022/Day7/Day7TestInput.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

print(lines)

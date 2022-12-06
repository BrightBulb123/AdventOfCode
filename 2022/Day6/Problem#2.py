file_name = "2022/Day6/Day6Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

line = lines[0]


indices = []
for i in range(len(line) - 14 + 1):
    window = line[i : i + 14]
    chunk_list = list(window)
    chunk_set = set(chunk_list)
    if len(chunk_set) == len(chunk_list):
        indices.append(i + 14)

print(indices)

file_name = "2022/Day6/Day6Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

line = lines[0]


indices = []
for i, a, b, c, d in zip(range(len(line)), line, line[1:], line[2:], line[3:]):
    chunk_list = [a, b, c, d]
    chunk_set = set(chunk_list)
    if len(chunk_set) == len(chunk_list):
        indices.append(i + 4)  # "+ 4" because it is after the last character of the sequence and the sequence is 4 characters long

print(indices)

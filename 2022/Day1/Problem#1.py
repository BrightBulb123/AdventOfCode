file_name = "2022/Day1/Day1Input.txt"


with open(file_name) as file:
    lines = file.readlines()

lines = "".join(lines)
data = lines.split("\n\n")
data = map(lambda x: x.split("\n"), data)
data = [[int(s) for s in elf_data] for elf_data in data]
data = {k+1:sum(v) for k,v in enumerate(data)}

maximum = max(data, key=data.get)


print(data[maximum])

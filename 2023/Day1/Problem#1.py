import re


file_name = "2023/Day1/Day1Input.txt"


with open(file_name) as file:
    lines = map(lambda x: x.replace("\n", ""), file.readlines())

digits_pattern = re.compile(r"[1-9]")

total = 0
for line in lines:
    matches = list(re.finditer(digits_pattern, line))
    first, last = matches[0].group(0), matches[-1].group(0)
    calibration_value = int(f"{first}{last}")
    total += calibration_value


print(total)

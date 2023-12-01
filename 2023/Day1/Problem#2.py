import regex as re


file_name = "2023/Day1/Day1Input.txt"


with open(file_name) as file:
    lines = map(lambda x: x.replace("\n", ""), file.readlines())

words_to_digits = {word:(digit+1) for digit, word in enumerate("one|two|three|four|five|six|seven|eight|nine|ten".split("|"))}
digits_pattern = re.compile(r"[1-9]|one|two|three|four|five|six|seven|eight|nine|ten")

total = 0
for line in lines:
    matches = list(re.finditer(digits_pattern, line, overlapped=True))
    first, last = matches[0].group(0), matches[-1].group(0)
    if first.isalpha():
        first = words_to_digits[first]
    if last.isalpha():
        last = words_to_digits[last]
    calibration_value = int(f"{first}{last}")
    total += calibration_value


print(total)

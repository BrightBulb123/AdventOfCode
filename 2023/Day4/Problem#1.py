import re


file_name = "2023/Day4/Day4Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


card_points: dict[int, int] = {}
for line in lines:
    card_num = int(re.match(r"Card\s+\d+", line)[0].replace("Card ", ""))

    line = re.sub(f"Card\\s+{card_num}:\\s+", "", line)
    winning_numbers, your_numbers = re.split(r"\s+\|\s+", line)
    winning_numbers = list(map(int, re.split(r"\s+", winning_numbers)))
    your_numbers = list(map(int, re.split(r"\s+", your_numbers)))

    current_points = sum(your_number in winning_numbers for your_number in your_numbers)
    card_points[card_num] = 2 ** (current_points - 1) if current_points != 0 else 0


print(sum(card_points.values()))

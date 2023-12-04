import itertools
import re


file_name = "2023/Day4/Day4Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


TOTAL_CARDS = len(lines)
card_counts: dict[int, int] = {}
for line in lines:
    card_num = int(re.match(r"Card\s+\d+", line)[0].replace("Card ", ""))
    card_counts[card_num] = (
        1 if card_num not in card_counts else card_counts[card_num] + 1
    )  # The original card is always counted

    line = re.sub(f"Card\\s+{card_num}:\\s+", "", line)
    winning_numbers, your_numbers = re.split(r"\s+\|\s+", line)
    winning_numbers = list(map(int, re.split(r"\s+", winning_numbers)))
    your_numbers = list(map(int, re.split(r"\s+", your_numbers)))

    current_points = sum(your_number in winning_numbers for your_number in your_numbers)
    for _, next_card_num in itertools.product(range(card_counts[card_num]), range(card_num + 1, card_num + current_points + 1)):
        if next_card_num <= TOTAL_CARDS:
            card_counts[next_card_num] = (
                card_counts[next_card_num] + 1 if next_card_num in card_counts else 1
            )  # Add 1 to the next card count if it exists, else, make it equal to 1


print(sum(card_counts.values()))

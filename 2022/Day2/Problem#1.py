file_name = "2022/Day2/Day2Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = "".join(lines)
lines = lines.split("\n")
lines = list(map(lambda x: x.split(" "), lines))

shapes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
scores = {"Rock": 1, "Paper": 2, "Scissors": 3, "Win": 6, "Draw": 3, "Lose": 0}
states = {
    ("Rock", "Rock"): "Draw",
    ("Rock", "Paper"): "Lose",
    ("Rock", "Scissors"): "Win",
    ("Paper", "Rock"): "Win",
    ("Paper", "Paper"): "Draw",
    ("Paper", "Scissors"): "Lose",
    ("Scissors", "Rock"): "Lose",
    ("Scissors", "Paper"): "Win",
    ("Scissors", "Scissors"): "Draw",
}

total = 0
for round in lines:
    opponent, player = round
    opponent, player = shapes[opponent], shapes[player]
    round_score = scores[states[(player, opponent)]] + scores[player]
    total += round_score

print(total)

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
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
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
    opponent, player_must = round
    opponent, player_must = shapes[opponent], shapes[player_must]

    if player_must == "Draw":
        player = opponent
    elif player_must == "Lose":
        for k, v in states.items():
            if v == "Lose" and opponent == k[1]:
                player = k[0]

    elif player_must == "Win":
        for k, v in states.items():
            if v == "Win" and opponent == k[1]:
                player = k[0]
    round_score = scores[states[(player, opponent)]] + scores[player]
    total += round_score

print(total)

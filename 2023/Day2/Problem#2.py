import re


file_name = "2023/Day2/Day2Input.txt"


with open(file_name) as file:
    lines = map(lambda x: x.replace("\n", ""), file.readlines())


class Game:
    def __init__(self, game_id: int, counts: dict[str, int]) -> None:
        self.id = game_id
        self.counts = counts
        self.power = self.counts["Red"] * self.counts["Blue"] * self.counts["Green"]


games = []
for line in lines:
    game_id = int(re.search(r"\d+", line)[0])
    subgames = line[line.find(":") + 2 :].split(
        "; "
    )  # Splice the string to obtain the substring after the colon (:), and just split every "; " from there to separate out the draws

    counts = {"Red": 0, "Green": 0, "Blue": 0}
    for subgame in subgames:
        draws = subgame.split(", ")
        for draw in draws:
            num, colour = draw.split(" ")
            num = int(num)
            colour = colour.title()  # "green" -> "Green"
            counts[colour] = max(counts[colour], num)

    current_game = Game(game_id=game_id, counts=counts)
    games.append(current_game)

total = sum(game.power for game in games)
print(total)

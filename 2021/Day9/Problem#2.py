file_name = "2021/Day9/Day9TestInput.txt"


with open(file_name) as file:
    lines = file.readlines()


lines = list(map(lambda x: x.replace("\n", ""), lines))


def adjacents_finder(depth: int, idx: int, lines: list[str]) -> dict[str, int]:
    """Check up, down, left, and right of the current element at depth `depth` and index `idx`, and return True if it is the lowest value among them."""

    up, down, left, right = None, None, None, None
    if depth != 0:
        up = int(lines[depth - 1][idx])
    if depth != len(lines) - 1:
        down = int(lines[depth + 1][idx])

    if idx != 0:
        left = int(lines[depth][idx - 1])
    if idx != len(lines[depth]) - 1:
        right = int(lines[depth][idx + 1])

    return {"up": up, "down": down, "left": left, "right": right}


adjacents = {}
for depth, row in enumerate(lines):
    for idx, char in enumerate(row):
        adjacents[(depth, idx)] = adjacents_finder(depth=depth, idx=idx, lines=lines)


def basin_finder(adjacents: dict[tuple[int], dict[str, int]]) -> None:
    for co_ords in adjacents:
        num = int(lines[co_ords[0]][co_ords[1]])


basin_finder(adjacents=adjacents)

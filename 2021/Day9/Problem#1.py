file_name = "2021/Day9/Day9Input.txt"


with open(file_name) as file:
    lines = file.readlines()


lines = list(map(lambda x: x.replace('\n', ''), lines))

def check_cell(depth: int, idx: int, lines: list[str]) -> bool:
    """Check up, down, left, and right of the current element at depth `depth` and index `idx`, and return True if it is the lowest value among them."""

    up, down, left, right, num = 10, 10, 10, 10, int(lines[depth][idx])
    if depth != 0:
        up = int(lines[depth - 1][idx])
    if depth != len(lines) - 1:
        down = int(lines[depth + 1][idx])

    if idx != 0:
        left = int(lines[depth][idx - 1])
    if idx != len(lines[depth]) - 1:
        right = int(lines[depth][idx + 1])

    if up != None and up < num:
        return False

    if down != None and down < num:
        return False

    if left != None and left < num:
        return False

    if right != None and right < num:
        return False

    return True


final = []
for depth, row in enumerate(lines):
    final.extend(int(char) for idx, char in enumerate(row) if check_cell(depth=depth, idx=idx, lines=lines))

print(sum(map(lambda x: x+1, final)))

file_name = "2022/Day8/Day8Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


lines = [[int(i) for i in line] for line in lines]

FOREST_WIDTH = len(lines[0])
highest_scenic_score = 0
for line_num, line in enumerate(lines):
    for column_num in range(FOREST_WIDTH):
        co_ords = (column_num, line_num)  # (x,y)
        number = line[column_num]
        scenic_score = 0

        # The edges will never have a highest scenic score.
        if line_num in [0, len(lines) - 1]:  # Top and bottom edges
            continue
        if column_num in [0, len(line) - 1]:  # Left and right edges
            continue

        numbers_before = line[:column_num]
        numbers_after = line[column_num + 1 :]  # inclusive:exclusive
        numbers_lower_before = [i < number for i in numbers_before]
        numbers_lower_after = [i < number for i in numbers_after]
        left = 0
        for n in numbers_lower_before[::-1]:  # Go through backwards
            left += 1
            if not n:
                break
        right = 0
        for n in numbers_lower_after:
            right += 1
            if not n:
                break
        numbers_above = [l[column_num] for l in lines[:line_num]]
        numbers_below = [
            l[column_num] for l in lines[line_num + 1 :]
        ]  # inclusive:exclusive
        numbers_lower_above = [i < number for i in numbers_above]
        numbers_lower_below = [i < number for i in numbers_below]
        up = 0
        for n in numbers_lower_above[::-1]:  # Go through backwards
            up += 1
            if not n:
                break
        down = 0
        for n in numbers_lower_below:
            down += 1
            if not n:
                break
        scenic_score = left * right * up * down
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score


print(highest_scenic_score)

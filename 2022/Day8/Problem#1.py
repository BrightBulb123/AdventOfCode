file_name = "2022/Day8/Day8Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


lines = [[int(i) for i in line] for line in lines]

FOREST_WIDTH = len(lines[0])
visible_trees = []
for line_num, line in enumerate(lines):
    for column_num in range(FOREST_WIDTH):
        co_ords = (column_num, line_num)  # (x,y)
        number = line[column_num]

        if line_num in [0, len(lines) - 1]:  # Top and bottom edges
            visible_trees.append(co_ords)
            continue
        if column_num in [0, len(line) - 1]:  # Left and right edges
            visible_trees.append(co_ords)
            continue

        numbers_before = line[:column_num]
        numbers_after = line[column_num + 1 :]  # inclusive:exclusive
        numbers_lower_before = [i < number for i in numbers_before]
        numbers_lower_after = [i < number for i in numbers_after]
        if all(numbers_lower_before) or all(numbers_lower_after):
            visible_trees.append(co_ords)
            continue

        numbers_above = [l[column_num] for l in lines[:line_num]]
        numbers_below = [
            l[column_num] for l in lines[line_num + 1 :]
        ]  # inclusive:exclusive
        numbers_lower_above = [i < number for i in numbers_above]
        numbers_lower_below = [i < number for i in numbers_below]
        if all(numbers_lower_above) or all(numbers_lower_below):
            visible_trees.append(
                co_ords
            )  # This one doesn't need a `continue` since it's at the end


print(len(visible_trees))

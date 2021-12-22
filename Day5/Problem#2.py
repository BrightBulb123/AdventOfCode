file_name = "Day5/Day5Input.txt"

with open(file_name) as file:
    co_ords = []
    for line in file:
        line = line.strip().split(" -> ")
        first_pair = tuple(int(i) for i in line[0].split(","))
        second_pair = tuple(int(i) for i in line[1].split(","))
        co_ords.append((first_pair, second_pair))

    def max_finder(co_ordinates: list, var: str) -> int:
        temp = []
        for pair in co_ordinates:
            for co_ord in pair:
                if var == "x":
                    temp.append(co_ord[0])
                else:
                    temp.append(co_ord[1])

        return max(temp)

    max_y = max_finder(co_ords, "y")
    max_x = max_finder(co_ords, "x")
    table = [("".join("." for _ in range(max_y + 1))) for _ in range(max_x + 1)]

    for co_ords_pair in co_ords:
        x1, x2, y1, y2 = co_ords_pair[0][0], co_ords_pair[1][0], co_ords_pair[0][1], co_ords_pair[1][1]
        x_step = -1 if (x1 > x2) else 1
        y_step = -1 if (y1 > y2) else 1
        x_co_ords = [x for x in range(x1, x2+(x_step), x_step)]
        y_co_ords = [y for y in range(y1, y2+(y_step), y_step)]

        if len(x_co_ords) > len(y_co_ords):
            y_co_ords *= len(x_co_ords)
        elif len(x_co_ords) < len(y_co_ords):
            x_co_ords *= len(y_co_ords)

        for x, y in zip(x_co_ords, y_co_ords):
            column = list(table[x])
            try:
                column[y] = int(column[y])
                column[y] += 1
            except ValueError:
                column[y] = '1'

            column = "".join(str(i) for i in column)
            table[x] = column

    table = ["".join(row) for row in (list(zip(*table)))]

    points = 0
    for row in table:
        for element in row:
            if (element != '.') and int(element) > 1:
                points += 1

    # print(*table, sep='\n')  # Uncomment this line to print out the entire diagram of the hydrothermal vent
    print(f"\nPoints: {points}")

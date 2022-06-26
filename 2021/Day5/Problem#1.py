file_name = "Day5/Day5Input.txt"

with open(file_name) as file:
    co_ords = []
    for line in file:
        line = line.strip().split(" -> ")
        first_pair = tuple(int(i) for i in line[0].split(","))
        second_pair = tuple(int(i) for i in line[1].split(","))
        co_ords.append(sorted((first_pair, second_pair)))

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
        y_co_ords = tuple(i[1] for i in co_ords_pair)
        x_co_ords = tuple(i[0] for i in co_ords_pair)

        x1, x2 = x_co_ords
        y1, y2 = y_co_ords

        if (not x1 == x2) and (not y1 == y2):
            continue

        y_co_ords = tuple(sorted(i[1] for i in co_ords_pair))
        x_co_ords = tuple(sorted(i[0] for i in co_ords_pair))

        for x in range(x_co_ords[0], x_co_ords[1] + 1):
            row = table[x]
            for y in range(y_co_ords[0], y_co_ords[1] + 1):
                row = list(row)
                try:
                    row[y] = int(row[y])
                    row[y] += 1
                except ValueError:
                    row[y] = 1
                row = "".join(str(i) for i in row)
                table[x] = row

    table = [list(i) for i in zip(*table)]

    points = 0
    for row in table:
        for element in row:
            if (element != '.') and int(element) > 1:
                points += 1
        print(*row, sep='')
    print(f"\nPoints: {points}")

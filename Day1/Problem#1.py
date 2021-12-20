with open("Day1Input.txt") as file:
    count = 0
    c = int(file.readline())
    n = int(file.readline())

    while True:
        if n > c:
            count += 1

        c = n

        try:
            n = int(file.readline())
        except ValueError:
            break

    print(count)

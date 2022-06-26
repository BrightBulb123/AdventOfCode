with open(r"Day2\Day2Input.txt") as file:
    h = 0
    d = 0
    a = 0

    while True:
        instruction = file.readline()
        if not instruction:
            break
        else:
            instruction = instruction.split(" ")

        amount = int(instruction[1])
        instruction = instruction[0]

        if instruction == "down":
            a += amount
        elif instruction == "forward":
            h += amount
            d += (a * amount)
        else:
            a -= amount

    print((h * d))

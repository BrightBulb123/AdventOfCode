with open(r"Day1\Day1Input.txt") as file:
    count = 0

    f_list = [int(file.readline())]
    s_list = []

    while True:
        try:
            line = (int(file.readline()))
        except ValueError:
            break
        s_list.append(line)

        if len(s_list) > 3:
            s_list = s_list[1:]

        if (len(f_list) == 3 and len(s_list) == 3) and (sum(s_list) > sum(f_list)):
            count += 1

        f_list.append(line)

        if len(f_list) > 3:
            f_list = f_list[1:]

    print(count)


# Papa's Solution:

# with open(r"Day1\Day1Input.txt") as file:

#     count = 0

#     previous = []
#     current = []

#     window = 0

#     for line in file:
#         current.append(int(line))
#         window += 1

#         if(window < 3):
#             continue

#         if previous and sum(current) > sum(previous):
#             count += 1

#         previous = current
#         current = current[1:]
#         window = 2

#     print(count)

setup = False
digits = None
count = 0
l = 0


def setup_array(line):
    return [0 for _ in line]


with open("Day3/Day3Input.txt") as file:
    for line in file:
        line = line.strip()
        count += 1
        if not setup:
            l = len(line)
            digits = setup_array(line)
            setup = True

        for i in range(l):
            if(line[i] == "1"):
                digits[i] = digits[i]+1


h = count/2

gamma = "".join("1" if i > h else "0" for i in digits)
epsilon = "".join("0" if i > h else "1" for i in digits)
gammad = int(gamma, 2)
epsilond = int(epsilon, 2)
print("gamma: ", gammad, gamma)
print("epsilon", epsilond, epsilon)
power = gammad*epsilond
print(power)

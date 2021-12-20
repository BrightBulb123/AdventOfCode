fileName = "Day3/Day3Input.txt"


def read_file(f):
    with open(fileName) as file:
        return [line.strip() for line in file]


def count_ones(ar):

    digits = [0 for _ in ar[0]]
    l = len(ar[0])

    for line in ar:
        for i in range(l):
            if(line[i] == "1"):
                digits[i] = digits[i]+1

    return digits


def calc_gamma(ones, half: float):
    return "".join("1" if float(i) >= half else "0" for i in ones)


def calc_epsilon(ones, half: float):
    return "".join("0" if float(i) >= half else "1" for i in ones)


def mult_binaries(gamma, epsilon):
    gammad = int(gamma, 2)
    epsilond = int(epsilon, 2)
    return gammad*epsilond


def compare_index(ar, idx, val):
    return [a for a in ar if a[idx] == val]


def calc_oxygen(arr, gamma, ix):
    l = len(arr)
    if(l == 1):
        return arr[0]

    c = compare_index(arr, ix, gamma[ix])

    o = count_ones(c)

    g = calc_gamma(o, len(c)/2)

    return calc_oxygen(c, g, ix+1)


def calc_carbon(arr, epsilon, ix):
    l = len(arr)
    if(l == 1):
        return arr[0]

    c = compare_index(arr, ix, epsilon[ix])

    o = count_ones(c)

    e = calc_epsilon(o, len(c)/2)

    return calc_carbon(c, e, ix+1)


def main():
    arr = read_file(fileName)
    digits = count_ones(arr)
    half = len(arr)/2

    gam = calc_gamma(digits, half)
    eps = calc_epsilon(digits, half)
    print(mult_binaries(gam, eps))

    ox = calc_oxygen(arr, gam, 0)
    cr = calc_carbon(arr, eps, 0)

    print(f"Oxygen: {ox}")
    print(f"Carbon: {cr}")

    print(mult_binaries(ox, cr))


if __name__ == "__main__":
    main()

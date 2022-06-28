file_name = "2021/Day8/Day8Input.txt"

with open(file_name) as file:
    lines = file.readlines()


def decoder(display_key: dict[int, str], key: dict[str, str], l: str):
    temp = []
    key = {v: k for k, v in key.items()}
    display_key = {v: k for k, v in display_key.items()}
    temp.extend(display_key["".join(sorted("".join(key[i] for i in out)))] for out in l)
    return [int("".join(str(i) for i in temp))]


outs = []
display_mappings = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

for line in lines:
    line = line.replace("\n", "")
    inp, out = map(lambda x: x.split(" "), line.split(" | "))
    inp.sort(key=lambda x: len(x))

    temp = []
    for i in inp[1]:
        temp2 = []
        temp2.extend(inp[0])
        temp2.extend(inp[1])
        if temp2.count(i) == 1:
            temp.append(i)

    segments = {"b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "a": temp[0]}
    wires = [temp[0]]
    for i in inp[3:6]:
        if not set(inp[0]) - set(i):
            dig_3 = i
            temp = inp[2].replace(inp[0][0], "").replace(inp[0][1], "")
            temp2 = i.replace(inp[0][0], "").replace(inp[0][1], "")
            segments["d"] = list(set(temp).intersection(set(temp2)))[0]
            wires.append(segments["d"])
            segments["b"] = temp.replace(segments["d"], "")[0]
            wires.append(segments["b"])
            segments["g"] = (
                temp2.replace(segments["d"], "")
                .replace(segments["b"], "")
                .replace(segments["a"], "")[0]
            )
            wires.append(segments["g"])

    for i in inp[3:6]:
        if type(segments["b"]) == str and i != dig_3 and str(segments["b"]) not in i:
            dig_2 = i
            segments["c"] = list(set(inp[0]).intersection(set(i)))[0]
            wires.append(segments["c"])
            break

    for i in dig_2:
        if i not in wires:
            segments["e"] = i
            wires.append(segments["e"])
            break

    for k, v in segments.items():
        if v == []:
            segments[k] = list(set(segments.keys()).difference(set(wires)))[0]
            wires.append(segments[k])
            break

    outs.extend(decoder(display_mappings, segments, out))


print(sum(outs))

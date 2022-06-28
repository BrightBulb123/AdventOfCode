# Advent of Code - Day 8 - Seven Segment Search

---

## Problem

### Overview

The seven segments of a seven-segment display ([[#Figure 1 - Seven-Segment Display|Figure 1]]) are each labelled letters $a$ through to $g$ (7 segments). Each segment is signalled to be on by *wires*, which are also labelled the letters $a$ through to $g$.

Unfortunately, the wires have been jumbled. The segments are still labelled like they are in [[#Figure 1 - Seven-Segment Display|Figure 1]], but the wire labels have been mixed up. Due to this, a wire labelled $a$ might **not** correspond to the segment labelled $a$.

Essentially, decode a string given in a format which consists of 10 unique permutations of characters $a$ to $g$ (ergo, 10 digits), with each character mapping onto a segment on a seven-segment display ([[#Figure 1 - Seven-Segment Display|Figure 1]]). These unique permutations of 7 characters may appear in any number from 1 through to 7. These permutations are followed by a delimiter (` | `), which separates the *input* (left of the delimiter) from the *output* (right of the delimiter).

Each element (separated by a space) in the string corresponds to one digit on the seven-segment display ([[#Figure 1 - Seven-Segment Display|Figure 1]]).

### Part One

Figure out how many times do the digits 1, 4, 7, or 8 appear in the *output* values.

### Part Two

What do you get if you add up all of the output values?

### Example Input

```plaintext
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
```

## Solution

> [!Note] Note
> Certain numbers of segments correspond with certain digits on a seven-segment display:
> - 2 segments on --> 1
> - 3 segments on --> 7
> - 4 segments on --> 4
> - 5 segments on --> 2, 3, 5
> - 6 segments on --> 0, 6, 9
> - 7 segments on --> 8

### Example - Worked Out Manually

![[Day 8 - Example Working Out.excalidraw]]

### Decoding numbers

#### Logic

1. Complete preliminary tasks.
2. Sort the list of inputs based on element length in ascending order.
3. Compare the 2-segment element (1) to the 3-segment element (7).
    - The odd wire out corresponds to segment $a$.
4. Compare the 2-segment element (1) to the 5-segment element(s) (2, 3, 5).
    1. Check which 5-segment element (3) has both wires of the 2-segment element (1).
        1. Compare the 4-segment element (4) with the 5-segment element (3).
            1. Check which wire (apart from the ones in the 2-segment element (1)) is common in this 5-segment element (3) and the 4-segment element (4).
                - The common wire corresponds to segment $d$.
                - The remaining wire in the 4-segment element (4) corresponds to segment $b$.
                - The remaining wire in the 5-segment element (3) corresponds to segment $g$.
    2. Check which remaining 5-segment element (2) does not contain the wire corresponding to segment $b$.
        - The common wire between this 5-segment element (2) and the 2-segment element (1) corresponds to segment $c$.
        - The remaining unidentified wire in the 5-segment element (2) corresponds to segment $e$.
        - The remaining wire in the 2-segment element (1) corresponds to segment $f$.

#### Code

```py
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
```

### Solution - Part One

```py
# previous code


count = 0
for num in outs:
    for i in str(num):
        if i in ['1', '4', '7', '8']:
            count += 1

print(count)
```

### Solution - Part Two

```py
# previous code


print(sum(outs))
```

## Figure 1 - Seven-Segment Display

```plaintext
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```


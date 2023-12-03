import re


file_name = "2023/Day3/Day3Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


SCHEMATIC_LENGTH = len(lines[0])
symbols_pattern = re.compile(r"[^\.|\d]")  # Matches any "symbol"
part_numbers = []
line_symbol_locations = {}
line_number_locations = {}
for idx, line in enumerate(lines):
    num_spans = [
        m.span() for m in re.finditer(r"\d+", line)
    ]  # Checks the spans of the numbers in the current line
    symbol_locations = [
        m.span()[0] for m in re.finditer(symbols_pattern, line)
    ]  # Checks the locations of the symbols in the current line
    line_number_locations[idx] = num_spans
    line_symbol_locations[idx] = symbol_locations

for line_num in range(len(lines)):
    sym_locs = line_symbol_locations[line_num]
    for sym in sym_locs:
        if (line_num != 0) or (line_num != (len(lines) - 1)):
            num_locs = line_number_locations[line_num - 1]  # Check the numbers in the line above
            for num in num_locs:
                num_range = range(num[0], num[-1])
                
                if (sym in num_range) or ((sym - 1) in num_range) or ((sym + 1) in num_range):  # Directly, then diagonals
                    part_numbers.append(int(lines[line_num - 1][num[0]:num[-1]]))

            num_locs = line_number_locations[line_num + 1]  # Check the numbers in the line below
            for num in num_locs:
                num_range = range(num[0], num[-1])

                if (sym in num_range) or ((sym - 1) in num_range) or ((sym + 1) in num_range):  # Directly, then diagonals
                    part_numbers.append(int(lines[line_num + 1][num[0]:num[-1]]))
        
        num_locs = line_number_locations[line_num]
        for num in num_locs:
            if sym != 0 and num[-1] == sym:
                part_numbers.append(int(lines[line_num][num[0]:num[-1]]))
            if sym != (SCHEMATIC_LENGTH - 1) and num[0] == (sym + 1):
                part_numbers.append(int(lines[line_num][num[0]:num[-1]]))


print(sum(part_numbers))

import re
from math import prod


file_name = "2023/Day3/Day3Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


SCHEMATIC_LENGTH = len(lines[0])
gears_pattern = re.compile(r"\*")  # Matches any "gear" (just any star for now, validate later)
line_gear_locations = {}
line_number_locations = {}
for idx, line in enumerate(lines):
    num_spans = [
        m.span() for m in re.finditer(r"\d+", line)
    ]  # Checks the spans of the numbers in the current line
    gear_locations = [
        m.span()[0] for m in re.finditer(gears_pattern, line)
    ]  # Checks the locations of the symbols in the current line
    line_number_locations[idx] = num_spans
    line_gear_locations[idx] = gear_locations

gear_ratios = []
for line_num in range(len(lines)):
    gear_locs = line_gear_locations[line_num]
    for gear in gear_locs:
        gear_ratio_numbers = []
        if (line_num != 0) or (line_num != (len(lines) - 1)):
            num_locs = line_number_locations[line_num - 1]  # Check the numbers in the line above
            for num in num_locs:
                num_range = range(num[0], num[-1])
                
                if (gear in num_range) or ((gear - 1) in num_range) or ((gear + 1) in num_range):  # Directly, then diagonals
                    gear_ratio_numbers.append(int(lines[line_num - 1][num[0]:num[-1]]))

            num_locs = line_number_locations[line_num + 1]  # Check the numbers in the line below
            for num in num_locs:
                num_range = range(num[0], num[-1])

                if (gear in num_range) or ((gear - 1) in num_range) or ((gear + 1) in num_range):  # Directly, then diagonals
                    gear_ratio_numbers.append(int(lines[line_num + 1][num[0]:num[-1]]))
        
        num_locs = line_number_locations[line_num]
        for num in num_locs:
            if gear != 0 and num[-1] == gear:
                gear_ratio_numbers.append(int(lines[line_num][num[0]:num[-1]]))
            if gear != (SCHEMATIC_LENGTH - 1) and num[0] == (gear + 1):
                gear_ratio_numbers.append(int(lines[line_num][num[0]:num[-1]]))
        
        if len(gear_ratio_numbers) == 2:
            gear_ratios.append(prod(gear_ratio_numbers))


print(sum(gear_ratios))

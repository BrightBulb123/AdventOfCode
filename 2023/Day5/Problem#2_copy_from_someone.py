# https://github.com/DownDev/advent-of-code/blob/main/2023/05-2.py
from itertools import groupby


file_name = "2023/Day5/Day5TestInput.txt"

with open(file_name) as file:
    lines = file.read().splitlines()

groups = [tuple(group) for not_empty, group in groupby(lines, bool) if not_empty]

seeds, *categories = groups
seeds_ranges = [int(x) for x in seeds[0].split()[1:]]
seeds_numbers = [(seeds_ranges[i], seeds_ranges[i + 1]) for i in range(0, len(seeds_ranges), 2)]

def calculate_overlap(start, end, source, length, destination):
    overlap_start = max(start, source)
    overlap_end = min(end, source + length)
    if overlap_start < overlap_end:
        return [(overlap_start - source + destination, overlap_end - source + destination)]
    return [(start, end)]

for category in categories:
    ranges = [(int(numbers.split()[0]), int(numbers.split()[1]), int(numbers.split()[2])) for numbers in category[1:]]
    sources = []
    for start, end in seeds_numbers:
        for destination, source, length in ranges:
            new_sources = calculate_overlap(start, end, source, length, destination)
            sources.extend(new_sources)
            if new_sources[0] != (start, end):
                break
        else:
            sources.append((start, end))
    seeds_numbers = sources

print(min(seeds_numbers)[0])

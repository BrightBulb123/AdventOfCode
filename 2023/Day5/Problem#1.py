file_name = "2023/Day5/Day5Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


def is_num_in_range(num: int, start: int, range: int) -> bool:
    """Checks if `num` is in the range `[start, start + range)`."""
    return start <= num < start + range


def map_parser(line: str, destination: str, source: str) -> dict[str, int]:
    """Turns `x y z` -> `{destination: x, source: y, "range": z}` for a given line (`x y z`), destination, and source."""
    line = tuple(map(int, line.split(" ")))
    return {attribute: line[idx] for idx, attribute in enumerate((destination, source, "range"))}


seeds = tuple(map(int, lines.pop(0).replace("seeds: ", "").split(" ")))
seeds_to_location_nums = {seed: seed for seed in seeds}
source_to_destination_maps: dict[str, list[dict[str, int]]] = {}
for line in lines:
    if line == "":
        continue
    elif "-to-" in line:
        source, destination = line.replace(" map:", "").split("-to-")
        map_type = f"{source} -> {destination}"
        source_to_destination_maps[map_type] = []
        continue

    line = map_parser(line=line, destination=destination, source=source)
    source_to_destination_maps[map_type].append(line)

for seed in seeds:
    for source_to_destination_map in source_to_destination_maps:
        source, destination = source_to_destination_map.split(" -> ")
        lines = source_to_destination_maps[source_to_destination_map]
        for line in lines:
            if is_num_in_range(num=seeds_to_location_nums[seed], start=line[source], range=line["range"]):
                difference = seeds_to_location_nums[seed] - line[source]
                destination_num = line[destination] + difference
                seeds_to_location_nums[seed] = destination_num
                break
        print(f"Seed: {seed}\t|\tMap: {source_to_destination_map}\t|\tNew: {seeds_to_location_nums[seed]}")
    print('='*100)

print(seeds_to_location_nums)
print(min(seeds_to_location_nums.values()))

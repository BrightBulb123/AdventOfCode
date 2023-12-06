file_name = "2023/Day5/Day5TestInput.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


def is_num_in_range(num: int, start: int, range: int) -> bool:
    """Checks if `num` is in the range `[start, start + range)`."""
    return start <= num < start + range


def map_parser(line: str, destination: str, source: str) -> dict[str, int]:
    """Turns `x y z` -> `{destination: x, source: y, "range": z}` for a given line (`x y z`), destination, and source."""
    line = tuple(map(int, line.split(" ")))
    return {attribute: line[idx] for idx, attribute in enumerate((destination, source, "range"))}


seeds_list = list(map(int, lines.pop(0).replace("seeds: ", "").split(" ")))
seeds: list[tuple[int]] = []
it = iter(seeds_list)
for seed_start in it:
    seed_range = next(it)
    seeds.append((seed_start, seed_start + seed_range))

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

# Trying to go from location -> seed number
# source_num = -1
# for source_to_destination_map_type in source_to_destination_maps.__reversed__():
#     source, destination = source_to_destination_map_type.split(" -> ")
#     lines = source_to_destination_maps[source_to_destination_map_type]
#     if source_num == -1:
#         paths = []
#         current_lowest = -1
#         for line in lines:
#             if current_lowest == -1 or line[destination] < current_lowest:
#                 current_lowest = line[destination]
#                 paths.append(line)
#         min_path = min(paths, key=lambda d: d[destination])
#     else:
#         for line in lines:
#             if is_num_in_range(num=source_num, start=line[destination], range=line['range']):
#                 min_path = line
#                 break

#     source_from_min_path = min_path.get(source)
#     source_num = source_from_min_path if source_from_min_path is not None else source_num
#     print(min_path, source_num)


current_lowest = -1
for seed_tuple in seeds:
    seed = seed_tuple[0]
    while seed < seed_tuple[-1]:
        seed_to_location_num = seed
        for source_to_destination_map in source_to_destination_maps:
            source, destination = source_to_destination_map.split(" -> ")
            lines = source_to_destination_maps[source_to_destination_map]
            for line in lines:
                if is_num_in_range(num=seed_to_location_num, start=line[source], range=line["range"]):
                    difference = seed_to_location_num - line[source]
                    destination_num = line[destination] + difference
                    seed_to_location_num = destination_num
                    break
        #     print(f"Seed: {seed}\t|\tMap: {source_to_destination_map}\t|\tNew: {seed_to_location_num}")
        # print('='*100)
        seed += 1
        if current_lowest == -1 or seed_to_location_num < current_lowest:
            current_lowest = seed_to_location_num

print(f"Most recent seed: {seed}\t|\tCurrent lowest: {current_lowest}")

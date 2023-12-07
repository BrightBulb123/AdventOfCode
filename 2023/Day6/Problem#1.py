import re
from math import floor, ceil, sqrt, prod
from pprint import pprint


file_name = "2023/Day6/Day6Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


def bounds_getter(max_time: int, record_distance: int) -> tuple[int]:
    """ Computes the intersection between $f(x)$ and $g(x)$, where $f(x) = -t^2 + `max_time`t$ and $(x) = `record_distance`$.
        The integer values that *can* represent how long to hold the button for lie within the range between the two intersections."""
    a = -1
    b = max_time
    c = -record_distance
    lower_bound = ((-b) + sqrt((b**2) - 4 * a * c)) / (2 * a)
    upper_bound = ((-b) - sqrt((b**2) - 4 * a * c)) / (2 * a)
    if lower_bound != ceil(lower_bound):
        lower_bound = ceil(lower_bound)
    else:
        lower_bound = ceil(lower_bound) + 1
    if upper_bound != floor(upper_bound):
        upper_bound = floor(upper_bound)
    else:
        upper_bound = ceil(upper_bound) - 1
    return tuple(map(int, (lower_bound, upper_bound)))


max_times = []
record_distances = []
for line in lines:
    if "Time" in line:
        times = map(int, re.split(r"\s+", re.sub(r"Time:\s+", "", line)))
        max_times.extend(times)
    else:
        distances = map(int, re.split(r"\s+", re.sub(r"Distance:\s+", "", line)))
        record_distances.extend(distances)

num_races = len(max_times)
ways_to_beat_each_race = {}
for max_time, record_distance, race_num in zip(
    max_times, record_distances, range(1, num_races + 1)
):
    bounds = bounds_getter(max_time=max_time, record_distance=record_distance)
    t_values = range(bounds[0], bounds[-1] + 1)
    ways_to_beat_each_race[race_num] = len(t_values)

pprint(ways_to_beat_each_race)
print(
    f"Multiplied ways to beat each race: {prod(iter(ways_to_beat_each_race.values()))}"
)

# Thanks to the AoC subreddit for suggesting the LCM method...
from math import lcm


file_name = "2023/Day8/Day8Input.txt"


with open(file_name) as file:
    lines = file.read().splitlines()


class WrongDirection(Exception):
    pass


class Node:
    all_ids = []

    def __init__(
        self, identifier: str, left_identifier: str = None, right_identifier: str = None
    ) -> None:
        self.identifier = identifier
        Node.all_ids.append(self.identifier)
        self.ending_identifier = self.identifier[-1]
        self.left_identifier = (
            self.identifier if left_identifier == self.identifier else left_identifier
        )
        self.right_identifier = (
            self.identifier if right_identifier == self.identifier else right_identifier
        )

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Node):
            return NotImplemented
        return self.identifier == __value.identifier

    def __hash__(self) -> int:
        return hash(self.identifier)


all_nodes = {}
directions = lines.pop(0)
for line in lines:
    if line == "":
        continue
    n = line.split(" = ")[0]
    l, r = line.replace(f"{n} = (", "").replace(")", "").split(", ")
    node = Node(identifier=n, left_identifier=l, right_identifier=r)
    all_nodes[n] = node


steps = 0
current_nodes = {all_nodes[k]: 0 for k in all_nodes if all_nodes[k].ending_identifier == "A"}
founds_nodes = {}
idx = 0
found_ZZZ = False
while not found_ZZZ:
    direction = directions[idx]
    match direction:
        case "L":
            current_nodes = {all_nodes[node.left_identifier]: steps for node in current_nodes}
        case "R":
            current_nodes = {all_nodes[node.right_identifier]: steps for node in current_nodes}
        case _:
            raise WrongDirection(
                f"This direction is wrong: {direction} is not a valid direction ('L' or 'R')."
            )

    steps += 1
    idx += 1

    for node in current_nodes:
        if node.ending_identifier == "Z":
            founds_nodes[node.identifier] = steps

    if len(current_nodes) == len(founds_nodes):
        found_ZZZ = True

    # if all(n if n.ending_identifier == "Z" else None for n in current_nodes):
    #     found_ZZZ = True
    if idx == (len(directions) - 1):
        directions += directions


final_steps_count = lcm(*[int(i) for i in founds_nodes.values()])
print(final_steps_count)

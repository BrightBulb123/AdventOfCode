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
current_node = all_nodes["AAA"]
idx = 0
found_ZZZ = False
while not found_ZZZ:
    direction = directions[idx]
    match direction:
        case "L":
            current_node = all_nodes[current_node.left_identifier]
        case "R":
            current_node = all_nodes[current_node.right_identifier]
        case _:
            raise WrongDirection(
                f"This direction is wrong: {direction} is not a valid direction ('L' or 'R')."
            )

    steps += 1
    idx += 1
    if current_node.identifier == "ZZZ":
        found_ZZZ = True
        break
    if idx == (len(directions) - 1):
        directions += directions

print(steps)

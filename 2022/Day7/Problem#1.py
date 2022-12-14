from __future__ import annotations
from pprint import pprint


file_name = "2022/Day7/Day7TestInput.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return self.__dict__ == __o.__dict__
        else:
            return False

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __repr__(self) -> str:
        return f"{self.name} - {self.size}"


tree: dict[tuple(str, int), list[tuple(str, int) | File]] = {}

current_directory = None
children = []
level = 0

for line in lines:
    if "$" in line:
        if "cd" in line:
            if ".." in line:
                level -= 1
            else:
                if current_directory is not None:
                    tree[current_directory] = children
                children = []

                current_directory = (line.replace("$ cd ", ""), level)
                tree[current_directory] = children
                level += 1
    elif "dir" in line:
        directory = (line.replace("dir ", ""), level)
        children.append(directory)
    else:
        file = File(line.split(" ")[-1], int(line.split(" ")[0]))
        children.append(file)


pprint(tree, compact=True)

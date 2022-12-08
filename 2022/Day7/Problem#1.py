from __future__ import annotations


file_name = "2022/Day7/Day7TestInput.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))


class File:
    def __init__(self, name: str, size: int, parent: Directory) -> None:
        self.name = name
        self.size = size
        self.parent = parent

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return self.__dict__ == __o.__dict__
        else:
            return False

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __repr__(self) -> str:
        return f"[{self.name} - {self.size}]"


class Directory:
    def __init__(
        self,
        name: str,
        level: int = None,
        children: list[File | Directory] = None,
        parent: Directory | None = None,
    ) -> None:
        if children is None:
            children = []
        if level is None:
            level = parent.level + 1
        else:
            self.level = level
        self.parent = None if name == "/" else parent
        self.name = name
        self.children = children
        self.size = self.compute_size()

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return self.__dict__["name"] == __o.__dict__["name"]
        else:
            return False

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __repr__(self) -> str:
        return f"{{{self.name} : {self.size}}}"

    def compute_size(self) -> int:
        if len(self.children) <= 0:
            return 0
        return sum(child.size for child in self.children)


def dir_or_file_fetcher(current_directory: Directory, line: str):
    if "dir" in line:
        return Directory(
            line.split(" ")[1],
            current_directory.level + 1,
            None,
            current_directory,
        )

    size, name = line.split(" ")
    return File(name, int(size), current_directory)


def dir_explorer(current_directory: Directory, line_idx: int) -> list[File | Directory]:
    line_idx += 1
    line = lines[line_idx]
    children = []
    while "$" not in line:
        child = dir_or_file_fetcher(current_directory, line)
        children.append(child)

        line_idx += 1
        if line_idx != len(lines):
            line = lines[line_idx]
        else:
            line = lines[-1]
            line_idx -= 1
            children.append(dir_or_file_fetcher(current_directory, line))
            break

    return children


list_of_directories = [Directory("/", 0)]
children: list[Directory, File] = []

current_directory = list_of_directories[0]
for line_idx, line in enumerate(lines[1:]):  # Already added root
    line_idx += 1
    if "ls" in line:
        current_directory.children = dir_explorer(current_directory, line_idx)
    elif "cd" in line:
        if ".." not in line:
            current_directory = Directory(
                line.split(" ")[1], current_directory.level + 1, None, current_directory
            )
        else:
            current_directory = current_directory.parent


print(list_of_directories)

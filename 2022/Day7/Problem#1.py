import re


file_name = "2022/Day7/Day7TestInput.txt"


with open(file_name) as file:
    lines = map(lambda x: x.replace("\n", ""), file.readlines())


class Directory:
    def __init__(self, name: str, contents=None, parent=None) -> None:
        if contents is None:
            contents = []
        self.name = name
        self.contents = contents
        self.size = self.get_size()
        self.parent = parent

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Directory):
            return NotImplemented

        return self.name == __value.name

    def __hash__(self) -> int:  # Because I implemented __eq__()
        return hash(tuple(self.name))

    def get_size(self) -> int:
        return sum(item.size for item in self.contents)  # 0 if self.contents == []

    def add_to_contents(self, item) -> None:
        if isinstance(item, File):
            if item not in self.contents:
                self.contents.append(item)
        else:
            item.parent = self
            if item in self.contents:
                if item.size >= self.contents[self.contents.index(item)]:
                    self.contents[self.contents.index(item)] = item
            else:
                self.contents.append(item)
            self.size = self.get_size()


class File:
    def __init__(self, name: str, extension: str, size: int) -> None:
        self.name = name
        self.extension = extension
        self.size = size

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, File):
            return NotImplemented

        return (
            self.name == __value.name
            and self.extension == __value.extension
            and self.size == __value.size
        )

    def __hash__(self) -> int:  # Because I implemented __eq__()
        return hash((self.name, self.size))


root = Directory("~")
current_dir = root  # Reference, not a copy, so any changes are still made to root
list_mode = False
for line in lines:
    if "$" in line:
        list_mode = False
        if "cd" in line:
            if ".." in line:
                current_dir = current_dir.parent
            else:
                new_directory = Directory(line.split("$ cd ")[-1])
                current_dir_contents_names = [d.name if isinstance(d, Directory) else None for d in current_dir.contents]
                if new_directory.name not in current_dir_contents_names:
                    current_dir.add_to_contents(new_directory)
                else:
                    new_directory = current_dir.contents[current_dir_contents_names.index(new_directory.name)]
                current_dir = new_directory
        elif "ls" in line:
            list_mode = True
    elif list_mode:
        if "dir" in line:
            name = line.split("dir ")[-1]
            new_directory = Directory(name=name)
            current_dir.add_to_contents(new_directory)
        else:
            size = int(re.split(r"[^0-9]+", line)[0])
            name, extension = re.split(r"\d+ ", line)[-1].split(".")
            f = File(name=name, extension=extension, size=size)
            current_dir.add_to_contents(f)

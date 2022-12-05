import re


file_name = "2022/Day5/Day5Input.txt"

with open(file_name) as file:
    lines = file.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))


class Stack:
    def __init__(self, num: int, crates: list[str]) -> None:
        self.num = num
        self.crates = crates

    def remove_crates(self, amount: int) -> list[str]:
        if len(self.crates) == 0:
            return []
        start_idx = len(self.crates) - amount
        return [self.crates.pop(idx) for idx in range(len(self.crates) - 1, start_idx - 1, -1)][::-1]  # IDK How/Why reversing this works for part 2, it just does...


class StackCollection:
    def __init__(self, stacks: list[Stack]) -> None:
        self.stacks = stacks

    def transfer(self, amount: int, stack_from: int, stack_to: int) -> None:
        stack_from = self.stacks[stack_from - 1]
        stack_to = self.stacks[stack_to - 1]
        crates = stack_from.remove_crates(amount)
        stack_to.crates.extend(crates)

    def __repr__(self) -> str:
        return "\n".join(
            f"{str(stack.num)}: {str(stack.crates)}" for stack in self.stacks
        )


stacks_list = []

line_total = 0
for line in lines:
    if not line:
        break
    if not line.replace(" ", "").isdigit():
        line_total += 1
        if line.endswith("    "):
            line = f"{line[:-4]} [ ]"
        line = line.replace("    ", "[ ] ")
        indexes = [m.start() for m in re.finditer("]", line)]
        chars = [line[idx - 1] for idx in indexes]

        chars = {k + 1: v for k, v in enumerate(chars)}

        stacks_list.append(chars)

    max_columns = len(chars)

stacks = {}

for stack_idx in range(1, max_columns + 1):
    temp = [stack[stack_idx] for stack in stacks_list if stack[stack_idx] != " "]
    stacks[stack_idx] = temp[::-1]


stacks = StackCollection([Stack(idx, stack) for idx, stack in stacks.items()])

instructions = lines[line_total + 2 :]

for instruction in instructions:
    instruction = list(
        map(
            int,
            instruction.replace("move ", "")
            .replace(" from ", "-")
            .replace(" to ", "-")
            .split("-"),
        )
    )
    print(instruction)
    stacks.transfer(instruction[0], instruction[1], instruction[2])

print(stacks)

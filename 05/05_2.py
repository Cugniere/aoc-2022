import collections
import re

def move_crates(stacks, crates, from_stack, to_stack):
    crane_crates = collections.deque(
        [stacks[from_stack].pop() for index in range(crates)]
    )
    for index in range(crates):
        stacks[to_stack].append(crane_crates.pop())


def fill_stack(stacks, line):
    for index in range(0, len(line)):
        if index + 1 not in stacks:
            stacks[index + 1] = collections.deque()
        if line[index].isalpha():
            stacks[index + 1].appendleft(line[index])


def supply_stacks():
    stacks = {}
    parse_stacks = True
    with open("./input") as file:
        for line in file:
            if parse_stacks:
                if line == "\n":
                    parse_stacks = False
                else:
                    fill_stack(stacks, line[1::4])
            else:
                move_crates(stacks, *map(int, re.findall("([\d]+)", line)))
    return "".join([stack.pop() for stack in stacks.values()])


print(supply_stacks())

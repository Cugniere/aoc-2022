# Day 5: Supply Stacks

[instructions](https://adventofcode.com/2022/day/5)

## Part One

Today's challenge was pretty fun! The goal was to move around stack of crates while getting track of which crate went where.

I used some simple code and (again) a `deque` in order to use as less memory as possible:
```python
import collections
import re

def move_crates(stacks, crates, from_stack, to_stack):
    for index in range(crates):
        stacks[to_stack].append(stacks[from_stack].pop())


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
```
The code is a bit messy so here are some explanations:
- when reading the input lines in the `supply_stack` function I first parse the crates stacks and store them in `stacks`, a `dict` of `deques`. Using `deques` allow to insert items at index `0` without much memory consumption
- once all lines describing the crates have been read, we go to the moving crates around part. The `move_crates` function simply use `deque` properties to remove the top crate in a pile and add it a the top of another pile

## Part Two

Interestingly, using `deque` in the fist part makes things more complex in the second part, since we need to move multiple crates at once, keeping their original order and `deque` can't `pop` multiple entries at once.

The code is almost the same as for the first part, except that we need a temporary buffer to hold the crates in their right order:
```python
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
```

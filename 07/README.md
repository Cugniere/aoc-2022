# Day 7: No Space Left On Device

[instructions](https://adventofcode.com/2022/day/7)

## Part One

I think that a lot of people will find that today's problem is way harder than Day 6 even if the guideline is obvious and the input file easy to parse. The main problem here is to find the right data structure to solve the problem.

At first I thought of using a recursive function, however since we need to read each line one after the other, using a simple loop was easier.

Here's my code:
```python
import collections
import re


def scan_device(max_size=100000):
    total_size = 0
    depth_size = collections.deque()
    with open("./input") as file:
        for line in file:
            if re.match("^\$ cd \.\.", line):
                buffer = depth_size.pop()
                if buffer <= max_size:
                    total_size += buffer
                depth_size[-1] += buffer
            elif re.match("^\$ cd", line):
                depth_size.append(0)
            elif re.match("([\d]+)", line):
                depth_size[-1] += int(re.match("([\d]+)", line)[0])

        for depth in depth_size:
            if depth <= max_size:
                total_size += depth
            else:
                break

        if sum(depth_size) <= max_size:
            total_size += sum(depth_size)
        return total_size
```

## Part Two

The second part is kind of the same as the first one, except that we need to store the size of each folder and find the right candidate:
```python
import collections
import re


def scan_device():
    occupied_space = 0
    total_disk_size = 70000000
    required_disk_space = 30000000
    deletion_candidate = 70000000
    directories_size = []

    depth_size = collections.deque()
    with open("./input") as file:
        for line in file:
            if re.match("^\$ cd \.\.", line):
                buffer = depth_size.pop()
                depth_size[-1] += buffer
                directories_size.append(buffer)
            elif re.match("^\$ cd", line):
                depth_size.append(0)
            elif re.match("([\d]+)", line):
                depth_size[-1] += int(re.match("([\d]+)", line)[0])
                occupied_space += int(re.match("([\d]+)", line)[0])

        depth_size.reverse()
        buffer = 0
        for depth in depth_size:
            buffer += depth
            directories_size.append(buffer)

        minimal_required_space = required_disk_space - (
            total_disk_size - occupied_space
        )
        for directory_size in directories_size:
            if (
                directory_size >= minimal_required_space
                and directory_size < deletion_candidate
            ):
                deletion_candidate = directory_size
        return deletion_candidate
```
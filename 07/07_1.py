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


print(scan_device(), scan_device() == 1743217)

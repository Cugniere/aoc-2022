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


print(scan_device(), scan_device() == 8319096)

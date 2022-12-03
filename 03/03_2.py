def group_identification(a, b, c):
    char = ord((set(a) & set(b) & set(c)).pop())
    if char >= 97:
        return char - 96
    else:
        return char - 38


def rucksack_reorganization():
    score = 0
    group = []
    with open("./input") as file:
        for line in file:
            group.append(line.rstrip("\n"))
            if len(group) == 3:
                score += group_identification(*group)
                group.clear()
    return score


print(rucksack_reorganization())

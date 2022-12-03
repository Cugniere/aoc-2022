def item_management(item_list):
    duplicate = ord(
        next(
            iter(
                set(item_list[: len(item_list) // 2])
                & set(item_list[len(item_list) // 2 :])
            )
        )
    )
    if duplicate >= 97:
        return duplicate - 96
    else:
        return duplicate - 38


def rucksack_reorganization():
    score = 0
    with open("./input") as file:
        for line in file:
            score += item_management(line.rstrip("\n"))
    return score


print(rucksack_reorganization())

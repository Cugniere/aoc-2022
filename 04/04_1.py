def pair_inclusion(a, b):
    a = [int(x) for x in a.split("-")]
    b = [int(x) for x in b.split("-")]
    if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
        return 1
    return 0


def camp_cleanup():
    score = 0
    with open("./input") as file:
        for line in file:
            score += pair_inclusion(*line.rstrip("\n").split(","))
    return score


print(camp_cleanup())

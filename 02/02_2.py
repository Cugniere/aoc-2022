def play(a, b):
    a = ord(a) - 64
    b = ord(b) - 87
    if b == 1:
        return (3 * (a == 1)) + (a - 1)
    elif b == 2:
        return 3 + a
    return 6 + (a % 3) + 1


def rps_strategy():
    score = 0
    with open("./input") as file:
        for line in file:
            score += play(*line.rstrip("\n").split(" "))
    return score


print(rps_strategy())

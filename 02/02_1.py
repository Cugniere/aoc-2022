def play(a, b):
    a = ord(a) - 64
    b = ord(b) - 87
    if a == b:
        return 3 + b
    elif ((b - a) != 2 and (a < b)) or (a - b == 2):
        return 6 + b
    return b


def rps_strategy():
    score = 0
    with open("./input") as file:
        for line in file:
            score += play(*line.rstrip("\n").split(" "))
    return score


print(rps_strategy())

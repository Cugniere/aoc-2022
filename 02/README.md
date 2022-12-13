# Day 2: Rock Paper Scissors

[instructions](https://adventofcode.com/2022/day/2)

## Part One

My first thought was to use map in order to be able to match the adversary play to mine, but it is also possible to use the integer representation of the letters:
```python
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
```

The `play` function compare both players hand and return either `3` plus the hand value if it's a tie, `6` plus the hand value if we're winning and just the hand value if we are losing. 

## Part Two

Exactly the same as before except we need to change the value returned depending on the adversary hand:
```python
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
```

# Day 4: Camp Cleanup

[instructions](https://adventofcode.com/2022/day/4)

## Part One

This first part had me hesitating a bit about the code I should produce in order to maximize reusability for today's Part Two.

After some hesitation I went for the simplest code I could think of:
```python
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
```

Not much magic here, I manually compare lower and higher bounds for the pairs in a line.

## Part Two

Second part was even easier, we only need to find if pairs are at least overlapping:
```python
def pair_inclusion(a, b):
    a = [int(x) for x in a.split("-")]
    b = [int(x) for x in b.split("-")]
    if (a[0] <= b[0] and a[1] >= b[0]) or (b[0] <= a[0] and b[1] >= a[0]):
        return 1
    return 0


def camp_cleanup():
    score = 0
    with open("./input") as file:
        for line in file:
            score += pair_inclusion(*line.rstrip("\n").split(","))
    return score
```

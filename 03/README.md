# Day 3: Rucksack Reorganization

[instructions](https://adventofcode.com/2022/day/3)

## Part One

This problem is a classical intersection between 2 lists problem:
```python
def item_management(item_list):
    duplicate = ord(
        (
            set(item_list[: len(item_list) // 2])
            & set(item_list[len(item_list) // 2 :])
        ).pop()
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
```

The `item_management` function may need a bit of explanation:
- first the duplicate variable takes the `item_list` and split it, creating two [Python set](https://docs.python.org/3/tutorial/datastructures.html#sets). The use of the `&` operator create an intersection between both sets, giving us the only item present in both. Finally we use `ord` to get the numerical value of the item
- in a second time we convert the numerical value of the item to the priority order given in the instruction. The unicode value for `a` being higher than the one of `A`, we need to have a basic condition in order to know which number to substract.

Complexity of the code is `O(m+n)` and I really don't see any possible major optimisation.

## Part Two

Second part was really simple following the code I used previously:
```python
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
```
I could technically read the input lines 3 by 3 instead of storing them in an array but I'm too lazy for that.

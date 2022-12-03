# Advent of Code - 2022

## Day 1: Calorie counting

[instructions](https://adventofcode.com/2022/day/1)

### Part One

From a naive perspective today's problem could be solved with a one liner such as : 
```python
max([ sum([int(y) for y in x.split("\n")]) for x in open("./input").read().split("\n\n")[:-1] ])
```
But my goal is to aim for a balanced solution between performance and readability.

My solution is pretty straightforward:
```python
def calorie_counting():
    buffer, max_calorie = 0, 0
    with open("./input") as file:
        for line in file:
            if line == "\n":
                max_calorie = max(max_calorie, buffer)
                buffer = 0
            else:
                buffer += int(line.rstrip("\n"))
    return buffer if buffer > max_calorie else max_calorie
``` 
Since the file is being read line by line memory consumption is minimal and we only need 2 variables to store values between loop:
- `buffer` to store the total amount of calories held by a single Elf
- `max_calorie` to store the maximum amount held by one of the Elf

### Part Two

 [instructions](https://adventofcode.com/2022/day/2)

The second part isn't much more challenging; the only basic optimisation I can see is to not store all the values in a list and get the top 3 at the end but instead to use a stack to minimize memory consumption. In theory there is no limit in number of Elves to count from.

```python
import collections


def calorie_counting_top_n(top_n=3):
    buffer = 0
    max_calorie = collections.deque([0] * top_n, top_n)

    def stack_insert(buffer):
        if buffer > max_calorie[0]:
            max_calorie.popleft()
            index = 0
            while index < top_n - 1:
                if max_calorie[index] < buffer:
                    index += 1
                else:
                    break
            max_calorie.insert(index, buffer)
        return max_calorie

    with open("./input") as file:
        for line in file:
            if line == "\n":
                stack_insert(buffer)
                buffer = 0
            else:
                buffer += int(line.rstrip("\n"))
    return sum(stack_insert(buffer))
``` 

## Day 2: Rock Paper Scissors

### Part One

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

### Part Two

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

## Day 3: Rucksack Reorganization

 [instructions](https://adventofcode.com/2022/day/3)

### Part One

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
- in a second time we convert the numerical value of the item to the priority order given in the instruction. The unicode value for `a` being higher than the one of `A`, we need to have a basic condition in order to know which number to substract


